import os
import pika
import random
import threading


def fact_recursion(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    return num * fact_recursion(num - 1)


def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))


def sendmessage():
    threading.Timer(2.0, sendmessage).start()
    random_number = fact_recursion(random.randint(0, 20))
    url = os.environ.get('CLOUDAMQP_URL',
                         'amqps://fzqwaiqz:10T0_WISg6Ci7Np80K_Ybu5A9UIecnAd@rattlesnake.rmq.cloudamqp.com/fzqwaiqz')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    random_number = fact_recursion(random.randint(0, 20))
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='hello')  # Declare a queue
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=f"Random number is {random_number}")

    print(f" [x] Sent Random number, {random_number}")

    channel.basic_consume('hello',
                          callback,
                          auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
    connection.close()


if __name__ == '__main__':
    sendmessage()
