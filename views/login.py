from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json

app = Blueprint("login",__name__)

# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
# rapid= sqlite("assets\\db\\dti_rapidxi.db")
rapid= sqlite(c.SQLITE_DB)


class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg

	@app.route("/login",methods=["POST","GET"])
	def login():
		return render_template("SITE_OFF.html") # MAINTENANCE
		return render_template("login/login.html")

	@app.route("/login_auth",methods=["POST"])
	def login_auth():
		username = request.form['user_name']
		password = request.form['password']
		log_res = rapid.select("SELECT * from `users` WHERE `username` = '{}' AND `password`='{}';".format(username,password))
		if(len(log_res)!=0):
			log_res[0]['password'] = "********"
			session["USER_DATA"] = log_res
			return jsonify({"success":True,"user":session["USER_DATA"]})
		else:
			return jsonify({"success":False})

	@app.route("/logout")
	def logout():
		session.clear()
		return redirect("/home")
		# return jsonify(session )

	@app.route("/get_session")
	def get_session():
		return jsonify(session )