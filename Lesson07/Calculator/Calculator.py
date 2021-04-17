from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_result', methods=['GET', 'POST'])
def action_page_get():
    data = {}
    if request.method == 'GET':
        args = request.args
        data = args.to_dict()
    elif request.method == 'POST':
        res = request.get_data()
        data = json.loads(res)
    print(f"args:")
    for key, val in data.items():
        print(f'\t{key}: {val}')
    result = {f'result': int(data['x']) * int(data['y'])}
    return jsonify(result)


if __name__ == '__main__':
    print(f"start serving Site")
    app.run()

