import random
import json

def generate_id():
    return str(random.randint(100000000000, 999999999999))

def validate_id(identifier):
    if len(identifier) == 12:
        try:
            int(identifier)
            return True
        except:
            return False
    return False

