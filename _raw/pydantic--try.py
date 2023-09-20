from datetime import date
from pprint import pprint
from typing import ClassVar

from pydantic import BaseModel

class BaseMessage(BaseModel):
    pass

class BaseObject(BaseMessage):
    VALID_ACTIONS: ClassVar[tuple] = ("create","upsert","delete")

    _action: str


class Directory(BaseObject):
    msgType = "Directory"

    uid: str
    path: str
    name: str
    parent_path: str


e1_dict = {
    "_action": "upsert",
    "uid": "WUDG",
    "path": "/a/b/cat",
    "name": "cat",
    "parent_path": "/a/b"
}
e1 = Directory(**e1_dict)
pprint(e1.json())
# breakpoint()



