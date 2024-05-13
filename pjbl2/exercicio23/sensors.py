# sensors.py

from flask import Blueprint, render_template, request

sensors_bp = Blueprint('sensors', __name__, template_folder='templates')

sensores = {'Umidade': 56, 'Temperatura': 25, 'Luminosidade': 15}


@sensors_bp.route('/register_sensor')
def register_sensor():
    return render_template('register_sensor.html')


@sensors_bp.route('/add_sensor', methods=['GET', 'POST'])
def add_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores[sensor] = 0
    return render_template('sensors.html', devices=sensores)


@sensors_bp.route('/remove_sensor')
def remove_sensor():
    return render_template('remove_sensor.html', devices=sensores)


@sensors_bp.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores.pop(sensor)
    return render_template('sensors.html', devices=sensores)

@sensors_bp.route('/sensors')
def sensors():
    return render_template('sensors.html', devices=sensores)