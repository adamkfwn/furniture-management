import pika

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
rabbitmq_username = 'guest'
rabbitmq_password = 'guest'
rabbitmq_exchange = 'furniture_exchange'

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=rabbitmq_host,
    port=rabbitmq_port,
    credentials=pika.PlainCredentials(username=rabbitmq_username, password=rabbitmq_password)
))
channel = connection.channel()

# Declare the exchange
channel.exchange_declare(exchange=rabbitmq_exchange, exchange_type='direct')

# Function to send an order
def send_order(order):
    # Publish the order to the exchange with the routing key 'order'
    channel.basic_publish(exchange=rabbitmq_exchange, routing_key='order', body=order)
    print("Order sent:", order)

# Send example orders
send_order("Add Furniture: Chair, ID: 1, Name: Chair 1")
send_order("Add Furniture: Desk, ID: 2, Name: Desk 1")
send_order("Delete Furniture: Chair, ID: 1")

# Close the connection
connection.close()
