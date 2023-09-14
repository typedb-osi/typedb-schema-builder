class Type:
    def __init__(self, name: str):
        self.name = name
        self.super_types = set()
        self.abstract = False
        self.roles = set()
        self.relation_roles = set()
        self.attributes = set()
        self.root_type="None"
        self.value: str=None

    def inherit(self,parent: "Type"=None):
        self.super_types=parent.super_types
        # Ignoring Abstract types for now
        # self.abstract = type.abstract
        self.roles=parent.roles
        self.relation_roles=parent.relation_roles
        self.attributes=parent.attributes
        self.root_type=parent.root_type
        
    def add_super_type(self, type_: str):
        self.super_types.add(type_)

    def set_abstract(self, positive: bool):
        self.abstract = positive

    def add_role(self, relation: str, role: str):
        self.roles.add((relation, role))

    def add_relation_roles(self, role: str):
        self.relation_roles.add(role)

    def add_attribute(self, attribute: str):
        self.attributes.add(attribute)
        
    def set_value(self,value: str):
        self.value=value
