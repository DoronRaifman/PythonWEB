import socket
from flask import Flask, render_template

app = Flask(__name__)


def start_work():
    host_name = socket.gethostname()
    real_ip = socket.gethostbyname(host_name)
    # real_ip = "127.0.0.1"
    port = 10000
    url = f"http://{real_ip}:{port}"
    print(f"start serving recalc on url: {url}")
    app.run(host=real_ip, port=port)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    start_work()

