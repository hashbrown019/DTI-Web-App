from flask import Flask, session, jsonify, request, redirect
import Configurations as c
from flask_cors import CORS,cross_origin

from views import login
from views import home
from controllers import api
# import sms_main as gsm
c.PORT = 80

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key=c.SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.register_blueprint(home.app)
app.register_blueprint(login.app)
app.register_blueprint(api.app)

@app.route("/")
def index():return redirect("/login")