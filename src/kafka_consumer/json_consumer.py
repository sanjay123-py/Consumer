import os, sys
import time
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from src.kafka_logger import logging
from src.constants import *
from src.kafka_config import sasl_config
from src.entity.generic import Generic

def consume_data(topic:str, schema_path:str):
    schema_str = Generic.get_schema(schema_path)
    json_deserializer = JSONDeserializer(schema_str, from_dict=Generic.dict_to_instance)

    consumer_conf = sasl_config()
    consumer_conf.update({
        'group.id' : 'group1',
        'auto.offset.reset' : 'earliest'
    })
    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:continue
            record: Generic = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))
            print(record.to_dict())
        except KeyboardInterrupt :
            break
    consumer.close()
