import socket
from flask import Flask, render_template, request, jsonify
import json
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['GET', 'POST'])
def action_page_get():
    length = 10000
    base_time = np.linspace(0.0, 5.0 * 2.0 * np.pi, length)
    noise = np.random.random(length)
    signal = np.round(10.0 * (np.sin(base_time) + 0.3 * noise))
    result = {'graph_data': signal.tolist()}
    return jsonify(result)


if __name__ == '__main__':
    print(f"start serving Site")
    # host_name = socket.gethostname()
    # real_ip = socket.gethostbyname(host_name)
    # port = 25347
    # url = f"http://{real_ip}:{port}"
    # start browser
    # threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    # print(f"start serving PurchaseList on url: {url}")
    # app.run(host=real_ip, port=port)
    app.run()

