from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from models import db, User, Sensor, Actuator, SensorData
from flask_login import LoginManager, login_required, current_user
import paho.mqtt.client as mqtt
import json
from datetime import datetime

# Importar os Blueprints
from auth import auth as auth_bp
from sensors import sensor_bp
from actuators import actuator_bp
from users import user_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# MQTT setup
broker = "broker.hivemq.com"
port = 1883
topic_sensor1 = "leakspy/sensor1"
topic_sensor2 = "leakspy/sensor2"
topic_actuators = "leakspy/actuators"
topic_diff = "leakspy/diff_water"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe([(topic_sensor1, 0), (topic_sensor2, 0), (topic_actuators, 0), (topic_diff, 0) ])
    print(f"Subscribed to topics: {topic_sensor1}, {topic_sensor2}, {topic_actuators}, {topic_diff}")

def on_message(client, userdata, msg):
    with app.app_context():
        print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
        payload = json.loads(msg.payload.decode())
        if msg.topic == topic_sensor1:
            sensor = Sensor.query.filter_by(name='Humidity').first()
            if sensor:
                print(f"Updating sensor {sensor.name} with value {payload['value']}")
                sensor.value = payload['value']
                db.session.add(SensorData(sensor_id=sensor.id, value=payload['value'], timestamp=datetime.now()))
                db.session.commit()
                print(f"Sensor {sensor.name} updated with value {sensor.value}")
            else:
                print("Sensor 'Humidity' not found")
        elif msg.topic == topic_sensor2:
            sensor = Sensor.query.filter_by(name='Pressure').first()
            if sensor:
                print(f"Updating sensor {sensor.name} with value {payload['value']}")
                sensor.value = payload['value']
                db.session.add(SensorData(sensor_id=sensor.id, value=payload['value'], timestamp=datetime.now()))
                db.session.commit()
                print(f"Sensor {sensor.name} updated with value {sensor.value}")
            else:
                print("Sensor 'Pressure' not found")
        elif msg.topic == topic_actuators:
            actuator = Actuator.query.filter_by(name=payload['actuator']).first()
            if actuator:
                print(f"Updating actuator {actuator.name} with state {payload['state']}")
                actuator.state = payload['state']
                db.session.commit()
                print(f"Actuator {actuator.name} updated with state {actuator.state}")
            else:
                print(f"Actuator {payload['actuator']} not found")
        elif msg.topic == topic_diff:
            sensor = Sensor.query.filter_by(name='Water Loss').first()
            if sensor:
                print(f"Updating sensor {sensor.name} with value {payload['value']}")
                sensor.value = payload['value']
                db.session.add(SensorData(sensor_id=sensor.id, value=payload['value'], timestamp=datetime.now()))
                db.session.commit()
                print(f"Sensor {sensor.name} updated with value {sensor.value}")
            else:
                print("Sensor 'PotentiometerDifference' not found")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(broker, port, 60)
mqtt_client.loop_start()

# Registrar Blueprints
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(actuator_bp)
app.register_blueprint(sensor_bp)
app.register_blueprint(user_bp)

@app.route('/historical_data')
@login_required
def historical_data():
    if current_user.role not in ['Admin', 'Estatístico']:
        return redirect(url_for('auth.home'))
    sensors = Sensor.query.all()
    sensor_id = request.args.get('sensor_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    data = []
    if sensor_id and start_date and end_date:
        data = SensorData.query.filter(
            SensorData.sensor_id == sensor_id,
            SensorData.timestamp.between(start_date, end_date)
        ).all()
    return render_template('historical_data.html', sensors=sensors, data=data, active_page='historical_data')

@app.route('/sensors')
@login_required
def sensors():
    sensors = Sensor.query.all()
    for sensor in sensors:
        print(f"Sensor {sensor.name} has value {sensor.value}")  # Debugging line
    return render_template('sensors.html', sensors=sensors, active_page='sensors')

@app.route('/actuators', methods=['GET', 'POST'])
@login_required
def actuators():
    if current_user.role not in ['Admin', 'Operador']:
        return redirect(url_for('auth.home'))
    actuators = Actuator.query.all()
    if request.method == 'POST':
        action = request.form.get('action')
        actuator_name = request.form.get('actuator')
        actuator = Actuator.query.filter_by(name=actuator_name).first()
        if action == 'On':
            actuator.state = 'On'
        elif action == 'Off':
            actuator.state = 'Off'
        mqtt_client.publish(topic_actuators, json.dumps({
            'actuator': actuator.name,
            'state': actuator.state
        }))
        db.session.commit()
    return render_template('actuators.html', actuators=actuators, active_page='actuators')

@app.route('/manage_sensors')
@login_required
def manage_sensors():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    sensors = Sensor.query.all()
    return render_template('manage_sensors.html', sensors=sensors, active_page='manage_sensors')

@app.route('/manage_users')
@login_required
def manage_users():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    users = User.query.all()
    return render_template('manage_users.html', users=users, active_page='manage_users')



@app.route('/remote_commands', methods=['GET', 'POST'])
@login_required
def remote_commands():
    if current_user.role not in ['Admin', 'Operador']:
        return redirect(url_for('auth.home'))
    actuators = Actuator.query.all()
    if request.method == 'POST':
        action = request.form.get('action')
        actuator_name = request.form.get('actuator')
        actuator = Actuator.query.filter_by(name=actuator_name).first()
        if action == 'On':
            actuator.state = 'On'
        elif action == 'Off':
            actuator.state = 'Off'
        mqtt_client.publish(topic_actuators, json.dumps({
            'actuator': actuator.name,
            'state': actuator.state
        }))
        db.session.commit()
    return render_template('remote_commands.html', actuators=actuators, active_page='remote_commands')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
