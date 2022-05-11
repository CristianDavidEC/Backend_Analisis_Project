from copyreg import constructor
from urllib import response
from fastapi import APIRouter, Response
from config.mongodb import db
from schemas.grafoSchema import grafoEntity, grafosEntity
from models.grafoModel import Grafo
from starlette.status import HTTP_204_NO_CONTENT

grafo = APIRouter()

# Consulta todos los grafos
@grafo.get("/grafos")
def find_all_grafos() :
    return grafosEntity(db.grafos.find())

# Consultad un grafo por id
@grafo.get("/grafos/{id}") 
def find_grafo( id : str ) :
    print(id)
    return grafoEntity(db.grafos.find_one({'id': id}))

# Crea un nuevo grafo
@grafo.post("/grafos")
def create_grafo(grafo : Grafo) :
    new_grafo = dict(grafo)
    id = db.grafos.insert_one(new_grafo).inserted_id
    nuevo = db.grafos.find_one({'_id': id})
    return grafoEntity(nuevo)

# Actualiza los datos de un grafo por su id
@grafo.put("/grafos/{id}")
def update_grafo():
    return "Hola"

# Elimina un grafo por su id
@grafo.delete("/grafos/{id}")
def delete_grafo( id : str ) :
    grafoEntity(db.grafos.find_one_and_delete({'id': id}))
    return Response(status_code = HTTP_204_NO_CONTENT)