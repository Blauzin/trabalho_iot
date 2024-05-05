from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

sensores = {'Umidade':56, 'Temperatura':25, 'Luminosidade':15}
atuadores = {'Servo Motor':0, 'Lâmpada':1}

users = {
    'user1': '1234',
    'user2': '1234'   
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register_user')
def register_user():
    return render_template('register_user.html')

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template('users.html', devices=users)

@app.route('/remove_user')
def remove_user():
    return render_template('remove_user.html', devices=users)

@app.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template('users.html', devices=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template('users.html', devices=users)

@app.route('/validated_user', methods=['POST'])
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

@app.route('/register_sensor')
def register_sensor():
    return render_template('register_sensor.html')

@app.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores[sensor] = 0
    return render_template('sensors.html', devices=sensores)

@app.route('/remove_sensor')
def remove_sensor():
    return render_template('remove_sensor.html', devices=sensores)

@app.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores.pop(sensor)
    return render_template('sensors.html', devices=sensores)

@app.route('/register_actuator')
def register_actuator():
    return render_template('register_actuator.html')

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores[atuador] = 0
    return render_template('actuators.html', devices=atuadores)

@app.route('/remove_actuator')
def remove_actuator():
    return render_template('remove_actuator.html', devices=atuadores)

@app.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores.pop(atuador)
    return render_template('actuators.html', devices=atuadores)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/demonstration', methods=['GET'])
def demonstration():
    return jsonify(sensores)

@app.route('/sensors')
def sensors():
    sensores = {'T1':56, 'T2':25, 'T3':15}
    return render_template('sensors.html', devices=sensores)

@app.route('/actuators')
def actuators():
    atuadores = {'Servo Motor':0, 'Lâmpada':1}
    return render_template('actuators.html', devices=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)