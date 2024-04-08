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

def add_user(user_name):
    url = 'http://127.0.0.1:5000/users/add_user'

    # JSON данные, которые вы хотите отправить
    data = {
        'user_name': user_name,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_queue_image(queue_identifier):
    url = 'http://127.0.0.1:5000/queues/get_queue_image'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)


#add_user_to_queue("339999194338", "456654289987")
#get_queue("385882291518")
#delete_user_from_queue("339999194338", "456654289987")
#add_queue("test", "456654289987")
#add_user("John221")
#add_queue("test123", "367154949266")
#add_user_to_queue("385882291512", "707862719213")
#add_user_to_queue("507223812912", "456654289980")
#add_user_to_queue("507223812912", "456654289110")
get_queue_image("850409622132")