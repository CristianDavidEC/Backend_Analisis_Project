from fastapi import FastAPI
from routes.grafos import grafo

app = FastAPI(
  title="FastAPI & Mongo CRUD Grafos.py",
  description="Api rest con MongoDB, FastAPI para operaciones con grafos",
  version="1.0.0",)

app.include_router(grafo)

