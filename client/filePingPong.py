

import json
import requests
import shutil
import time
import pdb

"""
Play ping-pong with the server:
 - Send the server the current_payload, and get a new payload back
 - Set the current_payload to the new payload we just got from the server
 - Wait for some time

Repeat^ in a loop
"""

SERVER_HOST  = "http://localhost:5000/"
PINGPONG_URL = SERVER_HOST + "filePingPayload"
NUMBER_FILE  = "number.txt"

def main():
    
    while True:
        ping_file()

        # Check what the file currently contains
        with open(NUMBER_FILE, "r") as f:
            print("{0} currently contains: {1}".format(NUMBER_FILE, f.readline()))

        time.sleep(0.5)

def ping_file():
    read_fd = open(NUMBER_FILE, "rb")
    r = requests.post(PINGPONG_URL, stream=True, files={
        "number_upload.txt": read_fd
    })
    read_fd.close()

    with open(NUMBER_FILE, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

if __name__ == "__main__":
    main()