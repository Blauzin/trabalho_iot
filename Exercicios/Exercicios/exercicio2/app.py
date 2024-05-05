from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """
        <html>
            <head>
                <title>Casa Conectada</title>
            </head>
            <body>
                <h1>Menu Principal:</h1>
                <h3>Quarto</h3>
                <ul>
                    <li>Sensor de luminosidade</li>
                    <li>Interruptor</li>
                </ul>
                <h3>Banheiro</h3>
                <ul>
                    <li>sensor de umidade</li>
                    <li>Lampada Inteligente</li>
                </ul>
            </body>
        </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
