from fastapi import FastAPI
from routes.grafos import grafo
from decouple import config

app = FastAPI()

app.include_router(grafo)


