import tkinter as tk
from tkinter import messagebox
import requests

# Set the base URL for the furniture API
furniture_base_url = 'localhost'

# Function to handle the Add Furniture button click
def add_furniture():
    furniture_id = entry_furniture_id.get()
    furniture_name = entry_furniture_name.get()
    data = {
        "id": furniture_id,
        "name": furniture_name
    }
    try:
        response = requests.post(furniture_base_url, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Furniture added successfully")
            clear_entries()
        else:
            messagebox.showerror("Error", "Failed to add furniture")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Connection error")

# Function to handle the Delete Furniture button click
def delete_furniture():
    furniture_id = entry_furniture_id.get()
    url = f"{furniture_base_url}/{furniture_id}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Furniture deleted successfully")
            clear_entries()
        elif response.status_code == 404:
            messagebox.showerror("Error", "Furniture not found")
        else:
            messagebox.showerror("Error", "Failed to delete furniture")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Connection error")

# Function to clear the entry fields
def clear_entries():
    entry_furniture_id.delete(0, tk.END)
    entry_furniture_name.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Furniture Management")
window.geometry("400x200")

# Create the furniture ID label and entry field
label_furniture_id = tk.Label(window, text="Furniture ID:")
label_furniture_id.pack()
entry_furniture_id = tk.Entry(window)
entry_furniture_id.pack()

# Create the furniture name label and entry field
label_furniture_name = tk.Label(window, text="Furniture Name:")
label_furniture_name.pack()
entry_furniture_name = tk.Entry(window)
entry_furniture_name.pack()

# Create the Add Furniture button
button_add_furniture = tk.Button(window, text="Add Furniture", command=add_furniture)
button_add_furniture.pack()

# Create the Delete Furniture button
button_delete_furniture = tk.Button(window, text="Delete Furniture", command=delete_furniture)
button_delete_furniture.pack()

# Run the main event loop
window.mainloop()
