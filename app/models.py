from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config(app):
    db.init_app(app)
    app.db = db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Colaborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    department = db.relationship('Department', backref='colaborators')

class Dependent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    colaborator_id = db.Column(db.Integer, db.ForeignKey('colaborator.id'))

    colaborator = db.relationship('Colaborator', backref='dependents')
