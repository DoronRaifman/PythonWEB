import socket
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    host_name = socket.gethostname()
    real_ip = socket.gethostbyname(host_name)
    port = 10000
    url = f"http://{real_ip}:{port}"
    print(f"start serving Site on url: {url}")
    app.run(host=real_ip, port=port)

