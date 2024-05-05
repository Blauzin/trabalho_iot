from flask import Flask, render_template, jsonify, request

sensores = {'Umidade':56, 'Temperatura':25, 'Luminosidade':15}

users = {
    'user1': '1234',
    'user2': '1234'   
}

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

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

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/demonstration', methods=['GET'])
def demonstration():
    return jsonify(sensores)

@app.route('/sensors')
def sensors():
    sensores = {'T1':56, 'T2':25, 'T3':15}
    return render_template('sensors.html', sensores=sensores)

@app.route('/actuators')
def actuators():
    atuadores = {'Servo Motor':0, 'Lâmpada':1}
    return render_template('actuators.html', atuadores=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)