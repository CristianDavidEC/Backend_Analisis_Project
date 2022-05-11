from pymongo import MongoClient
from decouple import config

coneccion = MongoClient()

#client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
#db = client.college