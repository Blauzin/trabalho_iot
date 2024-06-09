from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Actuator

actuator_bp = Blueprint('actuator_bp', __name__, template_folder='templates')

@actuator_bp.route('/manage_actuators')
@login_required
def manage_actuators():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    actuators = Actuator.query.all()
    return render_template('manage_actuators.html', actuators=actuators, active_page='manage_actuators')

@actuator_bp.route('/add_actuator', methods=['POST'])
@login_required
def add_actuator():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    name = request.form['name']
    actuator = Actuator(name=name, image='default_image.jpg', state='Off')
    db.session.add(actuator)
    db.session.commit()
    return redirect(url_for('actuator_bp.manage_actuators'))

@actuator_bp.route('/del_actuator', methods=['POST'])
@login_required
def del_actuator():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    name = request.form['name']
    actuator = Actuator.query.filter_by(name=name).first()
    if actuator:
        db.session.delete(actuator)
        db.session.commit()
    return redirect(url_for('actuator_bp.manage_actuators'))

@actuator_bp.route('/edit_actuator/<actuator_name>', methods=['POST'])
@login_required
def edit_actuator(actuator_name):
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    new_name = request.form['new_name']
    actuator = Actuator.query.filter_by(name=actuator_name).first()
    if new_name:
        actuator.name = new_name
    db.session.commit()
    return redirect(url_for('actuator_bp.manage_actuators'))
