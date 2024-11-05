from fastapi import FastAPI
from routes.acc_routes import acceleration_api_router
from routes.gyr_routes import orientation_api_router
from routes.dht_routes import environment_api_router
from routes.general_routes import general_api_router

app = FastAPI()

@app.get("/")
def read_root():
    return {
            "message": "Welcome to My API",
            "version": "1.0.0"
    }

app.include_router(general_api_router, tags=["General"])
app.include_router(acceleration_api_router, tags=["Accelerometer"])
app.include_router(orientation_api_router, tags=["Gyroscope"])
app.include_router(environment_api_router, tags=["DHT"])