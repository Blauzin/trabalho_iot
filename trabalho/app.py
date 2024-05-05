from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    sensor1_valor = 10
    sensor1_historico = [9, 11, 12, 10, 9]

    sensor2_valor = 20
    sensor2_historico = [19, 21, 22, 20, 19]

    return render_template('index.html', sensor1_valor=sensor1_valor, sensor1_historico=sensor1_historico, sensor2_valor=sensor2_valor, sensor2_historico=sensor2_historico)

if __name__ == '__main__':
    app.run(debug=True)

