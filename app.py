import Configurations as c
c.SQLITE_DB = c.SQLITE_DB_SERVER
c.RECORDS = c.RECORDS_SERVER
c.M_APPVER = c.M_APPVER_SERVER

c._SERVER_PORT = C.SERVER_PORT
c._HOST = C.SERVER_HOST
c._USER = C.SERVER_USER
c._PASSWORD = C.SERVER_PASSWORD
c._DATABASE = C.SERVER_DATABASE

print(" * SERVER Launch")


from flask import Flask, session, jsonify, request, redirect
from flask_cors import CORS,cross_origin

from views import login
from views import home
from controllers import api
from controllers import migrations
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
app.register_blueprint(migrations.app)

@app.route("/")
def index():return redirect("/login")

# @app.before_request
# def before_request():
# 	if( request.endpoint != "static" and "Handshake" not in str(request.endpoint).split(".")):
# 		if "USER_DATA" not in session:
# 			if(request.endpoint != "login.login"):
# 				return redirect('/login')
# 		else:
# 			if(request.endpoint == "login.login"):
# 				return redirect('/home')
# 	pass


app.run(host=c.HOST,port=c._PORT,debug=c.IS_DEBUG)
