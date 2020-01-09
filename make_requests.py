
import requests
import json
import time

SERVER_HOST = "http://localhost:5000/"

current_payload = 1

while True:
    ret = requests.get(SERVER_HOST + "pingPayload", data=str(current_payload))
    ret = ret.json()
    print("Response from server: {0}".format(str(ret)))
    current_payload = ret["newPayload"]
    time.sleep(0.5)
