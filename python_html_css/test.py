import base64
from flask import Flask, request
from markupsafe import escape

x = base64.b64encode(b'haron murumba')
print(x)

app = Flask(__name__)
@app.route('/')
def hello():
    name = request.args.get("name", "world")
    return f'Hello, {escape(name)}!'