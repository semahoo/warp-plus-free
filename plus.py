import json
import requests
import time
import random
import string
import os
from nacl.bindings import crypto_scalarmult_base
from base64 import b64encode
import datetime

# insert your desired GB
_YourGB = 1000000
# insert your Device ID something like this
_yourID = "8b05adf7-82a7-41a8-9b50-6133222a3a74"
key=None
def generate_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
def generate_key():
        private_key = os.urandom(32)
        public_key = crypto_scalarmult_base(private_key)
        return b64encode(private_key).decode('utf-8'), b64encode(public_key).decode('utf-8')


def handle():
        return requests.post(url, headers=headers, data=json.dumps({"referrer": _yourID}))


for i in range(_YourGB):
    url = 'https://api.cloudflareclient.com/v0a745/reg'
    headers = {'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'}
    install_id = generate_string(11)
    #key = key if key else generate_key()
    key=generate_key()
    data = {"key": key[1],
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, generate_string(134)),
            "referrer": _yourID,
            "warp_enabled": True,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "en-GB"}


    
    _res = handle()
    _json_res = _res.json()
    print("You got {}GB data!!".format(i+1))
    if (i+1)%2 == 0:
        time.sleep(60)

