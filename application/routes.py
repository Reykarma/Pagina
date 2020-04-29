from flask import render_template
from application import app

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/web_design")
def servicios():
    return render_template("web_design.html")

@app.errorhandler(404)
def page_not_found(e):
    return "404"
