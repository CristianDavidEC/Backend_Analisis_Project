from typing import Optional
from pydantic import BaseModel

class Grafo(BaseModel):
    #id: Optional[str]
    name: str
    descripcion: str 
    nodes: list [dict]
