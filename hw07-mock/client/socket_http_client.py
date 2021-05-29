import os
import socket
import json

CONNECT_RETRY = 10


class SocketClient:

    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self.log_file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'requests.log'))

        with open(self.log_file, 'w') as log:  # Recreate log file
            pass

    def _connect(self):
        connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect.settimeout(0.1)

        for i in range(CONNECT_RETRY):
            try:
                connect.connect((self.host, self.port))
                return connect
            except ConnectionRefusedError:
                if i == CONNECT_RETRY - 1:
                    raise

    def log_response(self, data):
        status_code = data[0].split(' ')[1]
        headers = data[1:-2]
        body = data[-1]
        with open(self.log_file, 'a') as log:
            log.write('STATUS_CODE:\n\t' + status_code + '\n')
            log.write('HEADERS:\n')
            for header in headers:
                log.write('\t' + header + '\n')
            log.write('RESPONSE_BODY:\n\t' + body + '\n\n')

    def handle_response(self, connect):
        total_data = []
        while True:
            data = connect.recv(8192)
            if data:
                total_data.append(data.decode())
            else:
                connect.close()
                break

        data = ''.join(total_data).splitlines()
        self.log_response(data)

        return {'status_code': int(data[0].split(' ')[1]), 'body': data[-1]}

    def to_json(self, dictionary):
        return json.dumps(dictionary, indent=4)

    def get(self, url):
        connect_get = self._connect()

        request = f'GET {url} HTTP/1.1\r\n' \
                  f'Host:{self.host}\r\n\r\n'

        for i in range(CONNECT_RETRY):
            try:
                connect_get.send(request.encode())
                return self.handle_response(connect_get)
            except BrokenPipeError:
                if i == CONNECT_RETRY - 1:
                    raise

    def post(self, url, data):
        connect_post = self._connect()
        json_data = self.to_json(data)

        content_type = 'Content-Type: application/json'
        content_length = 'Content-Length: ' + str(len(json_data))
        request = f'POST {url} HTTP/1.1\r\n' \
                  f'Host: {self.host}\r\n' \
                  f'{content_type}\r\n' \
                  f'{content_length}\r\n\r\n' \
                  + json_data

        connect_post.send(request.encode())

        return self.handle_response(connect_post)

    def put(self, url, data):
        connect_put = self._connect()
        json_data = self.to_json(data)

        content_type = 'Content-Type: application/json'
        content_length = 'Content-Length:' + str(len(json_data))
        request = f'PUT {url} HTTP/1.1\r\n' \
                  f'Host:{self.host}\r\n' \
                  f'{content_type}\r\n' \
                  f'{content_length}\r\n\r\n' \
                  + json_data

        connect_put.send(request.encode())

        return self.handle_response(connect_put)

    def delete(self, url, data):
        connect_delete = self._connect()
        json_data = self.to_json(data)

        content_type = 'Content-Type: application/json'
        content_length = 'Content-Length:' + str(len(json_data))
        request = f'DELETE {url} HTTP/1.1\r\n' \
                  f'Host: {self.host}\r\n' \
                  f'{content_type}\r\n' \
                  f'{content_length}\r\n\r\n' \
                  + json_data

        connect_delete.send(request.encode())

        return self.handle_response(connect_delete)
