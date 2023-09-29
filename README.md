# TypeDB Schema Builder

TypeDB schema builder package can be used to construct a TypeQL define constraint with native Python code.

## Installation

Install using pip:
``` 
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ typedb-schema-builder
```

## Methods

Functions offered:

* get_schema():
  
  Returns schema string and prints schema string.

* abstract(type: str):

  Makes type abstract. Returns qid attached to the constraint.

* sub(subtype: str, type: str,value: str):

  Create a new type given as argument "subtype" with supertype given as argument "type". The value parameter needs to be mentioned only when defining types with root type "attribute". Returns qid attached to the constraint.

* owns(type: str, owns: str):

  Assigns ownership of attribute given as argument "owns" to type given as argument "type". Returns qid attached to the constraint.

* owns_as(type: str, to_own: str, from_own: str):

  Assigns ownership of attribute given as argument "from_own" to alias given as argument "to_own" to type given as argument "type". Returns qid attached to the constraint.

* relates(type: str, role: str):

  Adds a role given as argument "role" to a relationship type given as argument "type". Returns qid attached to the constraint.

* relates_as(type: str, to_role: str, from_role: str):

  Adds a role given as argument "from_role" to an alias given as argument "to_role" to type given as argument "type". Returns qid attached to the constraint.

* plays(type: str, relation: str, role: str):

  Assigns the relation:role, where relation is given as argument "relation" and role is given as argument "role" to the type given as argument "type". Returns qid attached to the constraint.

* plays_as(type: str, relation: str, to_role: str, from_role: str):

  Assigns the relation:role, where relation is given as argument "relation" and role is given as argument "from_role" to alias given as "to_role" to the type given as argument "type". Returns qid attached to the constraint.

* regex(type: str, regex: str):

  Adds a regex pattern given as argument "regex" to attribute type given as argument "type". Returns qid attached to the constraint.

* key(type: str, attribute: str):

  Makes the attribute given as argument "attribute" that is owned by type given as argument "type" a @key attribute.

* unique(self, type: str, attribute: str):

  Makes the attribute given as an argument "attribute" that is owned by type given as argument "type" a @unique attribute. Returns qid attached to the constraint.

* print_constraint_log():

  Prints all the constraint IDs attached to every constraint.

## Usage

1. [Install](#installation) the package.
2. Import the `Builder` from the package in your code. 
3. Instantiate the `Builder.Builder()`.
4. Use [methods](#methods) mentioned above to construct a constraint.
5. Use `get_schema()` method to retrieve TypeQL constraint.

### Example

The following is a Python code usage example:
```
from typedbSchemaBuilder import Builder
      
builder=Builder.Builder()
      
builder.sub("person", "entity")
builder.sub("ownership", "relation")
builder.relates("ownership", "owner")
builder.plays("person", "ownership", "owner")
      
builder.get_schema()
```
The above example produces the following output:

```
define
person sub entity;
ownership sub relation,
    relates owner;
person plays ownership:owner;
```
