import requests
import json



def add_queue(description, creator_id):
    url = 'http://127.0.0.1:5000/queues/add_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'description': description,
        'creator_id': creator_id,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def add_user_to_queue(queue_identifier, user_id):
    url = 'http://127.0.0.1:5000/queues/add_user_to_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier,
        'user_id': user_id,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_queue(queue_identifier):
    url = 'http://127.0.0.1:5000/queues/get_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)
def delete_user_from_queue(queue_identifier, user_id):
    url = 'http://127.0.0.1:5000/queues/delete_user_from_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier,
        'user_id': user_id,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

add_user_to_queue("123123123123", "456654289987")
#get_queue("123123123123"):
