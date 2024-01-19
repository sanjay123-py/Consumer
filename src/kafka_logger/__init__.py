import os, sys
import logging
from datetime import datetime
LOG_DIR = "logs"
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR,f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log")
logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.INFO,
                    filemode="w",
                    format='[%(asctime)s]:%(levelname)s:%(lineno)d:%(filename)s:%(funcName)s():%(message)s'
                    )