import pika, json

params = pika.URLParameters('amqps://kpyuhktm:cD2MB5kgS-twjcQ65-bb4P8FUC1dgtFI@hornet.rmq.cloudamqp.com/kpyuhktm')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)