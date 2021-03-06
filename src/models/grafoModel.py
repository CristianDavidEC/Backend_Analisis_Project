from typing import Optional
from pydantic import BaseModel
from bson import ObjectId

class Grafo(BaseModel):
    _id: ObjectId
    name: str
    descripcion: str
    nodes: list [dict]

class GrafoOut(BaseModel):
    id: str
    name: str
    descripcion: str
    nodes: list [dict]