from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

# Define model
class Furniture(BaseModel):
    id: int
    name: str

# MySQL connection for the furniture database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kimojimmi1",
    database="KEA_FM_furniture"
)

app = FastAPI()

# Add furniture
@app.post("/furniture")
async def add_furniture(furniture: Furniture):
    cursor = db.cursor()
    try:
        table_name = furniture.name.lower()
        query = f"INSERT INTO {table_name} (id, name) VALUES (%s, %s)"
        values = (furniture.id, furniture.name)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Furniture added successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error adding furniture")
    finally:
        cursor.close()

# Delete furniture
@app.delete("/furniture/{furniture_id}/{table_name}")
async def delete_furniture(furniture_id: int, table_name: str):
    cursor = db.cursor()
    try:
        table_name = table_name.lower()
        query = f"DELETE FROM {table_name} WHERE id = %s"
        value = (furniture_id,)
        cursor.execute(query, value)
        db.commit()
        if cursor.rowcount < 1:
            raise HTTPException(status_code=404, detail="Furniture not found")
        return {"message": "Furniture deleted successfully"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error deleting furniture")
    finally:
        cursor.close()

# View furniture
@app.get("/furniture/{table_name}")
async def view_furniture(table_name: str):
    cursor = db.cursor()
    try:
        table_name = table_name.lower()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        furniture = []
        for row in cursor.fetchall():
            furniture_item = {
                "id": row[0],
                "name": row[1]
            }
            furniture.append(furniture_item)
        return furniture
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Error retrieving furniture")
    finally:
        cursor.close()
