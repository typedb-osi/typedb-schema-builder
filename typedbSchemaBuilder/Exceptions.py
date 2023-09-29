from antlr4 import InputStream, CommonTokenStream
from .TypeQLLexer import TypeQLLexer
from .TypeQLParser import TypeQLParser
from .MyErrorListener import MyErrorListener
from collections import deque
import re
import copy


class SchemaChecker:
    def __init__(self, schema: str, constraints_log: deque, types_: dict) -> None:
        self.schema = schema
        self.constraints_log = constraints_log
        self.types = types_

    def test(self) -> None:
        self.grammar_check(copy.deepcopy(self.schema))
        self.predefined_type_check()
        self.check_regex()
        # self.abstract_match_check()
        self.key_unique_ownership_check()
        # Check for defination availability

    def grammar_check(self, constraints: str) -> bool:
        lexer = TypeQLLexer(InputStream(constraints))
        lexer.removeErrorListeners()  # Remove default error listeners
        lexer.addErrorListener(MyErrorListener())
        stream = CommonTokenStream(lexer)
        parser = TypeQLParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())
        try:
            parser.eof_queries()
        except Exception as e:
            raise Exception(e)

    def check_regex(self) -> None:
        constraints_log_twin = copy.deepcopy(self.constraints_log)
        n = len(constraints_log_twin)
        for i in range(0, n):
            constraints = constraints_log_twin[0]
            constraints_log_twin.popleft()
            if constraints[0] == "regex":
                expression = r"" + constraints[2]
                re.compile(expression)

    # Does not work properly (flawed logic), needs to be re-written after finalising the requirements
    def abstract_match_check(self) -> None:
        constraints_log_twin = copy.deepcopy(self.constraints_log)
        n = len(constraints_log_twin)
        for i in range(0, n):
            constraints = constraints_log_twin[0]
            constraints_log_twin.popleft()
            abstract_count = [0, 0]
            for j in range(0, len(constraints)):
                if constraints[j] in self.types.keys():
                    if len(self.types[constraints[j]].super_types) == 0:
                        continue
                    abstract_count[self.types[constraints[j]].abstract] += 1
            if abstract_count[0] and abstract_count[1]:
                raise Exception("Error: Mixed types\nqid:" + str(constraints[-1]))

    def super_type_check(self) -> None:
        constraints_log_twin = copy.deepcopy(self.constraints_log)
        n = len(constraints_log_twin)
        for i in range(0, n):
            constraints = constraints_log_twin[0]
            constraints_log_twin.popleft()
            if constraints[0] == "sub":
                type = constraints[2]
                subtype = constraints[1]
                if type not in self.types.keys():
                    raise Exception(
                        "Error defining subtype:"
                        + subtype
                        + "\nThe type:"
                        + type
                        + "does not exist\nqid:"
                        + str(constraints[-1]),
                    )
                if subtype in self.types.keys():
                    if len(self.types[subtype].super_types) > 1:
                        raise Exception(
                            "Error defining subtype:"
                            + subtype
                            + "\nThe subtype is already defined\nqid:"
                            + str(constraints[-1])
                        )
                    elif (
                        len(self.types[subtype].super_types)
                        and type not in self.types[subtype].super_types
                    ):
                        raise Exception(
                            "Error defining subtype:"
                            + subtype
                            + "\nThe subtype is already defined\nqid:"
                            + str(constraints[-1])
                        )

    def key_unique_ownership_check(self) -> None:
        constraints_log_twin = copy.deepcopy(self.constraints_log)
        n = len(constraints_log_twin)
        for i in range(0, n):
            constraints = constraints_log_twin[0]
            constraints_log_twin.popleft()
            if constraints[0] == "key" or constraints[0] == "unique":
                type_ = constraints[1]
                owns = constraints[2]
                if owns not in self.types[type_].attributes:
                    message = (
                        "Error: Type = "
                        + type_
                        + " does not own:"
                        + owns
                        + "\nqid:"
                        + str(constraints[-1])
                    )
                    raise Exception(message)

    def predefined_type_check(self) -> None:
        constraints_log_twin = copy.deepcopy(self.constraints_log)
        n = len(constraints_log_twin)
        for i in range(0, n):
            constraints = constraints_log_twin[0]
            constraints_log_twin.popleft()
            if constraints[0] in ["abstract", "value", "regex"]:
                if constraints[1] not in self.types.keys():
                    message = (
                        "Error: type = "
                        + constraints[1]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)

            elif constraints[0] in ["relates", "relates_as"]:
                if constraints[1] not in self.types.keys():
                    message = (
                        "Error: type = "
                        + constraints[1]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
                elif "relation" != self.types[constraints[1]].root_type:
                    message = (
                        "Error:"
                        + constraints[1]
                        + " is not an relation type"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
            elif constraints[0] in ["owns", "owns_as", "key", "unique"]:
                if constraints[1] not in self.types.keys():
                    message = (
                        "Error: type = "
                        + constraints[1]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
                elif "entity" != self.types[constraints[1]].root_type:
                    message = (
                        "Error:"
                        + constraints[1]
                        + " is not an entity type"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)

                if constraints[-2] not in self.types.keys():
                    message = (
                        "Error:"
                        + constraints[-2]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
                elif "attribute" != self.types[constraints[-2]].root_type:
                    message = (
                        "Error:"
                        + constraints[-2]
                        + " is not an attribute type"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
            elif constraints[0] in ["sub"]:
                if constraints[2] not in self.types.keys():
                    message = (
                        "Error: type = "
                        + constraints[2]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
            elif constraints[0] in ["plays", "plays_as"]:
                if constraints[1] not in self.types.keys():
                    message = (
                        "Error: type = "
                        + constraints[1]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
                if "entity" != self.types[constraints[1]].root_type:
                    message = (
                        "Error: not entity, type = "
                        + constraints[1]
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)

                if constraints[2] not in self.types.keys():
                    message = (
                        "Error: relationship type = "
                        + constraints[2]
                        + " is not defined"
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
                if "relation" != self.types[constraints[2]].root_type:
                    message = (
                        "Error: not relationship, type = "
                        + constraints[2]
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)

                if constraints[-2] not in self.types[constraints[2]].relation_roles:
                    message = (
                        "Error: relationship type = "
                        + constraints[2]
                        + " has no role = "
                        + constraints[-2]
                        + "\nqid: "
                        + str(constraints[-1])
                    )
                    raise Exception(message)
