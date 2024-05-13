# actuators.py

from flask import Blueprint, render_template, request

actuators_bp = Blueprint('actuators', __name__, template_folder='templates')
global atuadores
atuadores = {'Servo Motor': 0, 'Lâmpada': 1}


@actuators_bp.route('/register_actuator')
def register_actuator():
    return render_template('register_actuator.html')


@actuators_bp.route('/add_actuator', methods=['GET', 'POST'])
def add_actuator():
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores[atuador] = 0
    return render_template('actuators.html', devices=atuadores)


@actuators_bp.route('/remove_actuator')
def remove_actuator():
    return render_template('remove_actuator.html', devices=atuadores)


@actuators_bp.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores.pop(atuador)
    return render_template('actuators.html', devices=atuadores)

@actuators_bp.route('/actuators')
def actuators():
    return render_template('actuators.html', devices=atuadores)