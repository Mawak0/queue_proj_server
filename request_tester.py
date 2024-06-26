import requests
import json


#server = "doujinshiradio.ru:5000"
server = "127.0.0.1:5000"
def add_queue(description, creator_id):
    url = 'http://'+server+'/queues/add_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'description': description,
        'creator_id': creator_id,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def add_user_to_queue(queue_identifier, user_id):
    url = 'http://'+server+'/queues/add_user_to_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier,
        'user_id': user_id,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_queue(queue_identifier):
    url = 'http://'+server+'/queues/get_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)
def delete_user_from_queue(queue_identifier, user_id):
    url = 'http://'+server+'/queues/delete_user_from_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier,
        'user_id': user_id,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def add_user(user_name):
    url = 'http://'+server+'/users/add_user'

    # JSON данные, которые вы хотите отправить
    data = {
        'user_name': user_name,
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_queue_image(queue_identifier):
    url = 'http://'+server+'/queues/get_queue_image'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_identifier
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_current_user_queues(user_id):
    url = 'http://doujinshiradio.ru:5000/users/get_current_user_queues'

    # JSON данные, которые вы хотите отправить
    data = {
        'user_id': user_id
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_user_position_in_queue(user_id, queue_id):
    url = 'http://'+server+'/queues/get_user_position_in_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'user_id': user_id,
        'queue_identifier': queue_id
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

def get_queue_description(queue_id):
    url = 'http://'+server+'/queues/get_queue_description'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': queue_id
    }
    json_data = json.dumps(data)
    response = requests.post(url, json=json_data)
    print(response.text)

#add_user_to_queue("339999194338", "456654289987")
#get_queue("385882291518")
#delete_user_from_queue("339999194338", "456654289987")
#add_queue("test", "456654289987")
#add_user("Test456")
#368955605705
#add_queue("test_queue123", "368955605705")
#637375079065
#add_user_to_queue("385882291512", "707862719213")
#add_user_to_queue("507223812912", "456654289980")
#delete_user_from_queue("339106682759", "453415766387")
#add_user_to_queue("339106682759", "453415766387")
#get_current_user_queues("453415766387")
get_queue_description("637375079065")
#get_user_position_in_queue("453415766387", "339106682759")
#get_queue_image("850409622132")