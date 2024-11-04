from fastapi import APIRouter, HTTPException
from config.database import gyroscope_collection
from models.api_model import Gyroscope
from schemas.api_schema import gyroscope_serializer, gyroscopes_serializer
#from bson import ObjectId

orientation_api_router = APIRouter()

# Retrieve all accelerations
@orientation_api_router.get("/api/orientation")
async def get_orientations():
    orientations = gyroscopes_serializer(gyroscope_collection.find({}, {"_id": 0}))
    return {"status": "ok", "data": orientations}

# Retrieve a specific acceleration by ID
@orientation_api_router.get("/api/orientation/{int_id}")
async def get_orientation(int_id: int):
    orientation = gyroscope_collection.find_one({"int_id": int_id}, {"_id": 0})
    if not orientation:
        raise HTTPException(status_code=404, detail="Orientation not found")
    return {"status": "ok", "data": gyroscope_serializer(orientation)}

    
# Post a new acceleration entry
@orientation_api_router.post("/api/orientation")
async def post_orientation(orientation: Gyroscope):
    # Convert to dictionary and add an integer ID
    orientation_data = dict(orientation)
    # Add the integer ID for each entry based on the count in the database
    orientation_data['int_id'] = gyroscope_collection.count_documents({}) + 1

    gyroscope_collection.insert_one(orientation_data)
    return {"status": "ok", "data": gyroscope_serializer(orientation_data)}

# Update an existing acceleration entry
@orientation_api_router.put("/api/orientation/{int_id}")
async def update_orientation(int_id: int, orientation: Gyroscope): 
    updated_orientation = gyroscope_collection.find_one_and_update(
        {"int_id": int_id}, {"$set": dict(orientation)}, return_document=True
    )
    if not updated_orientation:
        raise HTTPException(status_code=404, detail="Orientation not found")
    updated_orientation = gyroscope_serializer(updated_orientation)
    return {"status": "ok", "data": updated_orientation}
    
# Delete an acceleration entry
@orientation_api_router.delete("/api/orientation/{int_id}")
async def delete_orientation(int_id: int):
    result = gyroscope_collection.find_one_and_delete({"int_id": int_id})
    if not result:
        raise HTTPException(status_code=404, detail="Orientation not found")
    return {"status": "ok", "data": []}
