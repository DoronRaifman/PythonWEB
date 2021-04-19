from flask import Flask, render_template, request, jsonify
import json
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['GET', 'POST'])
def action_page_get():
    length = 1000
    base_time = np.linspace(0.0, 5.0 * 2.0 * np.pi, length)
    noise = np.random.random(length)
    signal = np.round(10.0 * (np.sin(base_time) + 0.3 * noise))
    result = {'graph_data': signal.tolist()}
    return jsonify(result)


if __name__ == '__main__':
    print(f"start serving Site")
    app.run()

