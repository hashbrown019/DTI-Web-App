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
	@app.route("/list_all_profile",methods=["POST","GET"])
	def list_all_profile():
		res = []
		dir_path = c.RECORDS+"/profiles/form_a/"
		for path in os.listdir(dir_path):
			if os.path.isfile(os.path.join(dir_path, path)):
				res.append(path)
		return jsonify(res)


	# @cross_origin()
	@app.route("/get_profile",methods=["POST","GET"])
	def get_profile():
		FILE = request.form["profile_file_name"]
		f = open(c.RECORDS+"/profiles/form_a/"+ FILE, "r")
		res = json.loads(f.read())
		f.close()
		return jsonify(res)

	# @cross_origin()
	@app.route("/api/test",methods=["POST","GET"])
	@app.route("/api",methods=["POST","GET"])
	def test():
		# print(dict(request.headers))
		resp = {}
		resp = rapid.select("SELECT * FROM `SYSTEM_SETTINGS`;")
		resp[0]["DATABASE_PATH_WEB"] = c.SQLITE_DB
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
		print(type(old_data_read))
		try:
			old_data_read = json.loads(old_data_read)
			old_data_read[FARMER_ID[1]] = json.loads(data)
		except Exception as e:
			# raise e
			print(" * ERROR IN FORM : "+FARMER_ID[1])
			return f_name

		print(FARMER_ID[1])
		f = open(c.RECORDS+"/profiles/form_a/"+ FARMER_ID[0]+".json", "w")
		f.write(json.dumps(old_data_read))
		f.close()
		return f_name

	@app.route("/api/sql_test",methods=["POST","GET"])
	def sql_test():
		_file = open("assets/records/fo.json",'r')
		cont_ = json.loads(_file.read())
		_file.close()
		for key1 in cont_:
			for key2 in cont_[key1]:
				for fo in cont_[key1][key2]:
					print("{} : {} -- {}".format(key1,key2,fo))
					rapid.do('''
						INSERT INTO 
							`fo_list`
							(`fo_name`,`pcu`, `rcu` ) 
						VALUES
							("{}","{}","{}");
					'''.format(key1,key2,fo))
		return jsonify(cont_)

	# =============================================================================================
	# @cross_origin()
	@app.route("/api/res",methods=["POST","GET"])
	def res():
		_AA = [3,6,10,13,17,19,21,23,26,28,29,37,39,42,48,50,52,55,56,62,64,65]
		_IA = [16,31,32,34,41,45,47,57,58,59,60]
		_PEA= [2,5,7,11,12,15,20,22,24,25,27,30,33,36,38,43,49,51,53]
		_SA = [1,4,8,9,14,18,35,40,44,46,54,61,63]

		content = request.form["DATA"]
		_cont = json.loads(content)
		# print(_cont)
		tests = _cont["tests"].keys()
		shh =  _cont["tests"]
		print(tests)
		acd = dict({
			"_AA":0,
			"_IA":0,
			"_PEA":0,
			"_SA":0
		})

		for kkk in tests:
			try:
				if(kkk.split("_")[1] in _AA): pass
			except Exception as e:
				print("SKIPPING ITEM : {}".format(e))
				continue
				# raise e
			if(int(kkk.split("_")[1]) in _AA):					
				acd["_AA"] = acd["_AA"] + int(shh[kkk]);print("_AA")
			elif(int(kkk.split("_")[1]) in _IA):				
				acd["_IA"] = acd["_IA"] + int(shh[kkk]);print("IA")
			elif(int(kkk.split("_")[1]) in _PEA):				
				acd["_PEA"] = acd["_PEA"] + int(shh[kkk]);print("_PEA")
			elif(int(kkk.split("_")[1]) in _SA):				
				acd["_SA"] = acd["_SA"] + int(shh[kkk]);print("_SA")

		print(acd)
		gran_total = acd["_SA"] + acd["_PEA"] +acd["_IA"] +acd["_AA"]

		humms = ((acd["_PEA"] + acd["_SA"])/gran_total )* 100
		stem = ((acd["_AA"] + acd["_IA"])/gran_total )* 100
		abm = ((acd["_IA"] +acd["_SA"])/gran_total )* 100
		gas = ((acd["_AA"] + acd["_SA"])/gran_total )* 100

		acd = {
			"_humss":math.ceil(humms),
			"_stem":math.ceil(stem),
			"_abm":math.ceil(abm),
			"_gas":math.ceil(gas),
		}
		return jsonify(acd)