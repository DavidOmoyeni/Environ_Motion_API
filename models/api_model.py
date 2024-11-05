from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class Accelerometer(BaseModel):
    id: Optional[int]=None
    acc_x: str
    acc_y: str
    acc_z: str
    time: Optional[datetime]=None

    # Validator to round x, y, and z to two decimal places
    @validator('acc_x', 'acc_y', 'acc_z', pre=True, always=True)
    def convert_to_string(cls, v):
        return str(round(float(v), 2))
    
    # Automatically set the current time if `time` is not provided
    @validator('time', pre=True, always=True)
    def set_default_time(cls, v):
        return v or datetime.now()

class Gyroscope(BaseModel):
    id: Optional[int]=None
    gyr_x: str
    gyr_y: str
    gyr_z: str
    time: Optional[datetime]=None

    # Validator to round x, y, and z to two decimal places
    @validator('gyr_x', 'gyr_y', 'gyr_z', pre=True, always=True)
    def convert_to_string(cls, v):
        return str(round(float(v), 2))
    
    # Automatically set the current time if `time` is not provided
    @validator('time', pre=True, always=True)
    def set_default_time(cls, v):
        return v or datetime.now()

class Environment(BaseModel):
    id: Optional[int]=None
    temperature: str
    humidity: str
    time: Optional[datetime]=None

    # Validator to round x, y, and z to two decimal places
    @validator('temperature', 'humidity', pre=True, always=True)
    def convert_to_string(cls, v):
        return str(round(float(v), 2))
    
    # Automatically set the current time if `time` is not provided
    @validator('time', pre=True, always=True)
    def set_default_time(cls, v):
        return v or datetime.now()
    

# Define a unified schema for the general endpoint
class GeneralData(BaseModel):
    accelerometer: Optional[Accelerometer] = None
    gyroscope: Optional[Gyroscope] = None
    environment: Optional[Environment] = None




