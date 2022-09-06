from flask import Blueprint, render_template, request, session, redirect, jsonify, send_file
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json
from flask_cors import CORS,cross_origin
import base64
import sys

app = Blueprint("migrations",__name__)
cors = CORS(app)

rapid= sqlite(c.SQLITE_DB)


class _main:
	@app.route("/migrationtest",methods=["POST","GET"])
	def migrationtest():
		return "migration module ready"

	@app.route("/json_checker",methods=["POST","GET"])
	def json_checker():
		res = {"good":[],"bad":[]}
		dir_path = c.RECORDS+"profiles/__temp__/"
		print(dir_path)
		file_ls = os.listdir(dir_path)
		for path in file_ls:
			if os.path.isfile(os.path.join(dir_path, path)):
				fr_s = open(dir_path+path,"r")
				raw_strs = fr_s.read()
				try:
					_data = json.loads(json.loads(raw_strs))
					print("type {} :: {}".format(type(_data),path) )
					res["good"].append(path)
				except:
					print("error : [{}]====\n{}".format(path,sys.exc_info()[0]))
					res["bad"].append(path)
				fr_s.close()
		
		return jsonify(res)


