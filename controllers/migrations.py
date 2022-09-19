from flask import Blueprint, render_template, request, session, redirect, jsonify, send_file
from flask_session import Session
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json
from flask_cors import CORS,cross_origin
import base64
import sys
import pandas as pd

app = Blueprint("migrations",__name__)
cors = CORS(app)

rapid= sqlite(c.SQLITE_DB)

mysqldb = mysql(c._HOST,c._USER,c._PASSWORD,c._DATABASE)

class _main:
	@app.route("/migrationtest",methods=["POST","GET"])
	def migrationtest():
		resp = "database : {}".format(str(mysqldb.select("SELECT VERSION()") ))
		note = resp + " || end DB"
		print(note)
		return note

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

	@app.route("/excel_popu",methods=["POST","GET"])
	def excel_popu():
		file_name =  c.RECORDS+"/spreadsheets/93#2022-09-19#NSAMAR_vc_a_1.xlsx" # path to file + file name
		sheet =  "VC FORM A" # sheet name or sheet number or list of sheet numbers and names

		df = pd.read_excel(io=file_name, sheet_name=sheet)
		EXCEL_DATA = df.iterrows()

		_result = {}
		LLL = dict(EXCEL_DATA)
		for key in LLL:
			_result[key] = [] 
			for val in LLL[key]:
				_result[key].append(val)

		counter = 0
		new_struc = {}
		__new_struc = []

		t1 = None
		t2 = None
		t3 = None

		# for colNames in df.head():
		# 	# print(colNames.find("Unnamed"))
		# 	if(colNames.find("Unnamed") == 0): pass
		# 	else:
		# 		new_struc[colNames] = {}
		# 		t1 =colNames

		# 	if (str(_result[0][counter]).lower().find("nan")):
		# 		new_struc[t1][_result[0][counter]] = {}
		# 		t2 = _result[0][counter]

		# 	new_struc[t1][t2][_result[1][counter] ]= _main.x_filed_get(_result,counter)
		# 	counter = counter + 1
		# return new_struc
		del _result[0]
		return (_result)
	
	def x_filed_get(_result,counter):
		row_counter = 0
		data = []
		for _res in _result:
			if row_counter >2 :
				data.append(_result[_res][counter])
			row_counter =  row_counter + 1
		return data
		# return data

	@app.route("/append_data_excel_mdata")
	def append_data_excel_mdata():
		datas = (_main.excel_popu())

		return str(len(datas))

	

	@app.route("/excel_upload",methods=["POST","GET"])
	def excel_upload():
		from datetime import date

		today = str(date.today())
		uploader = request.form['uploader']
		excel_ = request.files
		for excel in excel_:
			f = excel_[excel]
			f.save(os.path.join(c.RECORDS+"/spreadsheets/", uploader+"#"+today+"#"+secure_filename(f.filename)))
		return _main.get_uploaded_excel()
		# return data

	@app.route("/get_uploaded_excel",methods=["POST","GET"])
	def get_uploaded_excel():
		return jsonify(os.listdir(c.RECORDS+"/spreadsheets/"))
		# return data