from flask import Flask

app = Flask(__name__)

@app.route("/")#@는 데코레이터 
def hello():
    return "<h1>Hello World<h1>"
