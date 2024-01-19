# import os
# list_of_files=[
#     './consumer_main.py',
#     './producer_main.py',
#     './setup.py',
#     './requirements.txt',
#     './sample_data/movie_analytics_data/',
#     './src/__init__.py',
#     './src/constants/',
#     './src/kafka_config/',
#     './src/kafka_consumer/',
#     './src/kafka_producer/',
#     './src/kafka_logger/',
#     './src/kafka_config/__init__.py',
#     './src/constants/__init__.py',
#     './src/kafka_consumer/__init__.py',
#     './src/kafka_producer/__init__.py',
#     './src/kafka_logger/__init__.py',
#     './src/kafka_consumer/json_consumer.py',
#     './src/kafka_producer/json_producer.py',
#     './src/entity/__init__.py',
#     './src/entity/generic.py',
#
# ]
#
# for file in list_of_files:
#     file_dir,file_name = os.path.split(file)
#     os.makedirs(file_dir,exist_ok=True)
#     if not os.path.exists(file):
#         with open(file,'w') as f:
#             pass
#     else:
#         print(f'{file}---Already Exist..')
# from src.entity.generic import Generic
# from src.constants import DATA_PATH
# import time
# c=0
# for i in Generic.get_object(DATA_PATH):
#     print(i.to_dict())
#     if c % 10 == 0 : time.sleep(2)
#     c=c+1
