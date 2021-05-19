import threading
import json
import requests
from flask import Flask, jsonify, request
from requests.exceptions import ConnectionError

APP_DATA = {
    'Artyom': 19,
    'Danila': 12,
    'Mark': 20
}

RUN_MOCK_RETRY = 10

app = Flask(__name__)


@app.route('/create_user', methods=['POST'])
def create_user():
    name = json.loads(request.data)['name']
    age = json.loads(request.data)['age']

    if APP_DATA.get(name) is None:
        APP_DATA[name] = age
        data = {'name': name, 'age': age}
        return jsonify(data), 201
    else:
        return jsonify(f'User with name {name} already exists.'), 400


@app.route('/get_age/<name>', methods=['GET'])
def get_user_age(name):
    if age := APP_DATA.get(name):
        data = {'name': name, 'age': age}
        return jsonify(data), 200
    else:
        return jsonify(f'Age not found because user {name} does not exist.'), 404


@app.route('/change_age', methods=['PUT'])
def change_user_age():
    name = json.loads(request.data)['name']
    if APP_DATA.get(name) is not None:
        new_age = json.loads(request.data)['new_age']
        APP_DATA[name] = new_age
        data = {'name': name, 'age': new_age}
        return jsonify(data), 201
    else:
        return jsonify(f'Age cannot be changed as the user {name} does not exist.'), 404


@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    name = json.loads(request.data)['name']
    if APP_DATA.get(name) is not None:
        APP_DATA.pop(name)
        return jsonify(f'User {name} was deleted successfully!'), 200
    else:
        return jsonify(f'User {name} cannot be deleted because he does not exist.'), 404


def run_mock(host='127.0.0.1', port=8888):
    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })
    server.start()

    for i in range(RUN_MOCK_RETRY):
        try:
            requests.get(f'http://{host}:{port}')
            break
        except ConnectionError:
            if i == RUN_MOCK_RETRY - 1:
                raise

    return server


@app.route('/shutdown')
def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()
    return jsonify(f'Exit done successfully. Bye!'), 200
