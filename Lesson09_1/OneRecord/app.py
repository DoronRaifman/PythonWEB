import os
import socket

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Data', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class App:
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
        print(f'start serving server site on url: {url}')
        app.run(host=real_ip, port=port)

    @classmethod
    def create_db(cls):
        db.drop_all()
        db.create_all()
        students_list = [
            Student(firstname='doron', lastname='raifman', email='doron@example.com', age=64,
                    bio='Computer Science'),
            Student(firstname='john', lastname='doe', email='jd@example.com', age=23,
                    bio='Biology student'),
            Student(firstname='Sammy', lastname='Shark', email='sammyshark@example.com', age=20,
                    bio='Marine biology student'),
            Student(firstname='Carl', lastname='White', email='carlwhite@example.com', age=22,
                    bio='Marine geology student'),
        ]
        for student in students_list:
            db.session.add(student)
        db.session.commit()
        students = Student.query.all()
        print(students)
        return students


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname} {self.lastname}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('index.html', students=[student])


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        student = Student(firstname=firstname, lastname=lastname, email=email, age=age, bio=bio)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('edit.html', student=student)


@app.post('/<int:student_id>/delete/')
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/create_db', methods=['GET', 'POST'])
def create_db():
    students = App.create_db()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    App.init()
