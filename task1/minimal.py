from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
 
@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "<h1>Hello, world!<br>UTC Time: {}<br>User Agent: {}</h1>".format(dt, user_agent)
 
if __name__ == "__main__":
    app.run()