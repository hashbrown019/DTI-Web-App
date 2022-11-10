from flask import Flask, Blueprint, render_template, url_for

app = Blueprint("form_c",__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/resp_prof")
def resp_prof():
    return render_template("resp_prof.html")


@app.route("/business_info")
def business_info():
    return render_template("bsns_info.html")

@app.route("/ciboasn")
def ciboasn():
    return render_template("ciboasn.html")

if __name__ == "__main__":
    app.run(debug=True)

    # sample edit