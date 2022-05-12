from bson import ObjectId
from fastapi import APIRouter, Response, status
from config.mongodb import db
from schemas.grafoSchema import grafoEntity, grafosEntity
from models.grafoModel import Grafo
from starlette.status import HTTP_204_NO_CONTENT

grafo = APIRouter()

# Consulta todos los grafos
@grafo.get("/grafos", tags = ["Grafos"])
async def find_all_grafos():
    return grafosEntity(db.grafos.find())
 

# Consultad un grafo por id
@grafo.get("/grafos/{id}", tags = ["Grafos"])
async def find_grafo(id: str):
    return grafoEntity(db.grafos.find_one({'_id': ObjectId(id)}))


# Crea un nuevo grafo
@grafo.post("/grafos", tags = ["Grafos"])
async def create_grafo(grafo: Grafo):
    new_grafo = dict(grafo)
    id = db.grafos.insert_one(new_grafo).inserted_id
    nuevo_grafo = db.grafos.find_one({'_id': id})
    print(nuevo_grafo)
    return grafoEntity(nuevo_grafo)


# Actualiza los datos de un grafo por su id
@grafo.put("/grafos/{id}", tags = ["Grafos"])
async def update_grafo(id: str, grafo: Grafo):
    db.grafos.find_one_and_update({
            '_id': ObjectId(id)
        },{
            '$set': dict(grafo)
        })
    return grafoEntity(db.grafos.find_one({'_id': ObjectId(id)}))


# Elimina un grafo por su id
@grafo.delete("/grafos/{id}", 
            status_code = status.HTTP_204_NO_CONTENT,
            tags = ["Grafos"])
async def delete_grafo(id: str):
    db.grafos.find_one_and_delete({
        '_id': ObjectId(id)
        })
    return Response(status_code = HTTP_204_NO_CONTENT)
