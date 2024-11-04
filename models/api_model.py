from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class Accelerometer(BaseModel):
    id: Optional[int]=None
    x: float
    y: float
    z: float
    time: Optional[datetime]=None

    # Validator to round x, y, and z to two decimal places
    @validator('x', 'y', 'z', pre=True, always=True)
    def round_to_two_decimal(cls, v):
        return round(v, 2)
    
    # Automatically set the current time if `time` is not provided
    @validator('time', pre=True, always=True)
    def set_default_time(cls, v):
        return v or datetime.now()

class Gyroscope(BaseModel):
    id: Optional[int]=None
    x: float
    y: float
    z: float
    time: Optional[datetime]=None

    # Validator to round x, y, and z to two decimal places
    @validator('x', 'y', 'z', pre=True, always=True)
    def round_to_two_decimal(cls, v):
        return round(v, 2)
    
    # Automatically set the current time if `time` is not provided
    @validator('time', pre=True, always=True)
    def set_default_time(cls, v):
        return v or datetime.now()

class Environment(BaseModel):
    id: Optional[int]=None
    temperature: float
    humidity: float
    time: Optional[datetime]=None

    # Validator to round x, y, and z to two decimal places
    @validator('temperature', 'humidity', pre=True, always=True)
    def round_to_two_decimal(cls, v):
        return round(v, 2)
    
    # Automatically set the current time if `time` is not provided
    @validator('time', pre=True, always=True)
    def set_default_time(cls, v):
        return v or datetime.now()




