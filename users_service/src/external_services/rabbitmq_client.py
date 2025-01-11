import pika
import json

def send_message(queue_name: str, message: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange="", routing_key=queue_name, body=json.dumps(message))
    connection.close()

def receive_message(queue_name: str, callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(f"Listening to queue: {queue_name}")
    channel.start_consuming()
