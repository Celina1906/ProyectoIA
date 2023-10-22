from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATE_FOLDER"] = "templates"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/confirmar", methods=["POST"])
def confirmar():
    # Obtener el valor del cuadro de texto
    valor = request.form["valor"]

    # Mostrar el valor en la pantalla
    return render_template("confirmar.html", valor=valor)

if __name__ == "__main__":
    app.run(debug=True)
