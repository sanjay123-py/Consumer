import os, sys
import time
import json
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
    en = 0
    s3 = Generic.s3_obj()
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:continue
            en = en+1
            record: Generic = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))
            s3object = s3.Object(BUCKET_NAME, f'rating-data-{en}.json')
            s3object.put(
                Body=(bytes(json.dumps(record.to_dict()).encode('UTF-8')))
            )
        except KeyboardInterrupt:
            break
    consumer.close()
