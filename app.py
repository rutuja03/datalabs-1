""" Interface """
import datetime
import uuid
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string


APP = Flask(__name__, template_folder='/Users/10652536/PycharmProjects/maincode/Template/src')
APP.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/test"
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)


class Student(DB.Model):
    """Student Table"""
    __tablename__ = 'student'
    id = DB.Column(DB.String(250), primary_key=True)
    name = DB.Column(DB.String(80))
    class_id = DB.Column(DB.String(250))
    created_on = DB.Column((DB.String(250)))
    updated_on = DB.Column((DB.String(250)))

    def __init__(self, id, name, class_id, created_on, updated_on):
        """ Initialize Constructor"""
        self.id = id
        self.name = name
        self.class_id = class_id
        self.created_on = created_on
        self.updated_on = updated_on


class Class(DB.Model):
    """Class Table"""
    __tablename__ = 'class'
    id = DB.Column(DB.String(250), primary_key=True)
    name = DB.Column(DB.String(80))
    class_leader = DB.Column(DB.String(250))
    created_on = DB.Column((DB.String(250)))
    updated_on = DB.Column(DB.String(250))

    def __init__(self, id, name, class_leader, created_on, updated_on):
        """ Initialize Constructor"""
        self.id = id
        self.name = name
        self.class_leader = class_leader
        self.created_on = created_on
        self.updated_on = updated_on
        DB.create_all()


@APP.route('/insert', methods=['GET', 'POST'])
def insert():
    """ Insert Method """
    data3 = Student.query.all()
    if request.method == 'POST':
        student_details = request.form
        name = student_details['name']
        if name is not'':
            if name.isalpha():
                unique = uuid.uuid1()
                unique1 = uuid.uuid1()
                date1 = datetime.date.today()
                date2 = None
                data1 = Student(unique, name, unique1, date1, date2)
                data2 = Class(unique1, name, unique, date1, date2)
                DB.session.add(data1)
                DB.session.add(data2)
                DB.session.commit()
                return redirect('/insert')
    return render_template('insert.html', Data1=data3)


@APP.route('/update', methods=['GET', 'POST'])
def up():
    """ Update """
    data2 = Student.query.all()
    if request.method == 'POST':
        student_details = request.form
        name = student_details['name']
        if name is not'':
            if name.isalpha():
                student_id = student_details['id']
                update_this = Student.query.filter_by(id=student_id).first()
                update_this1 = Class.query.filter_by(class_leader=student_id).first()
                update_this.name = name
                update_this1.name = name
                date1 = datetime.date.today()
                update_this.updated_on = date1
                update_this1.updated_on = date1
                DB.session.commit()
    return render_template('update.html', Data1=data2)


@APP.route('/del', methods=['GET', 'POST'])
def dele():
    """ Delete """
    data2 = Student.query.all()
    if request.method == 'POST':
        studentDetails = request.form
        ID = studentDetails['id']
        del_this = Student.query.filter_by(id=ID).first()
        del_this1 = Class.query.filter_by(class_leader=ID).first()
        DB.session.delete(del_this)
        DB.session.delete(del_this1)
        DB.session.commit()
        return redirect('/del')
    return render_template('del.html', Data1=data2)


if __name__ == '__main__':
    APP.run(debug=True)
