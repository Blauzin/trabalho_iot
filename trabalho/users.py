from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, User

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

@user_bp.route('/manage_users')
@login_required
def manage_users():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    users = User.query.all()
    return render_template('manage_users.html', users=users, active_page='manage_users')

@user_bp.route('/add_user', methods=['POST'])
@login_required
def add_user():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    name = request.form['name']
    password = request.form['password']
    user = User(username=name, password=password, role='Operador')  # Define o papel padrão
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('user_bp.manage_users'))

@user_bp.route('/del_user', methods=['POST'])
@login_required
def del_user():
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    name = request.form['name']
    user = User.query.filter_by(username=name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('user_bp.manage_users'))

@user_bp.route('/edit_user/<user_name>', methods=['POST'])
@login_required
def edit_user(user_name):
    if current_user.role != 'Admin':
        return redirect(url_for('auth.home'))
    new_name = request.form['new_name']
    new_password = request.form['new_password']
    user = User.query.filter_by(username=user_name).first()
    if new_name:
        user.username = new_name
    if new_password:
        user.password = new_password
    db.session.commit()
    return redirect(url_for('user_bp.manage_users'))
