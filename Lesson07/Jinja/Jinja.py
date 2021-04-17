import os
import socket
import logging
import threading, webbrowser
from flask import Flask, request, render_template, jsonify, send_from_directory


app = Flask(__name__)


class Main(object):
    @classmethod
    def start_work(cls):
        # start browser
        host_name = socket.gethostname()
        real_ip = socket.gethostbyname(host_name)
        port = 25347
        url = f"http://{real_ip}:{port}"
        threading.Timer(1.25, lambda: webbrowser.open(url)).start()
        print(f"start serving jinja at {url}")
        logging.getLogger("werkzeug").setLevel(logging.ERROR)
        app.run(host=real_ip, port=port)

    @staticmethod
    def calc_rerun(days_count, couple_id, project_id):
        print(f'rerun with days:{days_count} couple_id:{couple_id},'
              f' project_id:{project_id}')


@app.route('/')
def index():
    project_names = [
        'Natania', 'Tel Aviv', 'Jerusalem', 'Modiin', 'Alfe Menashe',
        'Kfar Saba', 'Raanana']
    projects = [{'id': project_id, 'name': project_name}
                for project_id, project_name in enumerate(project_names)]
    return render_template('index.html', projects=projects)


@app.route('/rerun', methods=['GET'])
def rerun():
    arg_names = ['project_id', 'couple_id', 'days_count', 'Project_Couple']
    inputs = {arg_name: int(request.args.get(arg_name)) for arg_name in arg_names}
    inputs['is_project'] = True if inputs['Project_Couple'] == 0 else False
    # calculate
    print(f'rerun with {inputs}')
    Main.calc_rerun(inputs['days_count'], inputs['couple_id'], inputs['project_id'])
    return jsonify("OK")


@app.route('/version', methods=['GET'])
def get_version():
    return f'Jinja version 1.10'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    # global flask_app
    main_object = Main()
    main_object.start_work()


