import environ

def get_token():
    return environ.get("TOKEN")

def get_url():
    return environ.get("URL")