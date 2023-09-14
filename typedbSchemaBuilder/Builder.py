from collections import deque
from .Type import Type
from .Exceptions import SchemaChecker
import copy


class Builder:
    def __init__(self) -> None:
        self._schema = "define"
        self._context = "?#"
        self._query_log = deque()
        self._query_id_generator = 1
        self._types = dict()
        self.init_types()

    def init_types(self):
        self._types = {
            "attribute": Type("attribute"),
            "entity": Type("entity"),
            "relation": Type("relation"),
        }
        self._types["attribute"].root_type = "attribute"
        self._types["entity"].root_type = "entity"
        self._types["relation"].root_type = "relation"

    def get_schema(self):
        if len(self._query_log) == 0:
            raise Exception(
                "Error: Schema is empty. Make changes to the schema before attempting GetSchema"
            )

        n = len(self._query_log)
        self._schema = "define"
        self._context = "?#"

        old_query_log = deque()
        old_query_log, self._query_log = self._query_log, old_query_log

        self.init_types()

        for i in range(0, n):
            query = old_query_log[0]
            old_query_log.popleft()
            self.make_query(query)

        escaped_string = r"" + self._schema
        decoded_string = bytes(escaped_string, "utf-8").decode("unicode_escape")
        print(decoded_string)
        return decoded_string

    def abstract(self, type_: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    abstract;"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " abstract;"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["abstract", type_, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["abstract", type_, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()
        self._types[type_].abstract = True
        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    def sub(self, subtype: str, type_: str, value: str = None, qid: int = -1):
        self._context = subtype
        if value is not None:
            if self._types[type_].root_type == "attribute":
                self._schema += "\n" + subtype + " sub " + type_ + ","
                self._schema += "\n    value " + value + ";"
            else:
                raise Exception("Non attribute type cannot have a value")
        else:
            self._schema += "\n" + subtype + " sub " + type_ + ";"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["sub", subtype, type_, value, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["sub", subtype, type_, value, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()
        checker.super_type_check()

        self._types[subtype] = Type(subtype)
        self._types[subtype].inherit(self._types[type_])
        self._types[subtype].add_super_type(type_)

        self._query_log = query_log

        return self._query_log[-1][-1]

    def owns(self, type_: str, owns: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + owns + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + owns + ";"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["owns", type_, owns, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["owns", type_, owns, qid])

        if type_ in self._types.keys():
            self._types[type_].add_attribute(owns)
        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    def own_as(self, type_: str, to_own: str, from_own: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + to_own + " as " + from_own + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + to_own + " as " + from_own + ";"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(
                ["own_as", type_, to_own, from_own, self._query_id_generator]
            )
            self._query_id_generator += 1
        else:
            query_log.append(["own_as", type_, to_own, from_own, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_attribute(to_own)
        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    def relates(self, type_: str, role: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    relates " + role + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " relates " + role + ";"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["relates", type_, role, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["relates", type_, role, qid])
        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_relation_roles(role)

        self._query_log = query_log
        return self._query_log[-1][-1]

    def relates_as(self, type_, to_role: str, from_role: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + to_role + " as " + from_role + ";"
        else:
            self._context = type_
            self._schema += (
                "\n" + type_ + " relates " + to_role + " as " + from_role + ";"
            )

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(
                ["relates_as", type_, to_role, from_role, self._query_id_generator]
            )
            self._query_id_generator += 1
        else:
            query_log.append(["relates_as", type_, to_role, from_role, qid])

        self._types[type_].add_relation_roles(from_role)
        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    def plays(self, type_: str, relation: str, role: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    plays " + relation + ":" + role + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " plays " + relation + ":" + role + ";"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["plays", type_, relation, role, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["plays", type_, relation, role, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_role(relation, role)

        self._query_log = query_log
        return self._query_log[-1][-1]

    def plays_as(
        self, type_: str, relation: str, to_role: str, from_role: str, qid: int = -1
    ):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += (
                "\n    plays " + relation + ":" + from_role + " as " + to_role + ";"
            )
        else:
            self._context = type_
            self._schema += (
                "\n"
                + type_
                + " plays "
                + relation
                + ":"
                + from_role
                + " as "
                + to_role
                + ";"
            )

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(
                [
                    "plays_as",
                    type_,
                    relation,
                    to_role,
                    from_role,
                    self._query_id_generator,
                ]
            )
            self._query_id_generator += 1
        else:
            query_log.append(["plays_as", type_, relation, to_role, from_role, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_role(relation, to_role)
        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    # value should be added while subtyping attribute
    # def value(self, type_: str, value: str, qid: int=-1):
    #     if self._context == type_:
    #         if self._schema[-1] == ";":
    #             self._schema = self._schema[:-1] + ","
    #         self._schema += "\n    value " + value + ";"
    #     else:
    #         self._context = type_
    #         self._schema += "\n" + type_ + " value " + value + ";"

    #     query_log=copy.deepcopy(self._query_log)
    #     if(qid==-1):
    #         query_log.append(["value", type_, value, self._query_id_generator])
    #         self._query_id_generator += 1
    #     else:
    #         query_log.append(["value", type_, value, qid])

    #     checker = SchemaChecker (
    #         schema=self._schema, query_log=query_log, types_=self._types
    #     )
    #     checker.test()

    #     self._query_log=query_log
    #     return self._query_log[-1][-1]

    def regex(self, type_: str, regex: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += '\n    regex "' + regex + '";'
        else:
            self._context = type_
            self._schema += "\n" + type_ + ' regex "' + regex + '";'

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["regex", type_, regex, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["regex", type_, regex, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    def key(self, type_: str, attribute: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + attribute + " @key;"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + attribute + " @key;"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["key", type_, attribute, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["key", type_, attribute, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return query_log[-1][-1]

    def unique(self, type_: str, attribute: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + attribute + " @unique;"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + attribute + " @unique;"

        query_log = copy.deepcopy(self._query_log)
        if qid == -1:
            query_log.append(["unique", type_, attribute, self._query_id_generator])
            self._query_id_generator += 1
        else:
            query_log.append(["unique", type_, attribute, qid])

        checker = SchemaChecker(
            schema=self._schema, query_log=query_log, types_=self._types
        )
        checker.test()

        self._query_log = query_log
        return self._query_log[-1][-1]

    # idea for remove recontrust schema after negating some queries using query ids and reconstructing schema
    def make_query(self, query: list):
        query_type = query[0]
        getattr(self, query_type)(*query[1:])

    def remove(self, q_ids: list):
        n = len(self._query_log)
        self._schema = "define"
        self._context = "?#"

        old_query_log = deque()
        old_query_log, self._query_log = self._query_log, old_query_log

        self.init_types()
        for i in range(0, n):
            query = old_query_log[0]
            old_query_log.popleft()
            if query[-1] in q_ids:
                continue
            self.make_query(query)

    def print_query_log(self):
        for q in self._query_log:
            print(q)
