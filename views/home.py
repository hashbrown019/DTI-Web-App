from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json

app = Blueprint("home",__name__)


# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
rapid= sqlite("assets\\db\\dti_rapidxi.db")


class _main:
	def is_on_session(): return ('USER_DATA' in session)

	def __init__(self, arg):super(_main, self).__init__();self.arg = arg

	@app.route("/home",methods=["POST","GET"])
	def home():
		return redirect("/homepage#0")


	@app.route("/homepage",methods=["POST","GET"])
	def homepage():
		if(_main.is_on_session()):
			return render_template("home/home.html")
		else:
			return redirect("/login?force_url=1")


