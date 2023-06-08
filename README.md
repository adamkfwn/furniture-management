# KEA facility management

The Furniture Management System is a simple application that allows users to manage furniture items through a graphical user interface (GUI). It provides features for adding and deleting furniture items using an API.



## Requirements

Python 3

tkinter library

pika library

mysql-connector-python library

requests library
## Installation

Clone the repository:
git clone: https://github.com/adamkfwn/furniture-management.git

And install the required libraries
## Usage

1. Start the RabbitMQ server on your local machine.
2. Run the following scripts in separate terminals:
    python3 UI.py
    python3 API.py
    python3 sender.py
3. The GUI window will open, providing options to add and delete furniture items.
4. Enter the furniture ID and name in the respective fields and click the "Add Furniture" button to add a new item.
5. To delete a furniture item, enter its ID in the appropriate field and click the "Delete Furniture" button.
6. Messages regarding successful operations or errors will be displayed through message boxes.
## Scripts

The project consists of the following scripts:

1. UI.py: This script creates a graphical user interface using the tkinter library. It allows users to interact with the application by entering furniture details and performing actions.
2. API.py: This script acts as a consumer for the furniture API. It connects to RabbitMQ and listens for messages containing furniture data. Upon receiving a message, it updates the MySQL database with the furniture information.
3. sender.py: This script acts as a producer for the furniture API. It sends messages containing furniture data to the RabbitMQ exchange, which are then consumed by the furniture_consumer script.
4. FurnitureDB.sql: This script contains the SQL commands to create the necessary database tables and insert initial data for the furniture management microservice file names FurnitureMS.py.
