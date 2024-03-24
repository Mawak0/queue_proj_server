
import traceback
from flask import Flask, jsonify, request, render_template, Response
from pydantic import BaseModel, EmailStr, ValidationError
from enum import Enum
from typing import Union, Optional, List
import os
import json
import db_tools
import time

import other_tools


app = Flask("queue_proj_server")

possible_reply_statuses = ["done", "fail", "error: user_not_in_queue", "error: user_already_in_queue",
                           "error: user_does_not_exist"]

def reply_json_former(status, data={}):
    assert (status in possible_reply_statuses)
    return json.dumps({'status': status, 'data': data})


@app.route('/queues/get_queue', methods=['POST'])
def get_queue():
    try:
        request_json = json.loads(request.json)
        data = db_tools.get_queue(request_json['queue_identifier'])
        for i in range(0, len(data)):
            username = db_tools.get_user_name(data[i]['user_id'])
            data[i]['user_id'] = other_tools.empty_id
            data[i]['user_name'] = username
        return reply_json_former('done', data)
    except Exception as e:
        traceback.print_exc()
        return reply_json_former("fail")

@app.route('/queues/add_queue', methods=['POST'])
def add_queue():
    try:
        request_json = json.loads(request.json)
        new_queue_id = db_tools.add_new_queue(request_json['description'], request_json['creator_id'])
        return reply_json_former("done", {"new_queue_id": new_queue_id})
    except Exception as e:
        traceback.print_exc()
        return reply_json_former("fail")

@app.route('/queues/add_user_to_queue', methods=['POST'])
def add_user_to_queue():
    try:
        request_json = json.loads(request.json)
        if not db_tools.is_user_exist(request_json['user_id']):
            return reply_json_former('error: user_does_not_exist')
        if request_json['user_id'] in other_tools.get_users_in_queue(db_tools.get_queue(request_json['queue_identifier'])):
            return reply_json_former('error: user_already_in_queue')
        db_tools.add_user_to_queue(request_json['queue_identifier'], request_json['user_id'], str(time.time()))
        return reply_json_former('done')
    except Exception as e:
        traceback.print_exc()
        return reply_json_former('fail')

@app.route('/queues/delete_user_from_queue', methods=['POST'])
def delete_user_from_queue():
    try:
        request_json = json.loads(request.json)
        if request_json['user_id'] not in other_tools.get_users_in_queue(db_tools.get_queue(request_json['queue_identifier'])):
            return reply_json_former('error: user_not_in_queue')
        db_tools.delete_user_from_queue(request_json['queue_identifier'], request_json['user_id'])
        return reply_json_former('done')
    except Exception as e:
        traceback.print_exc()
        return reply_json_former('fail')

@app.route('/users/add_user', methods=['POST'])
def add_user():
    try:
        request_json = json.loads(request.json)
        new_user_id = db_tools.add_new_user(request_json['user_name'])
        return reply_json_former('done', {"user_id": new_user_id})
    except Exception as e:
        traceback.print_exc()
        return reply_json_former('fail')

if __name__ == '__main__':
    app.run()