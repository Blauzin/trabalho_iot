from flask import Blueprint, request, render_template

login = Blueprint('login', __name__, template_folder='templates')

users = {
    'user1': '1234',
    'user2': '1234'
}

@login.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')