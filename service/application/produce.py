from time import sleep
from infra.producer import NewKafkaProducer, publish
from .models import Route
from .core import load_positions, export_json_positions

def send_messages_in_kafka(message:dict):
    producer = NewKafkaProducer()
    router = Route(id=message['route_id'], client_id=message['client_id'])
    load_positions(router)
    for position in export_json_positions(router):
        data_position= {
           "routeId:":position.ID,
           "clientId:":position.client_id,
           "position:":position.position,
           "finished:":position.fineshed,
        }
        publish(msg=data_position, topic='readtest', producer=producer)
        sleep(1)
        
    