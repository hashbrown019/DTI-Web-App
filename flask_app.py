import Configurations as c
c.SQLITE_DB = c.SQLITE_DB_SERVER
c.RECORDS = c.RECORDS_SERVER
c.M_APPVER = c.M_APPVER_SERVER

c._SERVER_PORT = c.SERVER_PORT
c._HOST = c.SERVER_HOST
c._USER = c.SERVER_USER
c._PASSWORD = c.SERVER_PASSWORD
c._DATABASE = c.SERVER_DATABASE

from flask import Flask, session, jsonify, request, redirect
from flask_cors import CORS,cross_origin
from flask_minify import Minify

from views import login
from views import home
from controllers import api
from controllers import apiV2
from controllers import migrations
# import sms_main as gsm
c.PORT = 80


app = Flask(__name__)
Minify(app=app, html=True, js=True, cssless=True, static=True)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key=c.SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(home.app)
app.register_blueprint(login.app)
app.register_blueprint(api.app)
app.register_blueprint(apiV2.app)
app.register_blueprint(migrations.app)

@app.route("/")
def index():return redirect("/login")