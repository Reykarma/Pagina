from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
