from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

# Define model
class Hallway(BaseModel):
    hallway_id: int
    hallway_name: str

class Classroom(BaseModel):
    classroom_id: int
    classroom_name: str

# MySQL connection for the location database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kimojimmi1",
    database="KEA_FM_location"
)

app = FastAPI()

# Add hallway
@app.post("/hallways")
async def add_hallway(hallway: Hallway):
    cursor = db.cursor()
    try:
        query = "INSERT INTO Hallway (hallway_id, hallway_name) VALUES (%s, %s)"
        values = (hallway.hallway_id, hallway.hallway_name)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Hallway added successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error adding hallway")
    finally:
        cursor.close()

# Add classroom
@app.post("/classrooms")
async def add_classroom(classroom: Classroom):
    cursor = db.cursor()
    try:
        query = "INSERT INTO Classroom (classroom_id, classroom_name) VALUES (%s, %s)"
        values = (classroom.classroom_id, classroom.classroom_name)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Classroom added successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error adding classroom")
    finally:
        cursor.close()

# Delete hallway
@app.delete("/hallways/{hallway_id}")
async def delete_hallway(hallway_id: int):
    cursor = db.cursor()
    try:
        query = "DELETE FROM Hallway WHERE hallway_id = %s"
        value = (hallway_id,)
        cursor.execute(query, value)
        db.commit()
        if cursor.rowcount < 1:
            raise HTTPException(status_code=404, detail="Hallway not found")
        return {"message": "Hallway deleted successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error deleting hallway")
    finally:
        cursor.close()

# Delete classroom
@app.delete("/classrooms/{classroom_id}")
async def delete_classroom(classroom_id: int):
    cursor = db.cursor()
    try:
        query = "DELETE FROM Classroom WHERE classroom_id = %s"
        value = (classroom_id,)
        cursor.execute(query, value)
        db.commit()
        if cursor.rowcount < 1:
            raise HTTPException(status_code=404, detail="Classroom not found")
        return {"message": "Classroom deleted successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error deleting classroom")
    finally:
        cursor.close()

# View hallways
@app.get("/hallways")
async def view_hallways():
    cursor = db.cursor()
    try:
        query = "SELECT * FROM Hallway"
        cursor.execute(query)
        hallways = []
        for row in cursor.fetchall():
            hallway = {
                "hallway_id": row[0],
                "hallway_name": row[1]
            }
            hallways.append(hallway)
        return hallways
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error fetching")
