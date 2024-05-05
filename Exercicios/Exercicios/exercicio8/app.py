from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    rooms = {'Quarto':'/bedroom', 'Banheiro':'/bathroom'}
    return render_template('index.html', rooms=rooms)

@app.route('/bedroom')
def bedroom():
    devices = {'Sensor de Luminosidade':1000, 'Interruptor':2}
    return render_template('bedroom.html', devices=devices)

@app.route('/bathroom')
def bathroom():
    devices = {'Sensor de Umidade':27, 'Lâmpada Inteligente':1}
    return render_template('bathroom.html', devices=devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)