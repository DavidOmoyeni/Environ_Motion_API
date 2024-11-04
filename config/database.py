from pymongo.mongo_client import MongoClient

url = "mongodb+srv://omoyenido17:hPgJWOMm4XfnCm85@environmentapi.55s2i.mongodb.net/?retryWrites=true&w=majority&appName=EnvironmentAPI"
client = MongoClient(url)
db = client.Monitoring_application

accelerometer_collection  = db["Accelerometer"]
gyroscope_collection  = db["Gyroscope"]
dht_collection = db["DHT"]
