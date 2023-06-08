from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

# Define model
class Sensor(BaseModel):
    id: int
    sensor_name: str
    sensor_type: str

# MySQL connection for the sensor database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kimojimmi1",
    database="KEA_FM_sensors"
)

app = FastAPI()

# Add sensor
@app.post("/sensors")
async def add_sensor(sensor: Sensor):
    cursor = db.cursor()
    try:
        query = "INSERT INTO Sensor (id, sensor_name, sensor_type) VALUES (%s, %s, %s)"
        values = (sensor.id, sensor.sensor_name, sensor.sensor_type)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Sensor added successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error adding sensor")
    finally:
        cursor.close()

# Delete sensor
@app.delete("/sensors/{sensor_id}")
async def delete_sensor(sensor_id: int):
    cursor = db.cursor()
    try:
        query = "DELETE FROM Sensor WHERE id = %s"
        value = (sensor_id,)
        cursor.execute(query, value)
        db.commit()
        if cursor.rowcount < 1:
            raise HTTPException(status_code=404, detail="Sensor not found")
        return {"message": "Sensor deleted successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error deleting sensor")
    finally:
        cursor.close()

# View sensors
@app.get("/sensors")
async def view_sensors():
    cursor = db.cursor()
    try:
        query = "SELECT * FROM Sensor"
        cursor.execute(query)
        sensors = []
        for row in cursor.fetchall():
            sensor = {
                "id": row[0],
                "sensor_name": row[1],
                "sensor_type": row[2]
            }
            sensors.append(sensor)
        return sensors
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error fetching sensors")
    finally:
        cursor.close()
