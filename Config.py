from os import environ

def get_token():
    return environ.get('TOKEN')

def get_url():
    return environ.get('URL')

def get_uri():
    return environ.get('URI')

def get_host():
    return environ.get('HOST')

def get_database():
    return environ.get('DATABASE')

def get_port():
    return environ.get('PORT')

def get_user():
    return environ.get('USER')

def get_password():
    return environ.get('PASSWORD')
