from flask import Blueprint, render_template, request, session, redirect, url_for
from config import users

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                session['is_admin'] = user['is_admin']
                return redirect(url_for('auth.home'))
        return '<h1>Invalid credentials!</h1>'
    else:
        return render_template('login.html')

@auth.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', active_page='home')
    else:
        return redirect(url_for('auth.login'))
    
@auth.route('/logout')
def logout():
    # Remove the user information from the session
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('auth.login'))
