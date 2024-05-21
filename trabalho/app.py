from flask import Flask, render_template, request, redirect, url_for, session
from config import sensor_data, actuator_data, sensor_history, users
from blueprints import auth, actuators, sensors, users as users_bp
import paho.mqtt.client as mqtt
import json
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Role

app = Flask(__name__)
app.secret_key = 'my_very_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

# MQTT setup
broker = "mqtt-dashboard.com"
port = 1883
topic_sensor1 = "leakspy/sensor1"
topic_sensor2 = "leakspy/sensor2"
topic_actuators = "leakspy/actuators"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc)) 
    client.subscribe([(topic_sensor1, 0), (topic_sensor2, 0)])

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    if msg.topic == topic_sensor1:
        sensor_data['sensor1']['value'] = payload['value']
        sensor_history['sensor1'].append({'timestamp': payload['timestamp'], 'value': payload['value']})
    elif msg.topic == topic_sensor2:
        sensor_data['sensor2']['value'] = payload['value']
        sensor_history['sensor2'].append({'timestamp': payload['timestamp'], 'value': payload['value']})

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(broker, port, 60)
mqtt_client.loop_start()

app.register_blueprint(auth.auth, url_prefix='/')
app.register_blueprint(actuators.actuator_bp)
app.register_blueprint(sensors.sensor_bp)
app.register_blueprint(users_bp.user_bp)

@app.route('/sensors')
def sensors():
    return render_template('sensors.html', sensors=sensor_data, sensor_history=sensor_history, active_page='sensors')

@app.route('/actuators', methods=['GET', 'POST'])
def actuators():
    if request.method == 'POST':
        action = request.form.get('action')
        actuator_name = request.form.get('actuator')
        if action == 'On':
            actuator_data[actuator_name]['state'] = 'On'
        elif action == 'Off':
            actuator_data[actuator_name]['state'] = 'Off'
        # Publish the state to the MQTT broker
        mqtt_client.publish(topic_actuators, json.dumps({
            'actuator': actuator_name,
            'state': actuator_data[actuator_name]['state']
        }))
    return render_template('actuators.html', actuators=actuator_data, active_page='actuators')

@app.route('/manage_sensors')
def manage_sensors():
    return render_template('manage_sensors.html', sensors=sensor_data, active_page='manage_sensors')

@app.route('/manage_users')
def manage_users():
    return render_template('manage_users.html', users=users, active_page='manage_users')

if __name__ == '__main__':
    app.run(debug=True)
