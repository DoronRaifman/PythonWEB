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
    cur_papa = 0

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
def index():
    papa_id = request.args.get('papa_id')
    if papa_id is None:
        papa_id = 0
    Main.cur_papa = int(papa_id)
    items_list = Main.worker.get_item_siblings(papa_id=Main.cur_papa)
    items = Main.worker.item_list_to_dict_list(items_list)
    if Main.cur_papa != 0:
        papa_item = Main.worker.find_item_by_id(Main.cur_papa)
        papa_dict_list = Main.worker.item_list_to_dict_list([papa_item])
        papa = papa_dict_list[0]
    else:
        papa = {'id': 0, 'item_name': 'Top Level', 'papa_id': 0}
    return render_template('index.html', papa=papa, items=items)


@app.route('/version', methods=['GET'])
def get_version():
    return f"<h3> {SoftwareVersion.version_name}</h3>"


@app.route('/goto', methods=['GET'])
def goto():
    item_id = int(request.args.get('item_id'))
    Main.cur_papa = item_id
    Main.logger.debug(f'goto {item_id}')
    return jsonify("OK")


@app.route('/get_item', methods=['GET'])
def get_item():
    item_id = int(request.args.get('item_id'))
    item = Main.worker.find_item_by_id(item_id)
    Main.logger.debug(f'goup to {item.id}, {item.item_name}')
    item_dict_list = Main.worker.item_list_to_dict_list([item])
    return jsonify(item_dict_list[0])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    Main.start_work()




