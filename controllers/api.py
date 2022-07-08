from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connections import mysql,sqlite
import Configurations as c
import os
import json
from flask_cors import CORS,cross_origin


app = Blueprint("api",__name__)
cors = CORS(app)

# rapid = sqlite
rapid= sqlite(c.SQLITE_DB)
# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)

farm_details = None

class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg


	# @cross_origin()
	@app.route("/api/test")
	@app.route("/api")
	def test():
		print(request.get_json())
		# response.headers.add('Access-Control-Allow-Origin', '*')
		return "Test Complete | Data base Used : "+ SQLITE_DB


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
		response = jsonify({"success":True,"status": "DONE","data":None})
		FARMER_ID = f_name.split("@")
		# response.headers.add('Access-Control-Allow-Origin', '*')
		try:
			old_data = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "r");
			old_data_read = old_data.read()
			old_data.close()
		except Exception as e:
			old_data_read = "{}"
			# f = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "w")
			# f.write(json.dumps({}))
			# f.close()
			# raise e
		

		old_data_read = json.loads(old_data_read)
		old_data_read[FARMER_ID[1]] = json.loads(data)

		print(FARMER_ID[1])
		f = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "w")
		f.write(json.dumps(old_data_read))
		f.close()
		return f_name

