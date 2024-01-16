import pika, json

params = pika.URLParameters('amqps://ftilqnia:uk9yY1kACUiMSDdreeiRoSXvXzbVO-DJ@fish.rmq.cloudamqp.com/ftilqnia')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)