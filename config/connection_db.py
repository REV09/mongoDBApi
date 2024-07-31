from pymongo.mongo_client import MongoClient


def get_connection() -> MongoClient:
    uri = ("mongodb+srv://isdavidM23:HALOcea206-@moviedb.zaedaaf.mongodb.net/?retryWrites=true&w=majority&appName"
           "=movieDB")
    client = MongoClient(uri, connect=False)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client
