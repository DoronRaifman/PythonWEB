import os
import socket
import warnings
from flask import Flask, request, render_template, jsonify, send_from_directory

from Lesson08.Core.Enums import SoftwareVersion
from Lesson08.Core.LogHelper import configure_log
from Lesson08.Worker import Worker


app = Flask(__name__)


class Main:
    logger = None
    worker = Worker()

    @classmethod
    def start_work(cls):
        cls.logger = configure_log(name='default', logger_name='default')
        warnings.simplefilter("ignore")
        Main.worker.connect()
        host_name = socket.gethostname()
        real_ip = socket.gethostbyname(host_name)
        # real_ip = "127.0.0.1"
        port = 25347
        url = f"http://{real_ip}:{port}"
        # start browser
        # threading.Timer(1.25, lambda: webbrowser.open(url)).start()
        cls.logger.debug(f"start serving PurchaseList on url: {url}")
        app.run(host=real_ip, port=port)
        # app.run()
        # app.run(host=ip, port=port, debug=False)
        # app.run(port=port)
        Main.worker.disconnect()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login')
def login_data():
    user_name = request.args.get('user_name')
    records = Main.worker.find_user_by_name(user_name)
    if len(records) == 0:
        res = {'user_id': 0, 'user_name': '---'}
    else:
        res = records[0]
    return jsonify(res)


@app.route('/get_data')
def get_data():
    papa_id = request.args.get('papa_id')
    if papa_id is None:
        papa_id = 0
    papa_id = int(papa_id)
    user_id = int(request.args.get('user_id'))
    records = Main.worker.find_user_by_id(user_id)
    user_name = records[0]['user_name']
    items = Main.worker.get_item_siblings(user_id, papa_id)
    if papa_id != 0:
        papa = Main.worker.find_item_by_id(user_id, papa_id)
    else:
        papa = {'id': 0, 'item_name': 'Top Level', 'papa_id': 0}
    return render_template(
        'items.html', papa=papa, items=items, user_id=user_id,
        user_name=user_name, version=SoftwareVersion.version_name)


@app.route('/version', methods=['GET'])
def get_version():
    return f"<h3>{SoftwareVersion.version_name}</h3>"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    Main.start_work()




