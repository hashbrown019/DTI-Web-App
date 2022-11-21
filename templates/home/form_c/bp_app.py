from flask import Flask, Blueprint, render_template, url_for

app = Blueprint("form_c",__name__,template_folder="templates")

@app.route('/formc')
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

@app.route("/dcf/dcf_trade_promotion")
def dcf_trade_promotion():
    return render_template("dcf_trade_promotion.html")


@app.route("/dcf/dcf_product_development")
def dcf_product_development():
    return render_template("dcf_product_development.html")

@app.route("/dcf/dcf_matching_grant")
def dcf_matching_grant():
    return render_template("dcf_matching_grant.html")

@app.route("/dcf/dcf_enablers_tracker")
def dcf_enablers_tracker():
    return render_template("dcf_enablers_tracker.html")

if __name__ == "__main__":
    app.run(debug=True)

    # sample edit