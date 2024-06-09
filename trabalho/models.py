from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Admin, Estatístico, Operador

    def set_password(self, password):
        self.password = password  # Armazenar a senha em texto simples

    def check_password(self, password):
        print(f"Checking password for user {self.username}")
        print(f"Stored password: {self.password}")
        print(f"Provided password: {password}")
        return self.password == password



class Kit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sensors = db.relationship('Sensor', backref='kit', lazy=True)
    actuators = db.relationship('Actuator', backref='kit', lazy=True)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    value = db.Column(db.Float, nullable=True)
    kit_id = db.Column(db.Integer, db.ForeignKey('kit.id'), nullable=True)

class Actuator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    kit_id = db.Column(db.Integer, db.ForeignKey('kit.id'), nullable=True)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    sensor = db.relationship('Sensor', backref=db.backref('data', lazy=True))
