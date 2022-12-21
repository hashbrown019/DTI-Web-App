import Configurations as c
c.SQLITE_DB = c.SQLITE_DB_SERVER
c.RECORDS = c.RECORDS_SERVER
c.M_APPVER = c.M_APPVER_SERVER

c._SERVER_PORT = c.SERVER_PORT
c._HOST = c.SERVER_HOST
c._USER = c.SERVER_USER
c._PASSWORD = c.SERVER_PASSWORD
c._DATABASE = c.SERVER_DATABASE

print(" * Providing Imports Flask app")

from flask import Flask, session, jsonify, request, redirect
from flask_cors import CORS,cross_origin
from flask_minify import Minify

from views import login
from views import home
from controllers import api
from controllers import apiV2
from controllers import migrations
from controllers.GLOBALS_ import Globals_

from templates.home.form_c import bp_app as bp_c
from templates.home.form_c import excel_migration as e_m


# import sms_main as gsm
c.PORT = 80

print(" * Creating Flask app")

app = Flask(__name__)
Minify(app=app, html=True, js=True, cssless=True, static=True)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key=c.SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False


print(" * Registring blueprints on  Flask app")

app.register_blueprint(home.app)
app.register_blueprint(login.app)
app.register_blueprint(api.app)
app.register_blueprint(apiV2.app)
app.register_blueprint(migrations.app)

app.register_blueprint(bp_c.app)
app.register_blueprint(e_m.app)


Globals_(app)

@app.route("/")
def index():return redirect("/login")

print(" * Running Flask app")

app.run(host="0.0.0.0",port=8000)