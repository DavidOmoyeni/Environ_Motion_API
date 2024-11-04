def acceleration_serializer(acceleration) -> dict:
    return {
        "id": acceleration["int_id"],
        "x": acceleration["x"],
        "y": acceleration["y"],
        "z": acceleration["z"],
        "time": str(acceleration["time"])   
    }

def environment_serializer(environ_info) -> dict:
    return {
        "id": environ_info["int_id"],
        "temperature": environ_info["temperature"],
        "humidity": environ_info["humidity"], 
        "time": str(environ_info["time"]) 
    }

def gyroscope_serializer(orientation) -> dict:
    return {
        "id": orientation["int_id"],
        "x": orientation["x"],
        "y": orientation["y"],
        "z": orientation["z"],
        "time": str(orientation["time"]),   
    }



def accelerations_serializer(accelerations) -> list:
    return [acceleration_serializer(acceleration) for acceleration in accelerations]

def environments_serializer(environ_infos) -> list:
    return [environment_serializer(environ_info) for environ_info in environ_infos]

def gyroscopes_serializer(orientations) -> list:
    return [gyroscope_serializer(orientation) for orientation in orientations]