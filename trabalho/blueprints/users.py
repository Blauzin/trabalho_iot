from flask import Blueprint, render_template, request, redirect, url_for
from config import users

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

@user_bp.route('/manage_users')
def manage_users():
    return render_template('manage_users.html', users=users, active_page='manage_users')

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    password = request.form['password']
    if name not in users:
        users[name] = {'password': password, 'is_admin': False, 'image': 'default_image.jpg'}
    return redirect(url_for('user_bp.manage_users'))

@user_bp.route('/del_user', methods=['POST'])
def del_user():
    name = request.form['name']
    if name in users:
        users.pop(name)
    return redirect(url_for('user_bp.manage_users'))

@user_bp.route('/edit_user/<user_name>', methods=['POST'])
def edit_user(user_name):
    new_name = request.form['new_name']
    new_password = request.form['new_password']
    if new_name and new_password:
        users[new_name] = {'password': new_password, 'is_admin': users[user_name]['is_admin'], 'image': users[user_name]['image']}
        users.pop(user_name)
    elif new_name:
        users[new_name] = users.pop(user_name)
    elif new_password:
        users[user_name]['password'] = new_password
    return redirect(url_for('user_bp.manage_users'))
