import time
import requests
import datetime
import confluent_kafka
# from kafka import KafkaProducer
# from kafka import KafkaProducer

# time.sleep(10)
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
# future = producer.send('test-topic', b'raw_bytes')
# print(88888888888)
# conf = {'bootstrap.servers': 'localhost:29092', "security.protocol": "SSL", 'default.topic.config': {'api.version.request': False},}
# conf = {'bootstrap.servers': '172.20.0.3:29092'}

# print(99999999999999999999)
# producer = confluent_kafka.Producer(conf)

# TOPIC_SALE = 'wal_listener.public_billboard_sale'
# TOPIC_CATEGORY = 'wal_listener.public_billboard_category'


# def delivery_report(err, msg):
#     if err is not None:
#         print(f'Ошибка доставки сообщения: {err}')
#     else:
#         print(f'Сообщение доставлено в {msg.topic()} [{msg.partition()}]')
# producer.produce("all", value="hello", callback=delivery_report)
# print(99999999999999999999)

# producer.poll(0)
# producer.flush()
# print("999999999999999999999999999999999999999999999999")
# deadline = time.monotonic() + 5
# while time.monotonic() < deadline:
#     url = "https://docs.google.com/spreadsheets/d/1rbUMw-YmpSBfNQPW5L6-C80BB9vvxx7l/export?format=xlsx"
#     # url = ' https://docs.google.com/spreadsheets/d/1bckdpp4i-J0iFszaE-tqODnVhfNutyHKCW5wdFFD8-Y/export?format=xlsx'
#     response = requests.get(url)
#     with open('timetable.xlsx', "wb") as file:
#         producer.produce("all", value="hello", callback=delivery_report)
#         producer.poll(0)
#         producer.flush()
#         file.write(response.content)
#         print("999999999999999999999999999999999999999999999999")
#     time.sleep(5)

from pika import ConnectionParameters, BlockingConnection
import time
import pika



# time.sleep(40)
connection_params = ConnectionParameters(
    # host = "0.0.0.0",
    host = "172.18.0.2",
    port = 5672,
)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare("ИСП ПР")
deadline = time.monotonic() + 5
while time.monotonic() < deadline:
    url = "https://docs.google.com/spreadsheets/d/1rbUMw-YmpSBfNQPW5L6-C80BB9vvxx7l/export?format=xlsx"
    # url = ' https://docs.google.com/spreadsheets/d/1bckdpp4i-J0iFszaE-tqODnVhfNutyHKCW5wdFFD8-Y/export?format=xlsx'
    response = requests.get(url)
    with open('timetable.xlsx', "wb") as file:
        file.write(response.content)
        channel.basic_publish(exchange='',
                              routing_key='ИСП ПР',
                              body='Hello World!')
        
        print("999999999999999999999999999999999999999999999999")
    time.sleep(5)

print(" [x] Sent 'Hello World!'")
# with BlockingConnection(connection_params) as conn:
#     with conn.channel() as ch:
#         ch.queue_declare(queue="hello")
#         ch.basic_publish(
#             exchange="",
#             routing_key="",
#             body="Hello RabbitMQ!"
#         )
#         print(6666666666666666)


# from rabbitmq import RabbitMQ
# import time
# time.sleep(10)
# def callback(ch, method, properties, body):
#     print(f"Received {body}")


# try:
#     rabbitmq = RabbitMQ()
#     message = 'Test message'
#     rabbitmq.publish(message)
#     print(f"Sent message: {message}")
#     rabbitmq.close()
# except:
#     print("fuck")
#     time.sleep(10)
#     rabbitmq = RabbitMQ()
#     message = 'Test message'
#     rabbitmq.publish(message)
#     print(f"Sent message: {message}")
#     rabbitmq.close()