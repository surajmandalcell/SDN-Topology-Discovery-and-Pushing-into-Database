import base64
from pymongo.mongo_client import MongoClient

uri = base64.b64decode(
    "bW9uZ29kYitzcnY6Ly9yb290OnJvb3RAY2x1c3RlcjAud2tmdnFicC5tb25nb2RiLm5ldC8/cmV0cnlXcml0ZXM9dHJ1ZSZ3PW1ham9yaXR5"
).decode("utf-8")

# Create a new client and connect to the server
client = MongoClient(uri)
collection = client.get_database("cluster0").get_collection("logs")


# Send a ping to confirm a successful connection
def ping():
    try:
        client.admin.command('ping')
        print("You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def db_push(log_dict):
    try:
        collection.insert_one(log_dict)
        print("Successfully inserted log into MongoDB")
    except Exception as e:
        print(e)
