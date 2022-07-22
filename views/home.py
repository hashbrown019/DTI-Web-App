from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json

app = Blueprint("home",__name__)

# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
rapid= sqlite("assets\\db\\dti_rapidxi.db")


class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg

	@app.route("/home",methods=["POST","GET"])
	def home():
		return redirect("/homepage#0")


	@app.route("/homepage",methods=["POST","GET"])
	def homepage():
		return render_template("home/home.html")