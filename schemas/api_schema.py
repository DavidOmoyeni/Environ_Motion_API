def acceleration_serializer(acceleration) -> dict:
    return {
        "id": acceleration["int_id"],
        "acc_x": acceleration["acc_x"],
        "acc_y": acceleration["acc_y"],
        "acc_z": acceleration["acc_z"],
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
        "gyr_x": orientation["gyr_x"],
        "gyr_y": orientation["gyr_y"],
        "gyr_z": orientation["gyr_z"],
        "time": str(orientation["time"]),   
    }



def accelerations_serializer(accelerations) -> list:
    return [acceleration_serializer(acceleration) for acceleration in accelerations]

def environments_serializer(environ_infos) -> list:
    return [environment_serializer(environ_info) for environ_info in environ_infos]

def gyroscopes_serializer(orientations) -> list:
    return [gyroscope_serializer(orientation) for orientation in orientations]