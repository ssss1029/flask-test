
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/pingPayload')
def pingPayload():
    payload = request.data
    ret = int(payload) + 1
    return { "newPayload" : ret }

if __name__ == '__main__':
    app.run()
