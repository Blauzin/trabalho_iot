from flask import Flask, render_template, request, redirect, url_for, session
from auth import auth
from actuators import actuator_bp
from config import sensor_data, actuator_data, sensor_history

app = Flask(__name__)
app.secret_key = 'my_very_secret_key'

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(actuator_bp)


@app.route('/sensors')
def sensors():
    
    return render_template('sensors.html', sensors=sensor_data, sensor_history = sensor_history, active_page='sensors')

@app.route('/actuators')
def actuators():

    return render_template('actuators.html', actuators=actuator_data, active_page='actuators')

@app.route('/manage_sensors')
def manage_sensors():
    return ('sensors')

@app.route('/manage_users')
def manage_users():
    return ('users')

if __name__ == '__main__':
    app.run(debug=True)

