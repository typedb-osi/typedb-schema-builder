# python-typedb-schema-builder
typedb schema builder package

How to test the builder out:
1. Install using pip
   ``` 
      py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ typedb-schema-builder
   ```
2. Create builder_instance and use following methods offered via builder instance to create your schemas

   Example:
   
      ```
      from typedbSchemaBuilder import Builder
      
      builder=Builder.Builder()
      
      builder.sub("person", "entity")
      builder.sub("ownership", "relation")
      builder.relates("ownership", "owner")
      builder.plays("person", "ownership", "owner")
      
      builder.get_schema()
      ```
      ```
      Output:
         define
         person sub entity;
         ownership sub relation,
             relates owner;
         person plays ownership:owner;
      ```
Functions offered:

* builder_instance.get_schema():
Returns schema string and prints schema string.

* builder_instance.abstract(type: str):
Makes type abstract. Returns qid attached to the query.

* builder_instance.sub(subtype: str, type: str,value: str):
Create a new type given as argument "subtype" with supertype given as argument "type". The value parameter needs to be mentioned only when defining types with root type "attribute". Returns qid attached to the query.

* builder_instance.owns(type: str, owns: str):
Assigns ownership of attribute given as argument "owns" to type given as argument "type". Returns qid attached to the query.

* builder_instance.owns_as(type: str, to_own: str, from_own: str):
Assigns ownership of attribute given as argument "from_own" to alias given as argument "to_own" to type given as argument "type". Returns qid attached to the query.

* builder_instance.relates(type: str, role: str):
Adds a role given as argument "role" to a relationship type given as argument "type". Returns qid attached to the query.

* builder_instance.relates_as(type: str, to_role: str, from_role: str):
Adds a role given as argument "from_role" to an alias given as argument "to_role" to type given as argument "type". Returns qid attached to the query.

* builder_instance.plays(type: str, relation: str, role: str):
Assigns the relation:role, where relation is given as argument "relation" and role is given as argument "role" to the type given as argument "type". Returns qid attached to the query.

* builder_instance.plays_as(type: str, relation: str, to_role: str, from_role: str):
Assigns the relation:role, where relation is given as argument "relation" and role is given as argument "from_role" to alias given as "to_role" to the type given as argument "type". Returns qid attached to the query.

* builder_instance.regex(type: str, regex: str):
Adds a regex pattern given as argument "regex" to attribute type given as argument "type". Returns qid attached to the query.

* builder_instance.key(type: str, attribute: str):
Makes the attribute given as atrgument "attribute" that is owned by type given as argument "type" a @key attribute.

* builder_instance.unique(self, type: str, attribute: str):
Makes the attribute given as atrgument "attribute" that is owned by type given as argument "type" a @unique attribute. Returns qid attached to the query.

* builder_instance.print_query_log():
Prints all the query IDs attached to every query.

* builder_instance.remove(q_ids: list):
Removes all the queries given in list argument "q_ids". And re-renders the remaining queries.
