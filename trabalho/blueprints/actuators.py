from flask import Blueprint, render_template, request, redirect, url_for
from config import actuator_data

actuator_bp = Blueprint('actuator_bp', __name__, template_folder='templates')

@actuator_bp.route('/manage_actuators')
def manage_actuators():
    return render_template('manage_actuators.html', actuators=actuator_data, active_page='manage_actuators')

@actuator_bp.route('/add_actuator', methods=['POST'])
def add_actuator():
    name = request.form['name']
    if name not in actuator_data:
        actuator_data[name] = {'name': name, 'state': 'Off', 'image': 'default_image.jpg'}
    return redirect(url_for('actuator_bp.manage_actuators'))

@actuator_bp.route('/del_actuator', methods=['POST'])
def del_actuator():
    name = request.form['name']
    if name in actuator_data:
        actuator_data.pop(name)
    return redirect(url_for('actuator_bp.manage_actuators'))

@actuator_bp.route('/edit_actuator/<actuator_name>', methods=['POST'])
def edit_actuator(actuator_name):
    new_name = request.form['new_name']
    actuator_data[new_name] = actuator_data.pop(actuator_name)
    actuator_data[new_name]['name'] = new_name  # Atualiza o nome do atuador
    return redirect(url_for('actuator_bp.manage_actuators'))