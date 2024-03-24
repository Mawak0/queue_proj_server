import sqlite3
import traceback
import other_tools


db_path = 'queue_proj_database.db'


def db_action_write(clause, props=None):
    with sqlite3.connect(db_path, timeout=99999999999999999999) as connect:
        cursor = connect.cursor()
        if props != None:
            cursor.execute(clause, props)
        else:
            cursor.execute(clause)

def db_action_read(clause, props=None):
    with sqlite3.connect(db_path, timeout=99999999999999999999) as connect:
        cursor = connect.cursor()
        if props != None:
            cursor.execute(clause, props)
        else:
            cursor.execute(clause)
        result = cursor.fetchall()
        return result

def init_create_tables():
    db_action_write('''CREATE TABLE IF NOT EXISTS queues (identifier TEXT, description TEXT, creator_id TEXT)''')
    db_action_write('''CREATE TABLE IF NOT EXISTS users (user_id TEXT, user_name TEXT, reputation INT)''')

init_create_tables()


def is_user_exist(user_id):
    assert other_tools.validate_id(user_id)
    user = db_action_read("SELECT * FROM users WHERE user_id=?", [user_id])
    if len(user) == 0:
        return False
    return True

def is_queue_exist(identifier):
    assert other_tools.validate_id(identifier)
    queue = db_action_read("SELECT * FROM queues WHERE identifier=?", [identifier])
    if len(queue) == 0:
        return False
    return True

def add_new_user(name):
    new_user_id = other_tools.generate_id()
    db_action_write("INSERT INTO users (user_id, user_name, reputation) VALUES (?, ?, ?)", ([new_user_id, name, 0]))
    return new_user_id

def get_all_users():
    return db_action_read("SELECT * FROM users")


def add_new_queue(description, creator_id):
    new_queue_id = other_tools.generate_id()
    db_action_write("INSERT INTO queues (identifier, description, creator_id) VALUES (?, ?, ?)", ([new_queue_id, description, creator_id]))
    db_action_write(
        '''CREATE TABLE queue_'''+new_queue_id+''' (user_id TEXT, position INT, adding_time TEXT)''')
    return new_queue_id

def refresh_users_positions_in_queue(queue_identifier):
    assert other_tools.validate_id(queue_identifier)
    queue_dump = db_action_read("SELECT * FROM queue_"+queue_identifier+"")
    sorted_dump = sorted(queue_dump, key=lambda x: float(x[2]))
    for i in range(0, len(sorted_dump)):
        if sorted_dump[i][1] != i:
            current_id = sorted_dump[i][0]
            db_action_write("UPDATE queue_" + queue_identifier + " SET position=? WHERE user_id=?", [i, current_id])

def add_user_to_queue(queue_identifier, user_id, adding_time):
    assert other_tools.validate_id(queue_identifier)
    assert other_tools.validate_id(user_id)
    position = len(db_action_read("SELECT * FROM queue_"+queue_identifier))
    db_action_write("INSERT INTO queue_"+queue_identifier+" (user_id, position, adding_time) VALUES (?, ?, ?)", ([user_id, position, adding_time]))


def delete_user_from_queue(queue_identifier, user_id):
    assert other_tools.validate_id(queue_identifier)
    assert other_tools.validate_id(user_id)
    db_action_write("DELETE FROM queue_"+queue_identifier+" WHERE user_id=?", [user_id])
    refresh_users_positions_in_queue(queue_identifier)

def get_queue(queue_identifier):
    assert other_tools.validate_id(queue_identifier)
    rows = db_action_read("SELECT * FROM queue_"+queue_identifier+"")
    out = []
    for r in rows:
        out.append(dict())
        out[-1]['user_id'] = r[0]
        out[-1]['position'] = r[1]
        out[-1]['adding_time'] = r[2]
    return out

def get_user_name(user_id):
    assert other_tools.validate_id(user_id)
    name = db_action_read("SELECT user_name FROM users WHERE user_id=?", [user_id])[0][0]
    return name