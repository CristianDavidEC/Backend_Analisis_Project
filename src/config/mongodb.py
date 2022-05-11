from pymongo import MongoClient
from decouple import config


url = config("MONGODB_URL")
#print(url)
coneccion = MongoClient(url)
db = coneccion.GrafoDB
print(db)
print(db.grafos)

#client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
#db = client.college