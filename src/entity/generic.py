import logging
import os, sys
import json
import pandas as pd
import numpy as np
from src.constants import SCHEMA_FILE_PATH
from src.kafka_logger import logging
class Generic:

    def __init__(self, record:dict):
        for k,v in record.items():
            setattr(self, k, v)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def dict_to_instance(cls,dict_1:dict,ctx):
        print(dict_1, ctx)
        return cls(dict_1)
    @classmethod
    def get_object(cls, data_path:str):
        try:
            columns = Generic.get_columns(SCHEMA_FILE_PATH)
            with open(data_path, 'rb') as f:
                for line in f:
                    line = str(line.strip())[2:].split('::')
                    generic = Generic(dict(zip(columns,line)))
                    yield generic
        except Exception as e:
            logging.info(e)

    @classmethod
    def get_schema(cls,schema_file_path:str):
        try:
            schema=dict()
            schema.update({
                "$id": "http://example.com/myURI.schema.json",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "additionalProperties": False,
                "description": "Sample schema to help you get started.",
                "properties": dict(),
                "title": "SampleRecord",
                "type": "object"})
            columns = Generic.get_columns(schema_file_path)
            for column in columns:
                schema['properties'].update(
                    {
                        f'{column}' :
                            {
                                "discription" : f'generic {column}',
                                "type" : "string"
                            }
                    }
                )
            schema = json.dumps(schema)
            return schema
        except Exception as e:
            logging.info(e)
    @staticmethod
    def get_columns(file_path:str):
        with open(file_path, 'r') as f:
            columns = f.readline().strip().split(',')
        return columns

def instance_to_dict(instance: Generic, ctx):
    return instance.to_dict()