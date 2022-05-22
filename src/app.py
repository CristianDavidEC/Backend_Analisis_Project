from fastapi import FastAPI
from routes.grafos import grafo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  title="FastAPI & Mongo CRUD Grafos.py",
  description="Api rest con MongoDB, FastAPI para operaciones con grafos",
  version="1.0.0",)

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(grafo)

