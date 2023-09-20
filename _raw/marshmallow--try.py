from datetime import date
from pprint import pprint
from pathlib import Path
from marshmallow import Schema, fields, validates, ValidationError, validates_schema
from dataclasses import make_dataclass


class PathField(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        return None if value is None else str(value)

    def _deserialize(self, value, attr, data, **kwargs):
        return None if value is None else Path(value)

class BaseMessageSchema(Schema):

    def dumps(self):
        print("DUMP!")
        return super().dumps()



class BaseObjectSchema(BaseMessageSchema):
    VALID_ACTIONS = ("create","upsert","delete")

    _action = fields.Str(required=True)
    msgType = fields.Str(required=True)
    uid = fields.Str(load_default=None)

    @validates("msgType")
    def validate_msgType(self, value):
        if value != self.__msgType__:
            raise ValidationError(f"Invalid msgType type: {value}")

    @validates("_action")
    def validate_action(self, value):
        if value not in self.VALID_ACTIONS:
            raise ValidationError(f"Invalid action type: {value}")

    @validates_schema
    def validate_action_uid(self, data, **kwargs):
        if data["_action"] == "create":
            if data["uid"] is not None:
                raise ValidationError("create action must have uid=None")
        else:
            if data["uid"] is None:
                raise ValidationError("non create action must have valid uid")

    # SEE:
    # https://marshmallow.readthedocs.io/en/stable/quickstart.html#deserializing-to-objects
    # To generate an object

class DirectorySchema(BaseObjectSchema):
    __msgType__ = "Directory"
    path = PathField(required=True)
    name = fields.Str(load_default=None)
    parent_path = PathField(load_default=None)
    int_val = fields.Integer(load_default=0)
    float_val = fields.Float(load_default=0.0)
    bool_val = fields.Boolean(load_default=True)

directory_schema = DirectorySchema()

# Experiment with:
# class GroupResponse(Schema):
#     objects = fields.List(fields.Nested(BaseObjectSchema))

def generate_dataclass(class_name, schema):
    # https://docs.python.org/3/library/dataclasses.html#dataclasses.make_dataclass
    # we can pass in a base class
    _mapping = []
    for k,f in directory_schema.declared_fields.items():
        _t = None
        if isinstance(f,fields.Str):
            _t = str
        elif isinstance(f,PathField):
            _t = Path
        elif isinstance(f,(fields.Int,fields.Integer)):
            _t = int
        elif isinstance(f,fields.Float):
            _t = float
        elif isinstance(f,fields.Boolean):
            _t = bool
        else:
            _t = str
        _mapping.append((k,_t))

    return make_dataclass(class_name,_mapping)


Directory = generate_dataclass("Directory",directory_schema)

print('-'*32)
dobj = directory_schema.load({
    "msgType": "Directory",
    "_action": "create",
    "path": "/a/b/cat"
})
pprint(dobj)
d123 = Directory(**dobj)
pprint(d123)

print('-'*32)
try:
    d = directory_schema.load({
        "msgType": "Directoryq",
        "_action": "upsert",
        "uid": "WUDG",
        "path": "/a/b/cat",
        "name": "cat",
        "parent_path": "/a/b"
    })
    pprint(d)
except ValidationError as e:
    print("Error:",e)

print('-'*32)
r = directory_schema.load({
    "msgType": "Directory",
    "_action": "upsert",
    "uid": "WUDG",
    "path": "/a/b/cat",
    "name": "cat",
    "parent_path": "/a/b"
})
pprint(r)
obj = directory_schema.dump(r)
pprint(obj)

# breakpoint()
