from fastapi import APIRouter, HTTPException
from config.database import dht_collection
from models.api_model import Environment
from schemas.api_schema import environment_serializer, environments_serializer
#from bson import ObjectId

environment_api_router = APIRouter()

# Retrieve all accelerations
@environment_api_router.get("/api/environment/")
async def get_environ_infos():
    environ_infos = environments_serializer(dht_collection.find({}, {"_id": 0}))
    return {"status": "ok", "data": environ_infos}

# Retrieve a specific acceleration by ID
@environment_api_router.get("/api/environment/{int_id}")
async def get_environ_info(int_id: int):
    environ_info = dht_collection.find_one({"int_id": int_id}, {"_id": 0})
    if not environ_info:
        raise HTTPException(status_code=404, detail="Environ_info not found")
    return {"status": "ok", "data": environment_serializer(environ_info)}

    
# Post a new acceleration entry
@environment_api_router.post("/api/environment/")
async def post_orientation(environ_info: Environment):
    # Convert to dictionary and add an integer ID
    environ_info_data = dict(environ_info)
    # Add the integer ID for each entry based on the count in the database
    environ_info_data['int_id'] = dht_collection.count_documents({}) + 1

    dht_collection.insert_one(environ_info_data)
    return {"status": "ok", "data": environment_serializer(environ_info_data)}

# Update an existing acceleration entry
@environment_api_router.put("/api/environment/{int_id}")
async def update_environ_info(int_id: int, environ_info: Environment): 
    updated_environ_info = dht_collection.find_one_and_update(
        {"int_id": int_id}, {"$set": dict(environ_info)}, return_document=True
    )
    if not updated_environ_info:
        raise HTTPException(status_code=404, detail="Environ_info not found")
    updated_environ_info = environment_serializer(updated_environ_info)
    return {"status": "ok", "data": updated_environ_info}
    
# Delete an acceleration entry
@environment_api_router.delete("/api/environment/{int_id}")
async def delete_environ_info(int_id: int):
    result = dht_collection.find_one_and_delete({"int_id": int_id})
    if not result:
        raise HTTPException(status_code=404, detail="Environ_info not found")
    return {"status": "ok", "data": []}
