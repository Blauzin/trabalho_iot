from flask import Blueprint, render_template, request, redirect, url_for
from config import actuator_data
# Create a Blueprint for actuators
actuator_bp = Blueprint('actuator_bp', __name__, template_folder='templates')

@actuator_bp.route('/show_actuators')
def show_actuators():
    return render_template('manage_actuators.html', actuators=actuator_data)

@actuator_bp.route('/add_actuator', methods=['POST'])
def add_actuator():
    # Get the next ID
    next_id = max(actuator['id'] for actuator in actuator_data) + 1 if actuator_data else 1
    new_actuator = {
        'id': next_id,
        'name': request.form['name'],
        'image': 'default.jpg',  # Default image or implement a way to upload
        'state': 'Off'           # Default state
    }
    actuator_data.append(new_actuator)
    return redirect(url_for('actuator_bp.show_actuators'))

@actuator_bp.route('/edit_actuator/<int:id>', methods=['POST'])
def edit_actuator(id):
    for actuator in actuator_data:
        if actuator['id'] == id:
            # Example change, perhaps toggle state
            actuator['state'] = 'On' if actuator['state'] == 'Off' else 'Off'
            break
    return redirect(url_for('actuator_bp.show_actuators'))

@actuator_bp.route('/delete_actuator/<int:id>', methods=['POST'])
def delete_actuator(id):
    global actuator_data
    actuator_data = [actuator for actuator in actuator_data if actuator['id'] != id]
    return redirect(url_for('actuator_bp.show_actuators'))
