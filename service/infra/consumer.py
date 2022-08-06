import json
import os
from confluent_kafka import Consumer
from decouple import config

TOPIC =  config('KAFKA_TOPIC')
KAFKA_GROUP = config('KAFKA_GROUP')
BOOTSTRAP_SERVERS = config('KAFKA_BOOTSTRAP_SERVERS')


def NewKafkaConsumer() -> Consumer:
    try:
        consumer = Consumer({
            'bootstrap.servers': "localhost:9092",
            'group.id': "simulator",
            'auto.offset.reset': "smallest"
        })
        return consumer
    except Exception as err:
        print(f"Error in kafka consumer {err}")
        raise Exception("Erro on consumer kafka")

def consumer(consumer: Consumer, topic:str) -> list:
    try:
        consumer.subscribe([topic])
        print("Kafka consumer has been started")
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                # Extract the (optional) key and value, and print.
                return {
                    # 'key':msg.key().decode('utf-8'),
                    'topic':msg.topic(),
                    'value':msg.value().decode('utf-8'),
                }
    except Exception as err:
        print(f"Error in kafka consumer {err}")
        consumer.close()
        raise Exception("Erro on consumer kafka")