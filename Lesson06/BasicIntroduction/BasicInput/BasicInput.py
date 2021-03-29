from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('BasicInput.html')


@app.route('/action_page')
def action_page():
    args = request.args
    data = args.to_dict()
    print(f"form args:")
    for key, val in data.items():
        print(f'\t{key}: {val}')
    return jsonify(data)


if __name__ == '__main__':
    print(f"start serving Site")
    app.run()

