
import requests
import json
import time

"""
Play ping-pong with the server:
 - Send the server the current_payload, and get a new payload back
 - Set the current_payload to the new payload we just got from the server
 - Wait for some time

Repeat^ in a loop
"""

SERVER_HOST = "http://localhost:5000/"
PINGPONG_URL = SERVER_HOST + "pingPayload"

current_payload = 1

while True:
    ret = requests.get(PINGPONG_URL, data=str(current_payload)).json()
    print("Response from server: {0}".format(str(ret)))
    current_payload = ret["newPayload"]
    time.sleep(0.5)
