from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    
    f = open("/tmp/data", "w")
    f.write(request.data.decode("utf-8"))
    f.close()

    return 'Hello, World!'


