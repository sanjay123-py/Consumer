import os, sys
from src.kafka_consumer.json_consumer import consume_data
from src.constants import TOPIC, SCHEMA_FILE_PATH
try:
    consume_data(TOPIC, SCHEMA_FILE_PATH)
except Exception as e:
    print(e)