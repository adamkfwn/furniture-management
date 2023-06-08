import pika
import mysql.connector
import json

# RabbitMQ configuration
rabbitmq_url = "amqp://guest:guest@localhost:5672/"
exchange_name = "furniture_exchange"

# MySQL configuration
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "Kimojimmi1"
mysql_database = "KEA_FM_furniture"

# Establish a connection to MySQL
mysql_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# Function to handle database updates
def update_furniture(ch, method, properties, body):
    furniture_data = json.loads(body)
    furniture_id = furniture_data["id"]
    furniture_name = furniture_data["name"]

    # Perform the database update
    try:
        cursor = mysql_connection.cursor()
        cursor.execute("INSERT INTO Chair (id, name) VALUES (%s, %s)", (furniture_id, furniture_name))
        mysql_connection.commit()
        cursor.close()
        print("Furniture added to the database")
    except mysql.connector.Error as error:
        print(f"Failed to add furniture to the database: {error}")

    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Create a connection to RabbitMQ
rabbitmq_connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@localhost/%2f"))
channel = rabbitmq_connection.channel()

# Create the furniture queue and bind it to the exchange
channel.queue_declare(queue="furniture_queue")
channel.queue_bind(exchange=exchange_name, queue="furniture_queue", routing_key="furniture")

# Set the prefetch count to control the number of unacknowledged messages
channel.basic_qos(prefetch_count=1)

# Set up a consumer to receive messages
channel.basic_consume(queue="furniture_queue", on_message_callback=update_furniture)

# Start consuming messages
print("Waiting for messages. To exit, press CTRL+C")
channel.start_consuming()
