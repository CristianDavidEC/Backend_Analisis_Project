from fastapi import APIRouter
from config.mongodb import coneccion
from schemas.grafoSchema import grafoEntity, grafosEntity
from models.grafoModel import Grafo

grafo = APIRouter()

@grafo.get("/grafos")
def find_all_grafos():
    return grafosEntity(coneccion.local.grafos.find())

@grafo.get("/grafos/{id}") 
def find_grafo():
    return "Hola"

@grafo.post("/grafos")
def create_grafo(grafo : Grafo):
    new_grafo = dict(grafo)
    id = coneccion.local.grafos.insert_one(new_grafo).inserted_id
    return str(id)

@grafo.put("/grafos/{id}")
def update_grafo():
    return "Hola"

@grafo.delete("/grafos/{id}")
def delete_grafo():
    return "Hola"