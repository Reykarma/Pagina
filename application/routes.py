from application import app
from flask import render_template


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/Desarrollo_web")
def desarrollo_web():
    return render_template("web_design.html")

@app.route("/Programacion")
def programacion():
    return render_template("programacion.html")

