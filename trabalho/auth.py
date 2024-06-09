from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            print(f"User found: {user.username}")
            if user.check_password(password):
                login_user(user)
                return redirect(url_for('auth.home'))
            else:
                print("Password check failed")
        else:
            print("User not found")
        return '<h1>Invalid credentials!</h1>'
    return render_template('login.html')

@auth.route('/home')
@login_required
def home():
    return render_template('home.html', active_page='home')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
