from fastapi import APIRouter, HTTPException
from config.database import accelerometer_collection
from models.api_model import Accelerometer
from schemas.api_schema import acceleration_serializer, accelerations_serializer
#from bson import ObjectId


acceleration_api_router = APIRouter()

# Retrieve all accelerations
@acceleration_api_router.get("/api/acceleration")
async def get_accelerations():
    accelerations = accelerations_serializer(accelerometer_collection.find({}, {"_id": 0}))
    return {"status": "ok", "data": accelerations}

# Retrieve a specific acceleration by ID
@acceleration_api_router.get("/api/acceleration/{int_id}")
async def get_acceleration(int_id: int):
    acceleration = accelerometer_collection.find_one({"int_id": int_id}, {"_id": 0})
    if not acceleration:
        raise HTTPException(status_code=404, detail="Acceleration not found")
    return {"status": "ok", "data": acceleration_serializer(acceleration)}

    
# Post a new acceleration entry
@acceleration_api_router.post("/api/acceleration")
async def post_acceleration(acceleration: Accelerometer):
    # Convert to dictionary and add an integer ID
    acceleration_data = dict(acceleration)
    # Add the integer ID for each entry based on the count in the database
    acceleration_data['int_id'] = accelerometer_collection.count_documents({}) + 1

    accelerometer_collection.insert_one(acceleration_data)
    return {"status": "ok", "data": acceleration_serializer(acceleration_data)}

# Update an existing acceleration entry
@acceleration_api_router.put("/api/acceleration/{int_id}")
async def update_acceleration(int_id: int, acceleration: Accelerometer): 
    updated_acceleration = accelerometer_collection.find_one_and_update(
        {"int_id": int_id}, {"$set": dict(acceleration)}, return_document=True
    )
    if not updated_acceleration:
        raise HTTPException(status_code=404, detail="Acceleration not found")
    updated_acceleration = acceleration_serializer(updated_acceleration)
    return {"status": "ok", "data": updated_acceleration}
    
# Delete an acceleration entry
@acceleration_api_router.delete("/api/acceleration/{int_id}")
async def delete_acceleration(int_id: int):
    result = accelerometer_collection.find_one_and_delete({"int_id": int_id})
    if not result:
        raise HTTPException(status_code=404, detail="Acceleration not found")
    return {"status": "ok", "data": []}
