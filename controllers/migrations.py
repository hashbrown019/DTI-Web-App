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

	@app.route("/api/excel_popu",methods=["POST","GET"])
	def excel_popu():
		dir_path = c.RECORDS+"/spreadsheets/"
		FROM_EXCEL_RPOFILES = []

		for path in os.listdir(dir_path):
			PATH__ = os.path.join(dir_path, path)
			if os.path.isfile(PATH__):
				if PATH__.find("._DELETED_FILE_")<0:	
					print(PATH__)

					file_name =  PATH__ # path to file + file name
					# file_name =  c.RECORDS+"/spreadsheets/93#2022-09-19#NSAMAR_vc_a_1.xlsx" # path to file + file name
					sheet =  "VC FORM A" # sheet name or sheet number or list of sheet numbers and names
					try:
						df = pd.read_excel(io=file_name, sheet_name=sheet, engine='openpyxl')
					except Exception as e:
						print(e)
						continue

					EXCEL_DATA = df.iterrows()

					_result = {}
					LLL = dict(EXCEL_DATA)
					for key in LLL:
						_result[key] = [] 
						for val in LLL[key]:
							_result[key].append(val)
					del _result[0]
					FROM_EXCEL_RPOFILES = FROM_EXCEL_RPOFILES +_main.append_data_excel_mdata(_result,path)

		return (FROM_EXCEL_RPOFILES)
		# return jsonify(FROM_EXCEL_RPOFILES)

	def append_data_excel_mdata(datas,path):
		farmer_from_excel = []
		# datas = (_main.excel_popu())
		head  = datas[1]; del datas[1];
		_ID_ = path.split("#")[0]
		USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ORDER BY `name` ASC; ".format(_ID_) )
		if(len(USER)<=0):
			USER = [{"name":"none","password":"CONFIDENTIAL"}]
		for datum in datas:
			_farmer = datas[datum]
			for inc in range(len(_farmer)):
				_farmer[inc] = "{}".format(_farmer[inc])
				if _farmer[inc]  == "nan":
					_farmer[inc] = ""


			# print("{} >>> {}".format(type(_farmer[4]),_farmer[4] ))
			if(_farmer[3] == "" or _farmer[3] == " " or _farmer[3] == None):
				continue;

			_farmer[40] = _main.region_name_cleaner(_farmer[40])
			_farmer[47] = _main.crops_name_cleaner(_farmer[47])

			farmer_from_excel.append({
				'input_by': USER[0],
				'SOURCE': "NEW_EXCEL",
				'USER_ID':_farmer[1],
				'farmer_code': path,
				'f_name':_farmer[1],
				'm_name':_farmer[2],
				'l_name':_farmer[3],
				'ext_name':_farmer[4],
				'farmer_name': "{} {} {} {}".format(_farmer[1],_farmer[2],_farmer[3],_farmer[4],),

				'farmer_sex':_farmer[5],
				'addr_region':_farmer[40],
				'addr_prov':_farmer[41],
				'addr_city':_farmer[42],
				'addr_brgy':_farmer[43],
				'farmer-primary_crop':_farmer[47],
				'farmer-fo_name_rapid': _farmer[32],
				'farmer_dip_ref': _farmer[27]
			})
		# return str(len(datas))
		return farmer_from_excel

	

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
		ls_uploaded_excel = []
		dir_path = c.RECORDS+"/spreadsheets/"

		for path in os.listdir(dir_path):
			PATH__ = os.path.join(dir_path, path)
			if path.find("~$") == -1:
				if os.path.isfile(PATH__):
					if PATH__.find("._DELETED_FILE_")<0:
						file_details = (path.split("#"))
						USER = rapid.select("SELECT * FROM `users` WHERE `id`='{}' ORDER BY `name` ASC; ".format(file_details[0]))[0]
						if(len(USER)<=0):
							USER= {"name":"none","id":"none"}
						file_name =  PATH__ # path to file + file name
						# file_name =  c.RECORDS+"/spreadsheets/93#2022-09-19#NSAMAR_vc_a_1.xlsx" # path to file + file name
						sheet =  "VC FORM A" # sheet name or sheet number or list of sheet numbers and names
						try:
							df = pd.read_excel(io=file_name, sheet_name=sheet, engine='openpyxl')
							ls_uploaded_excel.append({
								"file_name":path,
								"status": "Synced",
								"name":USER["name"],
								"id":USER["id"]
							})
						except Exception as e:
							print(e)
							ls_uploaded_excel.append({
								"file_name":path,
								"status": "Failed",
								"name":USER["name"],
								"id":USER["id"]
								})
							continue
		return jsonify(ls_uploaded_excel);
		# return jsonify(os.listdir(c.RECORDS+"/spreadsheets/"));
		# return data


	@app.route("/download_excel/<excel_file>",methods=["POST","GET"])
	def download_excel(excel_file):
		# excel_file = request.form['file']
		print(excel_file)
		def_name = excel_file.split("@@")[2]
		excel_file = excel_file.replace("@@","#")
		return send_file(c.RECORDS+"/spreadsheets/"+excel_file, as_attachment=True,download_name=def_name)

	@app.route("/delete_excel/",methods=["POST","GET"])
	def delete_excel():
		excel_file = request.form['file']
		# print(excel_file)
		def_name = excel_file.split("@@")[2]
		excel_file = excel_file.replace("@@","#")

		os.rename(
			c.RECORDS+"/spreadsheets/"+excel_file,
			c.RECORDS+"/spreadsheets/"+excel_file+"._DELETED_FILE_"
		)
		return jsonify({"status":"done"})



	# THIS FUNCTION FIX THE REGION name with SIMILAR AREA
	def region_name_cleaner(region):
		region = str(region)
		roman_numerals = ["i","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii","xiii"]
		num_digits = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
		region = region.lower()
		region = region.replace(" ","")
		region = region.replace("region","")
		region = region.replace("r-","")
		region = region.replace("r:","")
		if(region==""):region = 'Untagged';
		else:
			try:
				if(region.isnumeric()):
					region = region
				else:
					region = num_digits[roman_numerals.index(region)]
			except Exception as e:
				region = region + ""
		return region

	# THIS FUNCTION FIX THE crops name with SIMILAR AREA
	def crops_name_cleaner(crops):
		crops = str(crops)
		crops = crops.lower()
		crops = crops.replace(" ","")
		if(crops==""):crops = 'Untagged';
		return crops