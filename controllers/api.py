from flask import Blueprint, render_template, request, session, redirect, jsonify, send_file
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json
from flask_cors import CORS,cross_origin
import base64
import sys
import random
from controllers.migrations import _main as migrations


app = Blueprint("api",__name__)
cors = CORS(app)

rapid= sqlite(c.SQLITE_DB)
# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
farm_details = None

class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg

	# @cross_origin()
	@app.route("/api/list_all_profile",methods=["POST","GET"])
	def list_all_profile():
		res = []
		dir_path = c.RECORDS+"/profiles/__temp__/"
		for path in os.listdir(dir_path):
			if os.path.isfile(os.path.join(dir_path, path)):
				if(path.find("@profile")>=0):
					# res.append(path)
					res.append(_main.profile_info_farmer(path))

		# res = migrations.excel_popu()
		res = res + migrations.excel_popu()
		random.shuffle(res)
		return jsonify(res)

	def profile_info_farmer(path):
		f = open(c.RECORDS+"/profiles/__temp__/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		# try:
		prof_1 = json.loads(json.loads(strsd))
		prof_1['addr_region'] = migrations.region_name_cleaner(prof_1['addr_region'])
		prof_1['farmer-primary_crop'] = migrations.crops_name_cleaner(prof_1['farmer-primary_crop'])
		prof_1['farmer_img_base64'] = ""
		prof_1['SOURCE'] = "MOBILE"

		USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ORDER BY `name` ASC; ".format(prof_1["USER_ID"]))
		if(len(USER)<=0):
			prof_1["input_by"] = {"name":"none"}
		else:
			prof_1["input_by"] = {}
			USER[0]["password"] = "CONFIDENTIAL"
			prof_1["input_by"] = USER[0]
		return prof_1
		# return json.dumps(json.dumps(prof_1))

	# @cross_origin()
	@app.route("/get_profile",methods=["POST","GET"]) # GET ONLY PROFILE FORM INFIO
	def get_profile():
		FILE = request.form["profile_file_name"]
		f = open(c.RECORDS+"/profiles/__temp__/"+ FILE, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		# try:
		prof_1 = json.loads(json.loads(strsd))
		prof_1['SOURCE'] = "MOBILE"
		prof_1['addr_region'] = migrations.region_name_cleaner(prof_1['addr_region'])
		prof_1['farmer-primary_crop'] = migrations.crops_name_cleaner(prof_1['farmer-primary_crop'])
		# prof_1['farmer_img_base64'] = "" # REMOVES BASE64 Data

		USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ORDER BY `name` ASC; ".format(prof_1["USER_ID"]))
		if(len(USER)<=0):
			prof_1["input_by"] = {"name":"none"}
		else:
			prof_1["input_by"] = {}
			USER[0]["password"] = "CONFIDENTIAL"
			prof_1["input_by"] = USER[0]
		return json.dumps(json.dumps(prof_1))


	@app.route("/get_full_profile_str",methods=["POST","GET"]) # GETS the Fulll data of Farmer
	def get_full_profile_str():
		FILE = request.form["profile_file_name"]
		f = open(c.RECORDS+"/profiles/__temp__/"+ FILE, "r")
		res = f.read()
		# res = json.loads(f.read())
		f.close()
		res_ = json.loads(json.loads(res))
		res_['SOURCE'] = "MOBILE"

		USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ORDER BY `name` ASC; ".format(res_["USER_ID"]))
		if(len(USER)<=0):
			res_["input_by"] = {"name":"none"}
		else:
			res_["input_by"] = {}
			USER[0]["password"] = "CONFIDENTIAL"
			res_["input_by"] = USER[0]
		return json.dumps(json.dumps(res_))

	@app.route("/get_sub_form_a",methods=["POST","GET"]) # GETS the Fulll data of Farmer
	def get_sub_form_a():
		FILE = request.form["subform"]
		print(FILE)
		f = open(c.RECORDS+"/profiles/__temp__/"+ FILE, "r")
		res = f.read()
		f.close()

		res_ = json.loads(json.loads(res))
		res_['SOURCE'] = "MOBILE"
		USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ORDER BY `name` ASC; ".format(res_["USER_ID"]))
		if(len(USER)<=0):
			res_["input_by"] = {"name":"none"}
		else:
			res_["input_by"] = {}
			USER[0]["password"] = "CONFIDENTIAL"
			res_["input_by"] = USER[0]

		return json.dumps(json.dumps(res_))

	# @cross_origin()
	@app.route("/api/get_imgProf/<ids>",methods=["POST","GET"]) # GET ONLY PROFILE FORM INFIO
	def get_imgProf(ids):
		f = open(c.RECORDS+"/profiles/__temp__/"+ ids, "r")
		prof__ = f.read()
		f.close()
		try:
			res = json.loads(prof__)
			return jsonify({"f_name":ids,"base_64":res["profile"]["farmer_img_base64"]})
		except Exception as e:
			return jsonify({"f_name":ids,"base_64":"../static/img/err_pic.png"})


	# @cross_origin()
	@app.route("/api/edit_user_acc",methods=["POST","GET"])
	def edit_user_acc():
		print("updating")
		u = request.form
		resp = rapid.do('''UPDATE `users` 
			SET `address`="{}",`email`="{}",`job`="{}",`mobile`="{}",`name`="{}",`password`="{}",`pcu`="{}",`rcu`="{}",`username`="{}"
			WHERE `id`={}
			;'''.format(u['address'],u['email'],u['job'],u['mobile'],u['name'],u['password'],u['pcu'],u['rcu'],u['username'],u['id']))
		return str(resp)

	# @cross_origin()
	@app.route("/get_user",methods=["POST","GET"])
	def get_user():
		resp = rapid.select("SELECT * FROM `users`;")
		return jsonify(resp)

	@app.route("/api/del_user",methods=["POST","GET"])
	def del_user():
		ids = request.form['id']
		resp = rapid.do("DELETE FROM `users` WHERE `id`={};".format(ids))
		return jsonify(resp)

	# @cross_origin()
	@app.route("/api/test",methods=["POST","GET"])
	@app.route("/api",methods=["POST","GET"])
	def test():
		# print(dict(request.headers))
		resp = {}
		resp = rapid.select("SELECT * FROM `SYSTEM_SETTINGS`;")
		resp[0]["DATABASE_PATH_WEB"] = c.SQLITE_DB
		f_v = open(c.M_APPVER+"app_version.txt","r")
		resp[0]["APP_VERSION"] = f_v.read()
		f_v.close()
		return jsonify(resp)

	@app.route("/api/index",methods=["POST","GET"])
	def api_index():
		return "api"

	@app.route("/api/get_asset_data",methods=["POST","GET"])
	def get_asset_data():
		_assets = open("assets/assets_01.txt").read().split("\n")
		# _assets = open("assets/init_data01.txt").read().split("\n")
		for ast in _assets:
			print(ast)
			rapid.do(ast.replace("\\","/"))
		return "api"

	@app.route("/api/conso",methods=["POST","GET"])
	def conso():
		_conso = {}
		profiled_area = {}
		farm_details = rapid.select("SELECT * FROM `farmer_details`")
		for farm in farm_details:
			if str(farm['State']).lower() in profiled_area:
				profiled_area.update({str(farm['State']).lower():profiled_area[str(farm['State']).lower()]+1})
			else:
				profiled_area.update({str(farm['State']).lower():1})

		profiled_assets = {}
		assets = rapid.select("SELECT * FROM `assets`")

		for asset in assets:
			if str(asset['Crop']).lower() in profiled_assets:
				if str(asset['State']).replace(" ","_").lower() in profiled_assets[str(asset['Crop']).lower()]:
					profiled_assets[str(asset['Crop']).lower()][str(asset['State']).replace(" ","_").lower()] = profiled_assets[str(asset['Crop']).lower()][str(asset['State']).replace(" ","_").lower()]+1
				else:
					profiled_assets[str(asset['Crop']).lower()].update({str(asset['State']).replace(" ","_").lower():1})
			else:
				profiled_assets.update({str(asset['Crop']).lower():{}})
		_conso.update({"profiled_area":profiled_area})
		_conso.update({"profiled_assets":profiled_assets})
		_conso.update({"profiles":farm_details})
		_conso.update({"assets":assets})
		return jsonify(_conso)
		# return str(_conso)

	# @cross_origin()
	@app.route("/api/user_register",methods=["POST","GET"])
	def user_register():
		reg_form = request.get_json()
		print(reg_form)
		row_name = ""
		row_value = ""
		for key, value in reg_form.items():
			row_name = row_name + "`"+key+"`,"
			row_value = row_value + "'"+value+"',"
			pass
		sql = "INSERT INTO `users`({}) VALUES ({})".format(row_name[:-1],row_value[:-1])
		sql_response = rapid.do(sql)
		print(sql)
		response = jsonify({"success":True,"status": "DONE","sql_response":sql_response})
		# response.headers.add('Access-Control-Allow-Origin', '*')
		return response

	# @cross_origin()
	@app.route("/api/login",methods=["POST","GET"])
	def login():
		login_form = request.get_json()
		sql_res = rapid.select("SELECT * FROM `users` WHERE `username`='{}' and `password`='{}';".format(login_form["username"],login_form["password"]))
		response = jsonify({"success":True,"status": "DONE","data":sql_res})
		# response.headers.add('Access-Control-Allow-Origin', '*')
		return response

	# @cross_origin()
	@app.route("/api/upload_data",methods=["POST","GET"])
	def upload_data():
		data = request.form['data']
		f_name = request.form['f_name']

		# --------------back-up------------
		back_up = open(c.RECORDS+"/profiles/__temp__/"+f_name+"", "w")
		back_up.write(json.dumps(data))
		back_up.close()
		# --------------end bacj-uP--------------

		response = jsonify({"success":True,"status": "DONE","data":None})
		FARMER_ID = f_name.split("@")
		# response.headers.add('Access-Control-Allow-Origin', '*')
		# try:
		# 	old_data = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "r");
		# 	old_data_read = old_data.read()
		# 	old_data.close()
		# except Exception as e:
		# 	old_data_read = "{}"
		# 	# f = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "w")
		# 	# f.write(json.dumps({}))
		# 	# f.close()
		# 	# raise e
		# print(type(old_data_read))
		# try:
		# 	old_data_read = json.loads(old_data_read)
		# 	old_data_read[FARMER_ID[1]] = json.loads(data)
		# except Exception as e:
		# 	# raise e
		# 	print(" * ERROR IN FORM : "+FARMER_ID[1])
		# 	return f_name

		# print(FARMER_ID[1])
		# f = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "w")
		# f.write(json.dumps(old_data_read))
		# f.close()
		return f_name

	@app.route("/api/download_zip_app",methods=["POST","GET"])
	def downloadFile ():
		#For windows you need to use drive name [ex: F:/Example.pdf]
		path = c.M_APPVER+"app-debug.apk"
		return send_file(path, as_attachment=True)
	# def download_zip_app():
	# 	from flask import Response # Changed line
	# 	import io
	# 	import zipfile
	# 	import time
	# 	FILEPATH = "app-debug.apk"
	# 	fileobj = io.BytesIO()
	# 	with zipfile.ZipFile(fileobj, 'w') as zip_file:
	# 		zip_info = zipfile.ZipInfo(FILEPATH)
	# 		zip_info.date_time = time.localtime(time.time())[:6]
	# 		zip_info.compress_type = zipfile.ZIP_DEFLATED
	# 		with open(FILEPATH, 'rb') as fd:
	# 			zip_file.writestr(zip_info, fd.read())
	# 	fileobj.seek(0)
	# 	f_v = open("app_version.txt","r")
	# 	__ver = f_v.read()
	# 	f_v.close()
	# 	# Changed line below
	# 	return Response(fileobj.getvalue(),
	# 					mimetype='application/zip',
	# 					headers={'Content-Disposition': 'attachment;filename=DTI_RAPID_MIS_'+__ver+'.apk'})



	@app.route("/api/todbdti",methods=["POST","GET"])
	def todbdti():
		data = json.loads(request.form["data"])
		table = request.form["table"]
		vals = ""
		fields = ""
		for datum in data:
			fields = fields + "`"+datum + "`,"
			vals = vals + '''"'''+str(data[datum]) + '''",'''
		sql = "INSERT INTO `dcf_{}` ({}) VALUES	({});".format(table,fields[:-1],vals[:-1])
		print(sql)
		rapid.do(sql)
		return "done"

	@app.route("/api/sql_test",methods=["POST","GET"])
	def sql_test():
		crops = ["Cacao","Coffee","Coconut","Banana","Calamansi","Jackfruit","Mango","Pili Nut","Other fruits and nuts"]

		for crop in crops:
			rapid.do('''
				INSERT INTO 
					`primary_crops`
					(`crop_name`) 
				VALUES
					("{}");
			'''.format(crop))
		return "done"

	@app.route("/lsprn",methods=["POST","GET"])
	def list_all_profile_new():
		res = []
		dir_path = c.RECORDS+"profiles/__temp__/"
		print(dir_path)
		for path in os.listdir(dir_path):
			if os.path.isfile(os.path.join(dir_path, path)):
				if(path.find("@profile")>=0):
					fr_s = open(dir_path+path,"r")
					raw_strs = fr_s.read()
					_data = json.loads(json.loads(raw_strs))
					fr_s.close()
					# # print(_data[])
					# print(type(_data))
					print(_data["farmer_name"])
					# return "0"
					res.append(path)

		print(len(res))
		return jsonify(res)
		
	@app.route("/migrate",methods=["POST","GET"])
	def migrate():
		res = []
		dir_path = c.RECORDS+"profiles/form_a/"
		print(dir_path)
		for path in os.listdir(dir_path):
			if os.path.isfile(os.path.join(dir_path, path)):
				fr_s = open(dir_path+path,"r")
				raw_strs = fr_s.read()
				try:
					_data = json.loads(raw_strs)
					fr_s.close()
					res.append(path)
				except:
					print("error : [{}]====\n{}".format(path,sys.exc_info()[0]))
					continue
				for datum in _data:
					# print(datum)
					__names_new = path.split(".json")[0]+"@"+datum
					# print(">>>>>>"+__names_new)
					new_data_lkasd = open(c.RECORDS+"/profiles/__temp__/"+__names_new+"", "w")
					new_data_lkasd.write(json.dumps(json.dumps(_data[datum])))
					new_data_lkasd.close()
					print(__names_new)

					if os.path.exists(dir_path+path):
						os.remove(dir_path+path)
						# print(dir_path+path)
						pass
					else:
						print("The file does not exist")

		lens_ = (len(res))

		res.append(lens_)
		return jsonify(res)
		