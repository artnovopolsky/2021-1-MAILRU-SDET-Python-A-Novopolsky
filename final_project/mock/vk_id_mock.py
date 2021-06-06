import json
from flask import Flask

users = {'artnovopolsky': 12345}

vk_id_mock = Flask(__name__)


@vk_id_mock.route('/vk_id/<username>', methods=['GET'])
def vk_id(username):
    if username in users.keys():
        return json.dumps({'vk_id': users[username]}), 200
    else:
        return json.dumps({}), 404


if __name__ == '__main__':
    vk_id_mock.run(host='0.0.0.0', port=9000)
