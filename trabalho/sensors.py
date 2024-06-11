from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Sensor

sensor_bp = Blueprint('sensor_bp', __name__, template_folder='templates')

@sensor_bp.route('/manage_sensors')
@login_required
def manage_sensors():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    sensors = Sensor.query.all()
    return render_template('manage_sensors.html', sensors=sensors, active_page='manage_sensors')

@sensor_bp.route('/edit_sensor/<int:sensor_id>', methods=['POST'])
@login_required
def edit_sensor(sensor_id):
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    sensor = Sensor.query.get(sensor_id)
    if sensor:
        sensor.name = request.form['new_name']
        sensor.value = request.form['new_value']
        db.session.commit()
    return redirect(url_for('sensor_bp.manage_sensors'))

@sensor_bp.route('/delete_sensor', methods=['POST'])
@login_required
def del_sensor():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    sensor_id = request.form['id']
    sensor = Sensor.query.get(sensor_id)
    if sensor:
        db.session.delete(sensor)
        db.session.commit()
    return redirect(url_for('sensor_bp.manage_sensors'))

@sensor_bp.route('/add_sensor', methods=['POST'])
@login_required
def add_sensor():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    name = request.form['name']
    value = request.form['value']
    new_sensor = Sensor(name=name, image='default_image.jpg',value=value)
    db.session.add(new_sensor)
    db.session.commit()
    return redirect(url_for('sensor_bp.manage_sensors'))
