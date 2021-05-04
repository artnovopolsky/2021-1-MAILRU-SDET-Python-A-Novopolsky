import os
import argparse
import json
from collections import Counter
from fnmatch import fnmatch

LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'access.log'))
RES_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'results', 'python_results.txt'))
RES_FILE_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'results', 'python_results.json'))
JSON_DATA = {}

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true', help='Вывод результатов в формате json.')


# Задание 1
def count_requests(jsonify):
    with open(LOG_FILE, 'r') as log:
        all_requests_count = len(log.readlines())

    if jsonify is True:
        JSON_DATA.setdefault('All_requests_count', all_requests_count)
        json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)

    elif jsonify is False:
        with open(RES_FILE, 'w') as res:
            res.writelines(['Общее количество запросов:\n', str(all_requests_count), '\n'])


# Задание 2
def count_request_types(jsonify):
    with open(LOG_FILE, 'r') as log:
        req_type_column = [req.split()[5][1:] for req in log.readlines()]
        req_types = Counter(req_type_column).most_common()

    if jsonify is True:
        count_req_types = {req[0]: req[1] for req in req_types}
        JSON_DATA.setdefault('Number_of_requests_by_type', count_req_types)
        json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)

    elif jsonify is False:
        with open(RES_FILE, 'a') as res:
            res.write('\nОбщее количество запросов по типу:\n')
            res.writelines([f'{req[1]} - {req[0]}\n' for req in req_types])


# Задание 3
def most_frequent_requests(jsonify):
    with open(LOG_FILE, 'r') as log:
        url_column = [req.split()[6] for req in log.readlines()]
        freq_requests = Counter(url_column).most_common(10)

    if jsonify is True:
        most_freq_reqs = {i+1: {'URL': req[0], 'Number_of_requests': req[1]}
                          for i, req in zip(range(len(freq_requests)), freq_requests)}
        JSON_DATA.setdefault('Top_10_most_frequent_requests', most_freq_reqs)
        json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)

    elif jsonify is False:
        with open(RES_FILE, 'a') as res:
            res.write('\nТоп-10 самых частых запросов:\n')
            res.writelines([f'URL: {req[0]} - Число запросов: {req[1]}.\n' for req in freq_requests])


# Задание 4
def largest_4xx_requests(jsonify):
    with open(LOG_FILE, 'r') as log:
        url_code_size_ip_columns = [(req.split()[6], int(req.split()[8]), int(req.split()[9]), req.split()[0])
                                    for req in log.readlines() if fnmatch(req.split()[8], '4??')]
        url_code_size_ip_columns.sort(key=lambda req: req[2], reverse=True)

    if jsonify is True:
        largest_reqs = {i+1: {'URL': req[0], 'Response_code': req[1], 'Size': req[2], 'IP': req[3]}
                        for i, req in zip(range(len(url_code_size_ip_columns)), url_code_size_ip_columns[:5])}
        JSON_DATA.setdefault('Top_5_largest_requests_with_4xx_response_codes', largest_reqs)
        json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)

    elif jsonify is False:
        with open(RES_FILE, 'a') as res:
            res.write('\nТоп-5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n')
            res.writelines([f'URL: {req[0]} - Статус: {req[1]} - Размер: {req[2]} - IP: {req[3]}.\n'
                            for req in url_code_size_ip_columns[:5]])


# Задание 5
def users_with_5xx_requests(jsonify):
    with open(LOG_FILE, 'r') as log:
        ip_with_5xx = [req.split()[0] for req in log.readlines() if fnmatch(req.split()[8], '5??')]
        freq_ip = Counter(ip_with_5xx).most_common(5)

    if jsonify is True:
        users_with_5xx = {i+1: {'IP': ip[0], 'Number_of_requests': ip[1]}
                          for i, ip in zip(range(len(freq_ip)), freq_ip)}
        JSON_DATA.setdefault('Top_5_users_by_the_requests_with_5xx_response_codes', users_with_5xx)
        json.dump(JSON_DATA, open(RES_FILE_JSON, 'w'), indent=4)

    elif jsonify is False:
        with open(RES_FILE, 'a') as res:
            res.write('\nТоп-5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n')
            res.writelines([f'IP-адрес: {ip[0]}. Кол-во запросов: {ip[1]}\n' for ip in freq_ip])


args = parser.parse_args()

count_requests(jsonify=args.json)
count_request_types(jsonify=args.json)
most_frequent_requests(jsonify=args.json)
largest_4xx_requests(jsonify=args.json)
users_with_5xx_requests(jsonify=args.json)
