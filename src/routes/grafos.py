from unittest import result
from bson import ObjectId
from fastapi import APIRouter, Response, status
from config.mongodb import db
from schemas.grafoSchema import grafoEntity, grafosEntity
from models.grafoModel import Grafo, GrafoOut


grafo = APIRouter()

# Consulta todos los grafos
@grafo.get("/grafos", tags = ["Grafos"],
            status_code = status.HTTP_200_OK,
            response_model = list[GrafoOut])
async def find_all_grafos():
    return grafosEntity(db.grafos.find())


# Consultad un grafo por id
@grafo.get("/grafos/{id}", tags = ["Grafos"],
            status_code = status.HTTP_200_OK,
            response_model = GrafoOut)
async def find_grafo(id: str):
    grafo = db.grafos.find_one({'_id': ObjectId(id)})
    return grafoEntity(db.grafos.find_one({'_id': ObjectId(id)}))


# Crea un nuevo grafo
@grafo.post("/grafos", tags = ["Grafos"],
            status_code = status.HTTP_201_CREATED,
            response_model = GrafoOut)
async def create_grafo(grafo: Grafo):
    new_grafo = dict(grafo)
    id = db.grafos.insert_one(new_grafo).inserted_id
    return grafoEntity(db.grafos.find_one({'_id': id}))


# Actualiza los datos de un grafo por su id
@grafo.put("/grafos/{id}", tags = ["Grafos"],
            status_code = status.HTTP_200_OK,
            response_model=GrafoOut)
async def update_grafo(id: str, grafo: Grafo):
    db.grafos.find_one_and_update({
            '_id': ObjectId(id)
        },{
            '$set': dict(grafo)
        })
    return grafoEntity(db.grafos.find_one({'_id': ObjectId(id)}))


# Elimina un grafo por su id
@grafo.delete("/grafos/{id}", tags = ["Grafos"],
                status_code = status.HTTP_204_NO_CONTENT)
async def delete_grafo(id: str):
    data = db.grafos.find_one_and_delete({
        '_id': ObjectId(id)
        })
    return ( Response(status_code = status.HTTP_204_NO_CONTENT) if data 
            else Response(status_code = status.HTTP_404_NOT_FOUND) ) 