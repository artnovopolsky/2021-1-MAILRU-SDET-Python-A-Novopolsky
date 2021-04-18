import json
import requests
from urllib.parse import urljoin


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url, email, password):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.session = requests.Session()
        self.csrf_token = None

    def _request(self, method, location, headers=None, data=None, expected_status=200):
        url = urljoin(self.base_url, location)
        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.')
        return response

    def _get_csrf_token(self):
        location = '/csrf/'
        self._request('GET', location)
        return self.session.cookies['csrftoken']

    def post_login(self):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.email,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        result = self._request('POST', location, headers=headers, data=data)
        self.csrf_token = self._get_csrf_token()

        return result

    def post_campaign_create(self, name='test_campaign'):
        location = '/api/v2/campaigns.json'

        headers = {
            'X-CSRFToken': self._get_csrf_token()
        }

        data = json.dumps({
            'name': name,
            'objective': 'reach',
            'package_id': 960,
            'banners': [{
                'urls': {
                    'primary': {
                        'id': 47177248
                    }
                },
                'textblocks': {},
                'content': {
                    'image_240x400': {
                        'id': 8678796
                    }
                },
                'name': ''}
            ]
        })

        response = self._request('POST', location, headers=headers, data=data)
        return response.json()['id']

    def get_campaign(self, campaign_id):
        location = f'/api/v2/campaigns/{campaign_id}.json'
        self._request('GET', location)

    def post_campaign_delete(self, campaign_id):
        location = f'/api/v2/campaigns/{campaign_id}.json'

        headers = {
            'X-CSRFToken': self._get_csrf_token()
        }

        data = json.dumps({
            'status': 'deleted'
        })

        self._request('POST', location, headers=headers, data=data, expected_status=204)

    def post_segment_create(self, name='test_segment'):
        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,' \
                   'relations__object_id,relations__params,relations_count,id,name,' \
                   'pass_condition,created,campaign_ids,users,flags'

        headers = {
            'X-CSRFToken': self._get_csrf_token()
        }

        data = json.dumps({
            "logicType": "or",
            "name": name,
            "pass_condition": 1,
            "relations": [{
                "object_type": "remarketing_player",
                "params": {
                    "type": "positive",
                    "left": 365,
                    "right": 0
                }
            }]
        })

        response = self._request('POST', location, headers=headers, data=data)

        return response.json()['id']

    def get_segment(self, segment_id):
        location = f'api/v2/remarketing/segments/{segment_id}' \
                   f'/relations.json?fields=id,params,object_type,object_id&_=1618703524358'

        self._request('GET', location)

    def delete_segment(self, segment_id):
        location = f'api/v2/remarketing/segments/{segment_id}.json'

        headers = {
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self._get_csrf_token()
        }

        self._request('DELETE', location, headers=headers, expected_status=204)
