from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json

app = Blueprint("login",__name__)

# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
rapid= sqlite("assets\\db\\dti_rapidxi.db")


class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg

	@app.route("/login",methods=["POST","GET"])
	def login():
		return render_template("login/login.html")

	@app.route("/login_auth",methods=["POST"])
	def login_auth():
		username = request.form['user_name']
		password = request.form['password']
		log_res = rapid.select("SELECT * from `users_account` WHERE `user_name` = '{}' AND `password`='{}';".format(username,password))
		return jsonify(log_res)