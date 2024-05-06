from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', active_page='home')

@app.route('/sensors')
def sensors():
    sensor_data = [
        {'name': 'Sensor 1', 'image': 'sensor1.jpg', 'value': 25},
        {'name': 'Sensor 2', 'image': 'sensor2.jpg', 'value': 30}
    ]
    return render_template('sensors.html', sensors=sensor_data, active_page='sensors')

@app.route('/actuators')
def actuators():
    actuator_data = [
        {'name': 'Actuator 1', 'image': 'actuator1.jpg', 'state': 'On'},
        {'name': 'Actuator 2', 'image': 'actuator2.jpg', 'state': 'Off'}
    ]
    return render_template('actuators.html', actuators=actuator_data, active_page='actuators')

if __name__ == '__main__':
    app.run(debug=True)

