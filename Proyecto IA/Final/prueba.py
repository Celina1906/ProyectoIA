from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_numero', methods=['POST'])
def procesar_numero():
    numero = request.form['numero']
    return render_template('resultado.html', numero=numero)

if __name__ == '__main__':
    app.run(debug=True)
