import base64
from pymongo.mongo_client import MongoClient

uri = base64.b64decode(
    "bW9uZ29kYjovL3Jvb3Q6cm9vdEBhYy1sd2xpemVnLXNoYXJkLTAwLTAwLndrZnZxYnAubW9uZ29kYi5uZXQ6MjcwMTcsYWMtbHdsaXplZy1zaGFyZC0wMC0wMS53a2Z2cWJwLm1vbmdvZGIubmV0OjI3MDE3LGFjLWx3bGl6ZWctc2hhcmQtMDAtMDIud2tmdnFicC5tb25nb2RiLm5ldDoyNzAxNy8/c3NsPXRydWUmcmVwbGljYVNldD1hdGxhcy1sa2dwcXUtc2hhcmQtMCZhdXRoU291cmNlPWFkbWluJnJldHJ5V3JpdGVzPXRydWUmdz1tYWpvcml0eQ=="
).decode("utf-8")

# Create a new client and connect to the server
client = MongoClient(uri)


# Send a ping to confirm a successful connection
def ping():
    try:
        client.admin.command('ping')
        print("You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
