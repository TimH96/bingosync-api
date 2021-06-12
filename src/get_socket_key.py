import requests
import json
from sys import argv

out : dict
try:
    res : requests.Response = requests.post(
        argv[1],
        data=json.dumps({
            'room': argv[2],
            'nickname': argv[3],
            'password': argv[4]
        }))
    out = res.json()
    out['session_id'] = res.request.headers['Cookie'].split('=')[1]
except Exception as error:
    out = {'error': error}
print(out)
