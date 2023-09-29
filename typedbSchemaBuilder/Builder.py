from collections import deque
from .Type import Type
from .Exceptions import SchemaChecker
import copy


class Builder:
    def __init__(self) -> None:
        self._schema = "define"
        self._context = "?#"
        self._constraint_log = deque()
        self._constraint_id_generator = 1
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
        if len(self._constraint_log) == 0:
            raise Exception(
                "Error: Schema is empty. Make changes to the schema before attempting GetSchema"
            )

        n = len(self._constraint_log)
        self._schema = "define"
        self._context = "?#"

        old_constraint_log = deque()
        old_constraint_log, self._constraint_log = self._constraint_log, old_constraint_log

        self.init_types()

        for i in range(0, n):
            constraint = old_constraint_log[0]
            old_constraint_log.popleft()
            self.make_constraint(constraint)

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

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["abstract", type_, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["abstract", type_, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()
        self._types[type_].abstract = True
        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

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

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["sub", subtype, type_, value, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["sub", subtype, type_, value, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()
        checker.super_type_check()

        self._types[subtype] = Type(subtype)
        self._types[subtype].inherit(self._types[type_])
        self._types[subtype].add_super_type(type_)

        self._constraint_log = constraint_log

        return self._constraint_log[-1][-1]

    def owns(self, type_: str, owns: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + owns + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + owns + ";"

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["owns", type_, owns, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["owns", type_, owns, qid])

        if type_ in self._types.keys():
            self._types[type_].add_attribute(owns)
        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

    def own_as(self, type_: str, to_own: str, from_own: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + to_own + " as " + from_own + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + to_own + " as " + from_own + ";"

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(
                ["own_as", type_, to_own, from_own, self._constraint_id_generator]
            )
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["own_as", type_, to_own, from_own, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_attribute(to_own)
        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

    def relates(self, type_: str, role: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    relates " + role + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " relates " + role + ";"

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["relates", type_, role, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["relates", type_, role, qid])
        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_relation_roles(role)

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

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

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(
                ["relates_as", type_, to_role, from_role, self._constraint_id_generator]
            )
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["relates_as", type_, to_role, from_role, qid])

        self._types[type_].add_relation_roles(from_role)
        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

    def plays(self, type_: str, relation: str, role: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    plays " + relation + ":" + role + ";"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " plays " + relation + ":" + role + ";"

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["plays", type_, relation, role, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["plays", type_, relation, role, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_role(relation, role)

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

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

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(
                [
                    "plays_as",
                    type_,
                    relation,
                    to_role,
                    from_role,
                    self._constraint_id_generator,
                ]
            )
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["plays_as", type_, relation, to_role, from_role, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()
        self._types[type_].add_role(relation, to_role)
        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

    # value should be added while subtyping attribute
    # def value(self, type_: str, value: str, qid: int=-1):
    #     if self._context == type_:
    #         if self._schema[-1] == ";":
    #             self._schema = self._schema[:-1] + ","
    #         self._schema += "\n    value " + value + ";"
    #     else:
    #         self._context = type_
    #         self._schema += "\n" + type_ + " value " + value + ";"

    #     constraint_log=copy.deepcopy(self._constraint_log)
    #     if(qid==-1):
    #         constraint_log.append(["value", type_, value, self._constraint_id_generator])
    #         self._constraint_id_generator += 1
    #     else:
    #         constraint_log.append(["value", type_, value, qid])

    #     checker = SchemaChecker (
    #         schema=self._schema, constraint_log=constraint_log, types_=self._types
    #     )
    #     checker.test()

    #     self._constraint_log=constraint_log
    #     return self._constraint_log[-1][-1]

    def regex(self, type_: str, regex: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += '\n    regex "' + regex + '";'
        else:
            self._context = type_
            self._schema += "\n" + type_ + ' regex "' + regex + '";'

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["regex", type_, regex, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["regex", type_, regex, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

    def key(self, type_: str, attribute: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + attribute + " @key;"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + attribute + " @key;"

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["key", type_, attribute, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["key", type_, attribute, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return constraint_log[-1][-1]

    def unique(self, type_: str, attribute: str, qid: int = -1):
        if self._context == type_:
            if self._schema[-1] == ";":
                self._schema = self._schema[:-1] + ","
            self._schema += "\n    owns " + attribute + " @unique;"
        else:
            self._context = type_
            self._schema += "\n" + type_ + " owns " + attribute + " @unique;"

        constraint_log = copy.deepcopy(self._constraint_log)
        if qid == -1:
            constraint_log.append(["unique", type_, attribute, self._constraint_id_generator])
            self._constraint_id_generator += 1
        else:
            constraint_log.append(["unique", type_, attribute, qid])

        checker = SchemaChecker(
            schema=self._schema, constraint_log=constraint_log, types_=self._types
        )
        checker.test()

        self._constraint_log = constraint_log
        return self._constraint_log[-1][-1]

    # idea for remove recontrust schema after negating some constraints using constraint ids and reconstructing schema
    def make_constraint(self, constraint: list):
        constraint_type = constraint[0]
        getattr(self, constraint_type)(*constraint[1:])

    def print_constraint_log(self):
        for q in self._constraint_log:
            print(q)
