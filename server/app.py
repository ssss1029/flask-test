
from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return "Hello World!"

@app.route('/pingPayload', methods=["GET"])
def pingPayload():
    payload = request.data
    ret = int(payload) + 1
    return { "newPayload" : ret }

NUMBER_UPLOAD_FNAME = "number_upload.txt"

@app.route('/filePingPayload', methods=["POST"])
def filePingPayload():

    uploaded_file = request.files[NUMBER_UPLOAD_FNAME]
    uploaded_file.save(NUMBER_UPLOAD_FNAME)

    with open(NUMBER_UPLOAD_FNAME, "r") as fp:
        number = int(fp.readline())
    
    print("Server recieved file upload with contents: {0}".format(number))

    with open(NUMBER_UPLOAD_FNAME, "w") as fp:
        fp.write(str(number + 1))

    return send_file(NUMBER_UPLOAD_FNAME)

if __name__ == '__main__':
    app.run()
