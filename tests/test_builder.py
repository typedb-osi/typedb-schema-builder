import unittest
from typedbSchemaBuilder import Builder

class TestBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = Builder.Builder()

    def test_abstract(self):
        self.builder.sub("brother","entity")
        self.builder.abstract("brother")
        expected_output= 'define\n'+ 'brother sub entity,\n'+ '    abstract;'
        message = "abstract method failed"
        
        # Add assertions to test the behavior of the abstract function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_sub(self):
        self.builder.sub("sister", "entity")
        expected_output='define\n'+'sister sub entity;'
        message = "sub method failed"
        
        # Add assertions to test the behavior of the sub function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_owns(self):
        self.builder.sub("name","attribute","string")
        self.builder.sub("sister", "entity")
        self.builder.owns("sister","name")
        expected_output="""define
name sub attribute,
    value string;
sister sub entity,
    owns name;"""
        message = "owns method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_owns_as(self):
        self.builder.sub("person","entity")
        self.builder.own_as("person","nickname","name")
        self.builder.sub("name","attribute","string")
        expected_output="""define
person sub entity,
    owns nickname as name;
name sub attribute,
    value string;"""
        message = "owns_as method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_relates(self):
        self.builder.sub("leaderboard","relation")
        self.builder.relates("leaderboard","participant")
        self.builder.relates("leaderboard","rank")
        expected_output = "define\nleaderboard sub relation,\n    relates participant,\n    relates rank;"
        message = "relates method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)


    def test_relates_as(self):
        self.builder.sub("leaderboard","relation")
        self.builder.relates("leaderboard","participant")
        self.builder.relates("leaderboard","rank")
        
        
        self.builder.sub("queue","leaderboard")
        self.builder.relates_as("queue","person","participant")
        self.builder.relates_as("queue","queue_token_number","rank")
        
        expected_output = """define
leaderboard sub relation,
    relates participant,
    relates rank;
queue sub leaderboard,
    owns person as participant,
    owns queue_token_number as rank;"""

        message = "relates_as method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_plays(self):
        self.builder.sub("person", "entity")
        self.builder.sub("ownership", "relation")
        self.builder.relates("ownership", "owner")
        self.builder.plays("person", "ownership", "owner")
        
        expected_output = """define
person sub entity;
ownership sub relation,
    relates owner;
person plays ownership:owner;"""


        message = "plays method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_plays_as(self):
        self.builder.sub("person", "entity")
        self.builder.sub("ownership", "relation")
        self.builder.relates("ownership", "owner")
        self.builder.plays_as("person", "ownership","landlord", "owner")
        
        expected_output = """define
person sub entity;
ownership sub relation,
    relates owner;
person plays ownership:owner as landlord;"""

        message = "plays_as method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

    def test_regex(self):
        self.builder.sub("name","attribute","string")
        self.builder.regex("name","[ABC]*")
        
        expected_output = """define
name sub attribute,
    value string,
    regex "[ABC]*";"""


        message = "regex method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)
        
    def test_key(self):
        self.builder.sub("name","attribute","string")
        self.builder.regex("name","[ABC]*")
        self.builder.sub("person","entity")
        self.builder.owns("person","name")
        self.builder.key("person","name")
        
        expected_output = """define
name sub attribute,
    value string,
    regex "[ABC]*";
person sub entity,
    owns name,
    owns name @key;"""


        message = "key method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)
        
    def test_unique(self):
        self.builder.sub("name","attribute","string")
        self.builder.regex("name","[ABC]*")
        self.builder.sub("person","entity")
        self.builder.owns("person","name")
        self.builder.unique("person","name")
        
        expected_output = """define
name sub attribute,
    value string,
    regex "[ABC]*";
person sub entity,
    owns name,
    owns name @unique;"""


        message = "uninque method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)

        
    def test_remove(self):
        self.builder.sub("name","attribute","string")
        self.builder.regex("name","[ABC]*")
        self.builder.sub("person","entity")
        self.builder.owns("person","name")
        qid=self.builder.unique("person","name")
        self.builder.key("person","name")
        self.builder.remove([qid])

        expected_output = """define
name sub attribute,
    value string,
    regex "[ABC]*";
person sub entity,
    owns name,
    owns name @key;"""



        message = "remove method failed"
        
        # Add assertions to test the behavior of the owns function
        self.assertEqual(self.builder.get_schema(), expected_output, message)


if __name__ == '__main__':
    unittest.main()