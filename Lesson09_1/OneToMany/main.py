import json
import os
import socket

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm.attributes import flag_modified

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'Data', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Main:
    @classmethod
    def init(cls):
        cls.start()

    @classmethod
    def cleanup(cls):
        pass

    @classmethod
    def start(cls):
        print(f"start serving Site")
        host_name = socket.gethostname()
        real_ip = socket.gethostbyname(host_name)
        port = 5000
        # real_ip = "127.0.0.1"
        url = f"http://{real_ip}:{port}"
        print(f'start serving server site (1->n) on url: {url}')
        app.run(host=real_ip, port=port)

    @staticmethod
    def get_params():
        data = {}
        if request.method == 'GET':
            args = request.args
            data = args.to_dict()
        elif request.method == 'POST':
            res = request.get_data()
            data = json.loads(res)
        return data

    @classmethod
    def create_empty_db(cls):
        db.drop_all()
        db.create_all()
        print('adding users:')
        users_dict = {
            'doron': {'password': '1234', 'user_role': 'admin'},
            'henry': {'password': '1234', 'user_role': 'admin'},
        }
        for user_name, user_info in users_dict.items():
            user = User(name=user_name, password=user_info['password'], user_role=user_info['user_role'])
            db.session.add(user)
            db.session.commit()
        users_list = User.query.all()
        print(users_list)

    @classmethod
    def create_db(cls):
        db.drop_all()
        db.create_all()
        customer_list = [
            Customer(name='Anger 207', contact='Moshe', contact_phone='054-1234501',
                     contact_email='anger@anger207.com'),
            Customer(name='Leasing', contact='Haim', contact_phone='054-1234502',
                     contact_email='leasing@leasing.com'),
        ]
        for customer in customer_list:
            db.session.add(customer)
        db.session.commit()
        customers = Customer.query.all()
        print(f'customers: {customers}')
        client_dict = {
            'Anger 207': [
                Client(name='Anger 207', contact='david', contact_phone='054-1234513',
                       contact_email='anger_yard@anger207.com'),
            ],
            'Leasing': [
                Client(name='Intel KG', contact='ilanit', contact_phone='054-1234514',
                       contact_email='intel_kg@intel.com'),
                Client(name='Intel Haifa', contact='gal', contact_phone='054-1234515',
                       contact_email='intel_haifa@intel.com'),
            ]
        }
        for customer in customers:
            customer_id = customer.id
            clients = client_dict[customer.name]
            for client in clients:
                client.customer_id = customer_id
                db.session.add(client)
        db.session.commit()
        system_config = {
            'Anger 207': {
                'Anger 207': {
                    'main_yard': {
                        'gateways': [1, 2],
                        'info': {
                            'name': 'main_yard', 'contact': 'sasha', 'contact_phone': '054-1234521',
                            'contact_email': 'main_yard@example.com',
                        }
                    },
                    'back_yard': {
                        'gateways': [3, 4],
                        'info': {
                            'name': 'back yard', 'contact': 'raz', 'contact_phone': '054-1234522',
                            'contact_email': 'back_yard@example.com',
                        }
                    },
                }
            },
            'Leasing': {
                'Intel KG': {
                    'main_yard': {
                        'gateways': [5, 6],
                        'info': {
                            'name': 'main yard', 'contact': 'henry', 'contact_phone': '054-1234523',
                            'contact_email': 'main_yard1@intel.com',
                        }
                    },
                    'back_yard': {
                        'gateways': [7, 8],
                        'info': {
                            'name': 'back yard', 'contact': 'lihi', 'contact_phone': '054-1234524',
                            'contact_email': 'back_yard1@intel.com',
                        }
                    },
                },
                'Intel Haifa': {
                    'main_yard': {
                        'gateways': [9],
                        'info': {
                            'name': 'main yard', 'contact': 'tomer', 'contact_phone': '054-1234525',
                            'contact_email': 'main_yard2@intel.com',
                        }
                    },
                    'back_yard': {
                        'gateways': [10],
                        'info': {
                            'name': 'back yard', 'contact': 'zuzu', 'contact_phone': '054-1234526',
                            'contact_email': 'back_yard2@intel.com',
                        }
                    },
                },
            },
        }
        clients = Client.query.all()
        print(f'clients: {clients}')
        for customer in customers:
            customer_name = customer.name
            for client in customer.clients:
                client_id = client.id
                client_name = client.name
                customer_info = system_config[customer_name]
                sites_info = customer_info[client_name]
                for site_name, site_data in sites_info.items():
                    info = site_data['info']
                    site_record = Site(
                        name=info['name'], contact=info['contact'], contact_phone=info['contact_phone'],
                        contact_email=info['contact_email'], client_id=client_id)
                    db.session.add(site_record)
                    db.session.commit()
                    site_id = site_record.id
                    fork_lift_list = site_data['gateways']
                    for fork_lift_id in fork_lift_list:
                        fork_id_str = f'fork {fork_lift_id}'
                        fork_lift = ForkLift(name=fork_id_str, site_id=site_id)
                        db.session.add(fork_lift)
                    db.session.commit()
        sites = Site.query.all()
        print(f'sites: {sites}')

        fork_lifts_list = ForkLift.query.all()
        print(f'fork_lifts: {fork_lifts_list}')

        print('adding users:')
        users = {
            'doron': {'password': '1234', 'user_role': 'admin'},
            'henry': {'password': '1234', 'user_role': 'admin'},
            'multi': {'password': '1234', 'user_role': 'manager', 'customers': ['Anger 207', 'Leasing']},
            'john': {'password': '1234', 'user_role': 'manager', 'customers': ['Anger 207']},
            'intel': {'password': '1234', 'user_role': 'manager', 'customers': ['Leasing']},
            'moshe': {'password': '1234', 'user_role': 'user', 'customers': ['Anger 207']},
            'haim': {'password': '1234', 'user_role': 'user', 'customers': ['Leasing']},
        }
        customers_dict = {customer.name: customer for customer in customers}
        for user_name, user_info in users.items():
            user = User(name=user_name, password=user_info['password'], user_role=user_info['user_role'])
            db.session.add(user)
            db.session.commit()
            customer_users = user_info['customers'] if 'customers' in user_info else []
            for customer_name in customer_users:
                customer = customers_dict[customer_name]
                # customer_user = CustomerUsers(customer_id=customer.id, user_id=user.id)
                customer.users.append(user)
                db.session.commit()
                # print(f'\tcustomer:{customer.name}: {customer.users}')
        for customer_name, customer in customers_dict.items():
            print(f'\tcustomer:{customer.name}: {customer.users}')
        return customers, clients, sites


CustomerUsers = db.Table('CustomerUsers',
                         db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                         )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    user_role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User "{self.name[:20]}", id={self.id}>'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(30), nullable=False)
    contact_phone = db.Column(db.String(20))
    contact_email = db.Column(db.String(30))

    clients = db.relationship('Client', backref='client')
    users = db.relationship('User', secondary=CustomerUsers, backref='customers')

    def __repr__(self):
        return f'<Customer "{self.name}", id={self.id}>'


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(30), nullable=False)
    contact_phone = db.Column(db.String(20))
    contact_email = db.Column(db.String(30))

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    sites = db.relationship('Site', backref='site')

    def __repr__(self):
        return f'<Client "{self.name}", id={self.id}>'


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(30), nullable=False)
    contact_phone = db.Column(db.String(20))
    contact_email = db.Column(db.String(30))

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    def __repr__(self):
        return f'<Site "{self.name}", id={self.id}>'


class ForkLift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))

    def __repr__(self):
        return f'<ForkLift "{self.name}", id={self.id}, site_id={self.site_id}>'


@app.route('/', methods=['GET'])
def login_form():
    print(f'login_form')
    return render_template('login.html')


@app.route('/login', methods=['GET'])
def login_form_apply():
    data = Main.get_params()
    print(f'login_form_apply. data:{data}')
    user_name, password, remember = data['user_name'], data['password'], data['remember']
    result = {'is_ok': True, 'message': 'OK', 'user_name': user_name, 'user_id': -1}
    user = User.query.filter_by(name=user_name).first()
    if password != user.password:
        print('login error')
        result = {'is_ok': False, 'message': "user name and password doesn't match. Please try again", 'user_id': -1}
    else:
        print(f'login ok with user_id {user.id}')
        result['user_id'] = user.id
        # return redirect(url_for('customers', user_id=user.id, customer_id=None, client_id=None))

    return jsonify(result)


@app.route('/customers/<int:user_id>/')
def customers(user_id):
    customers_list_temp = Customer.query.all()
    user = User.query.filter_by(id=user_id).first()
    inc_customers = {customer.id: None for customer in user.customers}
    if user.user_role == 'admin':
        customers_list = customers_list_temp
    else:
        customers_list = [customer for customer in customers_list_temp if customer.id in inc_customers]
    html = render_template('customers.html', user_id=user_id, user_role=user.user_role,
                           customers=customers_list, customer_id=None, client_id=None)
    return html


@app.route('/customers/<int:user_id>/<int:customer_id>/')
def customers_one(user_id, customer_id):
    user = User.query.filter_by(id=user_id).first()
    customer = Customer.query.get_or_404(customer_id)
    return render_template('customers.html', user_id=user_id, user_role=user.user_role,
                           customers=[customer], customer_id=customer_id, client_id=None)


@app.route('/customers/<int:user_id>/<int:customer_id>/clients/<int:client_id>')
def customers_one_client(user_id, customer_id, client_id):
    user = User.query.filter_by(id=user_id).first()
    customer = Customer.query.get_or_404(customer_id)
    return render_template('customers.html', user_id=user_id, user_role=user.user_role,
                           customers=[customer], customer_id=customer_id, client_id=client_id)


@app.route('/customers/add/<int:user_id>/', methods=('GET', 'POST'))
def customers_add(user_id):
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        contact_phone = request.form['contact_phone']
        contact_email = request.form['contact_email']

        customer = Customer(name=name, contact=contact, contact_phone=contact_phone, contact_email=contact_email)
        db.session.add(customer)
        db.session.commit()

        return redirect(url_for('customers', user_id=user_id, customer_id=customer.id, client_id=None))

    return render_template('customers_add.html', user_id=user_id)


@app.route('/customers/edit/<int:user_id>/<int:customer_id>/', methods=('GET', 'POST'))
def customers_edit(user_id, customer_id):
    if request.method == 'POST':
        customer = Customer.query.get_or_404(customer_id)
        customer.name = request.form['name']
        customer.contact = request.form['contact']
        customer.contact_phone = request.form['contact_phone']
        customer.contact_email = request.form['contact_email']

        db.session.commit()

        return redirect(url_for('customers', user_id=user_id, customer_id=customer.id, client_id=None))

    customer = Customer.query.get_or_404(customer_id)
    return render_template('customers_edit.html', user_id=user_id, customer_id=customer_id, customer=customer)


@app.route('/customers/del/<int:user_id>/<int:customer_id>/', methods=('GET', ))
def customers_del(user_id, customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customers', user_id=user_id, customer_id=customer.id))


@app.route('/clients/add/<int:user_id>/<int:customer_id>/', methods=('GET', 'POST'))
def clients_add(user_id, customer_id):
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        contact_phone = request.form['contact_phone']
        contact_email = request.form['contact_email']

        client = Client(name=name, contact=contact, contact_phone=contact_phone, contact_email=contact_email,
                        customer_id=customer_id)
        db.session.add(client)
        db.session.commit()

        return redirect(url_for('customers_one', user_id=user_id, customer_id=customer_id, client_id=None))

    return render_template('clients_add.html', user_id=user_id)


@app.route('/clients/edit/<int:user_id>/<int:customer_id>/<int:client_id>/', methods=('GET', 'POST'))
def clients_edit(user_id, customer_id, client_id):
    if request.method == 'POST':
        client = Client.query.get_or_404(client_id)
        client.name = request.form['name']
        client.contact = request.form['contact']
        client.contact_phone = request.form['contact_phone']
        client.contact_email = request.form['contact_email']

        db.session.commit()

        return redirect(url_for('customers_one', user_id=user_id, customer_id=customer_id, client_id=None))

    customer = Customer.query.get_or_404(customer_id)
    client = Client.query.get_or_404(client_id)
    return render_template('clients_edit.html', user_id=user_id,
                           customer_id=customer_id, customer=customer, client=client)


@app.route('/clients/del/<int:user_id>/<int:customer_id>/<int:client_id>/', methods=('GET', ))
def clients_del(user_id, customer_id, client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('customers_one', user_id=user_id, customer_id=customer_id, client_id=None))


@app.route('/clients/add/<int:user_id>/<int:customer_id>/<int:client_id>/', methods=('GET', 'POST'))
def sites_add(user_id, customer_id, client_id):
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        contact_phone = request.form['contact_phone']
        contact_email = request.form['contact_email']

        site = Site(name=name, contact=contact, contact_phone=contact_phone, contact_email=contact_email,
                    client_id=client_id)
        db.session.add(site)
        db.session.commit()

        return redirect(url_for('customers_one', user_id=user_id, customer_id=customer_id, client_id=None))

    return render_template('sites_add.html', user_id=user_id)


@app.route('/sites/edit/<int:user_id>/<int:customer_id>/<int:site_id>/', methods=('GET', 'POST'))
def sites_edit(user_id, customer_id, site_id):
    if request.method == 'POST':
        site = Site.query.get_or_404(site_id)
        site.name = request.form['name']
        site.contact = request.form['contact']
        site.contact_phone = request.form['contact_phone']
        site.contact_email = request.form['contact_email']

        db.session.commit()

        return redirect(url_for('customers_one', user_id=user_id, customer_id=customer_id, client_id=None))

    site = Site.query.get_or_404(site_id)
    return render_template('sites_edit.html', user_id=user_id, customer_id=customer_id, site=site)


@app.route('/sites/del/<int:user_id>/<int:customer_id>/<int:site_id>/', methods=('GET', ))
def sites_del(user_id, customer_id, site_id):
    site = Site.query.get_or_404(site_id)
    db.session.delete(site)
    db.session.commit()
    return redirect(url_for('customers_one', user_id=user_id, customer_id=customer_id, client_id=None))


@app.route('/fork_lifts/<int:user_id>/<int:customer_id>/<int:client_id>/<int:site_id>/', methods=('GET', ))
def fork_lifts(user_id, customer_id, client_id, site_id):
    customer = Customer.query.get_or_404(customer_id)
    client = Client.query.get_or_404(client_id)
    site = Site.query.get_or_404(site_id)
    fork_lifts_list = ForkLift.query.filter_by(site_id=site_id).all()
    user = User.query.filter_by(id=user_id).first()
    return render_template('fork_lifts.html', user_id=user_id, user_role=user.user_role,
                           customer=customer, client=client, site=site, fork_lifts=fork_lifts_list)


@app.route('/fork_lifts/add/<int:user_id>/<int:customer_id>/<int:client_id>/<int:site_id>/', methods=('GET', 'POST'))
def fork_lifts_add(user_id, customer_id, client_id, site_id):
    if request.method == 'POST':
        name = request.form['name']

        fork_lift = ForkLift(name=name, site_id=site_id)
        db.session.add(fork_lift)
        db.session.commit()

        return redirect(url_for('fork_lifts', user_id=user_id,
                                customer_id=customer_id, client_id=client_id, site_id=site_id))

    customer = Customer.query.get_or_404(customer_id)
    client = Client.query.get_or_404(client_id)
    site = Site.query.get_or_404(site_id)
    return render_template('fork_lifts_add.html', user_id=user_id, customer=customer, client=client, site=site)


@app.route('/fork_lifts/edit/<int:user_id>/<int:customer_id>/<int:client_id>/<int:site_id>/<int:fork_id>/',
           methods=('GET', 'POST'))
def fork_lifts_edit(user_id, customer_id, client_id, site_id, fork_id):
    if request.method == 'POST':
        fork_lift = ForkLift.query.get_or_404(fork_id)
        fork_lift.name = request.form['name']
        db.session.commit()

        return redirect(url_for('fork_lifts', user_id=user_id,
                                customer_id=customer_id, client_id=client_id, site_id=site_id))

    fork_lift = ForkLift.query.get_or_404(fork_id)
    return render_template('fork_lifts_edit.html', user_id=user_id,
                           customer_id=customer_id, client_id=client_id, site_id=site_id, fork_lift=fork_lift)


@app.route('/fork_lifts/del/<int:user_id>/<int:customer_id>/<int:client_id>/<int:site_id>/<int:fork_id>/',
           methods=('GET', ))
def fork_lifts_del(user_id, customer_id, client_id, site_id, fork_id):
    fork_lift = ForkLift.query.get_or_404(fork_id)
    db.session.delete(fork_lift)
    db.session.commit()
    return redirect(url_for('fork_lifts', user_id=user_id, customer_id=customer_id, client_id=client_id, site_id=site_id))


@app.route('/users/<int:user_id>/', methods=['GET'])
def users(user_id):
    customers_list_temp = Customer.query.all()
    user_list = User.query.all()
    user = User.query.filter_by(id=user_id).first()
    inc_customers = {customer.id: None for customer in user.customers}
    if user.user_role == 'admin':
        customers_list = customers_list_temp
    else:
        customers_list = [customer for customer in customers_list_temp if customer.id in inc_customers]
    return render_template('users.html', user_id=user_id, user_role=user.user_role,
                           customers=customers_list, users=user_list)


@app.route('/users/edit/<int:user_id>/<string:user_role>/<int:user_id_edit>/', methods=['GET', 'POST'])
def users_edit(user_id, user_role, user_id_edit):
    user = User.query.get_or_404(user_id_edit)
    if request.method == 'POST':
        user.name = request.form['name']
        user.password = request.form['password']
        user.user_role = request.form['user_role']

        db.session.commit()
        url = url_for('users', user_id=user_id)
        return redirect(url)

    return render_template('users_edit.html', user_id=user_id, user_role=user_role, user=user)


@app.route('/users/add/<int:user_id>/<string:user_role><int:customer_id>/', methods=('GET', 'POST'))
def users_add(user_id, user_role, customer_id):
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_role = request.form['user_role']

        user = User.query.filter_by(name=name).first()
        if user is None:
            user = User(name=name, password=password, user_role=user_role)
            db.session.add(user)
        if user_role != 'admin':
            customer = Customer.query.get_or_404(customer_id)
            customer.users.append(user)
            db.session.commit()

        return redirect(url_for('users', user_id=user_id))

    return render_template('users_add.html', user_id=user_id, user_role=user_role, customer_id=customer_id)


@app.route('/users/del/<int:user_id>/<int:user_id_del>/<int:customer_id>/', methods=('GET', ))
def users_del(user_id, user_id_del, customer_id):
    user = User.query.get_or_404(user_id_del)
    customer = Customer.query.get_or_404(customer_id)
    customer_users = list(customer.users)
    customer.users.clear(user)
    for user_to_add in customer_users:
        if user_to_add.id != user_id_del:
            customer.users.append(user_to_add)
    db.session.commit()
    if len(user.customers) == 0:
        db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users', user_id=user_id))


@app.route('/create_db', methods=['GET', 'POST'])
def create_db():
    Main.create_db()
    return redirect(url_for('customers', user_id=1))


@app.route('/create_empty_db', methods=['GET', 'POST'])
def create_empty_db():
    Main.create_empty_db()
    return redirect(url_for('customers', user_id=1))


if __name__ == '__main__':
    Main.init()
