import requests
import json



def create_queue():
    global url, data
    url = 'http://127.0.0.1:5000/queues/add_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'description': 'test queue',
        'creator_id': '123123123123',
    }

def add_user():
    global url, data
    url = 'http://127.0.0.1:5000/queues/add_user_to_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': '339999194338',
        'user_id': '123123123123',
    }

def get_queue():
    global url, data
    url = 'http://127.0.0.1:5000/queues/get_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': '339999194338',
    }
def delete_user():
    global url, data
    url = 'http://127.0.0.1:5000/queues/delete_user_from_queue'

    # JSON данные, которые вы хотите отправить
    data = {
        'queue_identifier': '339999194338',
        'user_id': '123123123121',
    }
delete_user()
# Преобразование данных в формат JSON
json_data = json.dumps(data)

# Отправка POST запроса с JSON данными
response = requests.post(url, json=json_data)

# Печать ответа сервера
print(response.text)
