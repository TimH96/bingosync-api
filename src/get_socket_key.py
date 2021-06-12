import requests
import json
from sys import argv

out : dict
try:
    res : requests.Response = requests.post(
        'https://bingosync.com/api/join-room',
        data=json.dumps({
            'room': argv[1],
            'nickname': argv[2],
            'password': argv[3]
        }))
    out = res.json()
    out['session_id'] = res.request.headers['Cookie'].split('=')[1]
except Exception as error:
    out = {'error': error}
print(out)
