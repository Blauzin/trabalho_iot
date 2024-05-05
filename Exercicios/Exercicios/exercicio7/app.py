from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensors')
def sensors():
    sensores = {'Sensor de Umidade':22, 'Sensor de Temperatura':23, 'Sensor de Luminosidade':1034}
    return render_template('sensors.html', sensores=sensores)
@app.route('/actuators')
def actuators():
    atuadores = {'Servo Motor':122, 'Lâmpada':1}
    return render_template('actuators.html', atuadores=atuadores)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)