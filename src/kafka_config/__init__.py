import os, sys

API_KEY = os.getenv('API_KEY', None)

ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL', None)

API_SECRET_KEY = os.getenv('API_SECRET_KEY', None)

BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER', None)

SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)

SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET', None)

SECURITY_PROTOCOL = "SASL_SSL"

SSL_MECHANISM = "PLAIN"

def sasl_config():
    sasl_conf = {
        'sasl.mechanism' : SSL_MECHANISM,
        'bootstrap.servers' : BOOTSTRAP_SERVER,
        'security.protocol' : SECURITY_PROTOCOL,
        'sasl.username' : API_KEY,
        'sasl.password' : API_SECRET_KEY
        }
    return sasl_conf

def schema_config():
    return {
        'url' : ENDPOINT_SCHEMA_URL,
        'basic.auth.user.info' : f'{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}'
    }