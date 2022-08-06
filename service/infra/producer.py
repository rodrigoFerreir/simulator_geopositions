import json
from datetime import datetime
from confluent_kafka import Producer
from decouple import config


BOOTSTRAP_SERVERS =  config('KAFKA_BOOTSTRAP_SERVERS')

def NewKafkaProducer() -> Producer:
    try:
        producer = Producer({
            'bootstrap.servers':'localhost:9092',
        })
        return producer

    except Exception as err:
        print(f"Error in kafka producer {err}")
        raise Exception("Erro on producer kafka")


def publish(msg:str, topic:str, producer:Producer):
    try:
        value_message = json.dumps({
            "topic": topic,
            "message": msg,
            "date_time": str(datetime.now())
        }, ensure_ascii=False, indent=2)

        producer.produce(
            topic=topic,
            value=value_message
        )
        producer.flush()
    except Exception as err:
        print(err)
        raise Exception('Erro in pusblish kafka')