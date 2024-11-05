from fastapi import APIRouter, HTTPException
from config.database import accelerometer_collection, gyroscope_collection, dht_collection
from models.api_model import Accelerometer, Gyroscope, Environment, GeneralData
from schemas.api_schema import acceleration_serializer, gyroscope_serializer, environment_serializer
#from bson import ObjectId

# Unified API Router
general_api_router = APIRouter()

# Post general
@general_api_router.post("/api/general/")
async def post_general_data(data: GeneralData):
    responses = {}
    
    # Process accelerometer data if provided
    if data.accelerometer:
        acceleration_data = dict(data.accelerometer)
        acceleration_data['int_id'] = accelerometer_collection.count_documents({}) + 1
        accelerometer_collection.insert_one(acceleration_data)
        responses['accelerometer'] = {"status": "ok", "data": acceleration_serializer(acceleration_data)}

    # Process gyroscope data if provided
    if data.gyroscope:
        gyroscope_data = dict(data.gyroscope)
        gyroscope_data['int_id'] = gyroscope_collection.count_documents({}) + 1
        gyroscope_collection.insert_one(gyroscope_data)
        responses['gyroscope'] = {"status": "ok", "data": gyroscope_serializer(gyroscope_data)}

    # Process environment data if provided
    if data.environment:
        environment_data = dict(data.environment)
        environment_data['int_id'] = dht_collection.count_documents({}) + 1
        dht_collection.insert_one(environment_data)
        responses['environment'] = {"status": "ok", "data": environment_serializer(environment_data)}

    # Check if any data was processed
    if not responses:
        raise HTTPException(status_code=400, detail="No valid data provided")

    return responses
