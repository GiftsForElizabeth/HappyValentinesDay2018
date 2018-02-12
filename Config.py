from os import environ

def get_token():
    return environ.get('TOKEN')

def get_url():
    return environ.get('URL')

def get_uri():
    return environ.get('DB_URI')

def get_host():
    return environ.get('DB_HOST')

def get_database():
    return environ.get('DATABASE')

def get_port():
    return environ.get('DB_PORT')

def get_user():
    return environ.get('DB_USER')

def get_password():
    return environ.get('DB_PASSWORD')
