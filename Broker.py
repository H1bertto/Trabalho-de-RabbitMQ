import pika
import sys


class Broker:
    def __init__(self, key, msg, tela=None):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

        channel.basic_publish(exchange='topic_logs', routing_key=key, body=msg)
        # print(" [x] Sent %r:%r" % (routing_key, message))
        tela.write(" [x] Sent %r:%r" % (key, msg))
        connection.close()