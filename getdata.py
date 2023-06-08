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

# Declare a random queue with exclusive=True
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the exchange with the routing key 'data'
channel.queue_bind(exchange=rabbitmq_exchange, queue=queue_name, routing_key='data')

# Callback function to process the received messages
def process_message(ch, method, properties, body):
    print("Received data:", body.decode())

# Consume messages from the queue
channel.basic_consume(queue=queue_name, on_message_callback=process_message, auto_ack=True)

# Start consuming messages
print("Waiting for data...")
channel.start_consuming()
