from flask import Blueprint, render_template, request, redirect, url_for
from config import sensor_data

sensor_bp = Blueprint('sensor_bp', __name__, template_folder='templates')

@sensor_bp.route('/manage_sensors')
def manage_sensors():
    return render_template('manage_sensors.html', sensors=sensor_data, active_page='manage_sensors')

@sensor_bp.route('/add_sensor', methods=['POST'])
def add_sensor():
    name = request.form['name']
    if name not in sensor_data:
        sensor_data[name] = {'name': name, 'state': 'Inactive', 'image': 'default_image.jpg'}
    return redirect(url_for('sensor_bp.manage_sensors'))

@sensor_bp.route('/del_sensor', methods=['POST'])
def del_sensor():
    name = request.form['name']
    if name in sensor_data:
        sensor_data.pop(name)
    return redirect(url_for('sensor_bp.manage_sensors'))

@sensor_bp.route('/edit_sensor/<sensor_name>', methods=['POST'])
def edit_sensor(sensor_name):
    new_name = request.form['new_name']
    sensor_data[new_name] = sensor_data.pop(sensor_name)
    sensor_data[new_name]['name'] = new_name  # Atualiza o nome do sensor
    return redirect(url_for('sensor_bp.manage_sensors'))
