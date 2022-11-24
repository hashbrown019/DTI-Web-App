from flask import Blueprint, render_template, request, session, redirect, jsonify, send_file, Response
from flask_session import Session
from modules.Connections import mysql,sqlite
from modules import Utility as util
import Configurations as c
import os
import json
from flask_cors import CORS,cross_origin
import base64
import sys
import random
from controllers.migrations import _main as migrations
from tqdm import tqdm
# import threading
# from multiprocessing import Pool, Process
import asyncio

app = Blueprint("apiV2",__name__)
cors = CORS(app)

rapid= sqlite(c.SQLITE_DB)
# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
farm_details = None

FARMER_PROFILE_LS = None

class _main:
	def __init__(self, arg):
		super(_main, self).__init__();
		print(" * STARTING API V2")
		self.arg = arg;
		
	@app.route("/api/v2/global_",methods=["POST","GET"])
	def global_():
		return FARMER_PROFILE_LS;

	@app.route("/api/v2/list_all_profile",methods=["POST","GET"])
	def list_all_profile():
		return jsonify(_main.list_all_profile___());

	def list_all_profile___():
		res = []
		dir_path = c.RECORDS+"/profiles/__temp__/";
		_title = "----";
		loads_ = tqdm(os.listdir(dir_path),  desc =_title,ascii ="►>○•|█");
		for path in loads_:
			if os.path.isfile(os.path.join(dir_path, path)):
				if(path.find("@profile")>=0):
					loads_.desc = " * "+path
					# res.append(path)
					try:
						res.append(_main.profile_info_farmer(path))
						pass
					except Exception as e:
						print(e)
		# res = migrations.excel_popu()
		res = res + migrations.excel_popu()
		random.shuffle(res)
		return res

	def profile_info_farmer(path):
		f = open(c.RECORDS+"/profiles/__temp__/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['addr_region'] = migrations.region_name_cleaner(prof_1['addr_region'])
		prof_1['farmer-primary_crop'] = migrations.crops_name_cleaner(prof_1['farmer-primary_crop'])
		prof_1['farmer-fo_name_rapid']  = migrations.other_name_cleaner(prof_1['farmer-fo_name_rapid'])
		prof_1['farmer_dip_ref']  = migrations.other_name_cleaner(prof_1['farmer_dip_ref'])
		prof_1['farmer_img_base64'] = "";
		prof_1['SOURCE'] = "MOBILE";

		USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ORDER BY `name` ASC; ".format(prof_1["USER_ID"]))
		if(len(USER)<=0):
			prof_1["input_by"] = {"name":"none"}
		else:
			prof_1["input_by"] = {}
			USER[0]["password"] = "CONFIDENTIAL"
			prof_1["input_by"] = USER[0]
		return prof_1


	@app.route("/api/v2/create_dash_for_all",methods=["POST","GET"])
	def create_dash_for_all():
		data  = json.loads(_main.get_alldata_from_shrink_data_file())
		return data[0]
		for x in data[0]:
			print((x))

		return str(data)
		# return jsonify(data)

# ================================================================================
	@app.route("/api/v2/set_data_return",methods=["POST","GET"])
	def set_data_return():
		d_r = json.loads(request.data, strict=False)
		f = open(c.RECORDS+"/profiles/DASH_RETURN_DATA.json", "w")
		f.write(json.dumps(d_r))
		f.close()
		return "DONE"
		# return jsonify(data)

	@app.route("/api/v2/get_data_return",methods=["POST","GET"])
	def get_data_return():
		chunck_farmer_profile = c.RECORDS+"/profiles/DASH_RETURN_DATA.json"
		file_stats = os.stat(chunck_farmer_profile)
		f = open(chunck_farmer_profile, "r")
		all_data = f.read()
		f.close()
		resp = Response(all_data)
		resp.headers['Content-Length'] = file_stats.st_size
		resp.headers['X-File-Length'] = file_stats.st_size
		resp.headers['total'] = file_stats.st_size
		return resp

# ================================================================================
	
	async def thread_chunking(args):
		print(" ************* START thread_chunking")
		all_data  = await _main.list_all_profile___()
		f = open(c.RECORDS+"/profiles/farmer_profile.json", "w")
		f.write(json.dumps(all_data))
		f.close()
		print(" ************* FINISHED thread_chunking")
		pass

	@app.route("/api/v2/set_farmer_chunk_data",methods=["POST","GET"])
	def set_farmer_chunk_data():
		# t1 = threading.Thread(target=_main.thread_chunking, args=(10,))
		# t1.start()
		# with Pool(1) as p:
		# 	print(p.map(_main.thread_chunking, "args"))
		asyncio.run(_main.thread_chunking(1))
		# p = Process(target=_main.thread_chunking, args=('bob',))
		# p.start()
		# t1.join() #FOR WAITING FINISHE THREAD
		# all_data  = _main.list_all_profile___()
		# f = open(c.RECORDS+"/profiles/farmer_profile.json", "w")
		# f.write(json.dumps(all_data))
		# f.close()
		return "Done"

	@app.route("/api/v2/get_farmer_chunk_data",methods=["POST","GET"])
	def get_farmer_chunk_data():
		chunck_farmer_profile = c.RECORDS+"/profiles/farmer_profile.json"
		file_stats = os.stat(chunck_farmer_profile)
		all_data = _main.get_alldata_from_shrink_data_file()
		resp = Response(all_data)
		resp.headers['Content-Length'] = file_stats.st_size
		resp.headers['X-File-Length'] = file_stats.st_size
		resp.headers['total'] = file_stats.st_size
		return resp

	@app.route("/api/v2/farmer_chunk_data_date",methods=["POST","GET"])
	def farmer_chunk_data_date():
		import datetime, time
		file_dm = datetime.datetime.fromtimestamp(util.file_creation_date(c.RECORDS+"/profiles/farmer_profile.json"))
		date_now = datetime.datetime.now()
		time_diff = (date_now-file_dm)
		data = {"file_dm":str(file_dm).split(".")[0],"time_diff":str(time_diff).split(".")[0]}
		return (data)
		
# ================================================================================

	def get_alldata_from_shrink_data_file():
		chunck_farmer_profile = c.RECORDS+"/profiles/farmer_profile.json"
		f = open(chunck_farmer_profile, "r")
		all_data = f.read()
		f.close()
		return all_data

	@app.route("/api/v2/get_all_primary_crops",methods=["POST","GET"])
	def get_all_primary_crops():
		res = rapid.select("SELECT * FROM `primary_crops`;")
		return jsonify(res)

	@app.route("/api/v2/get_all_fo",methods=["POST","GET"])
	def get_all_fo():
		res = rapid.select("SELECT `rcu` FROM `fo_list`;")
		return jsonify(res)


# ================================================================================


	@app.route("/api/v2/sample",methods=["POST","GET"])
	def v2_sample():
		complete_col = {}
		res = []
		res_ls = {}
		dir_path = c.RECORDS+"/profiles/__temp__/";
		_title = "----";
		loads_ = tqdm(os.listdir(dir_path),  desc =_title,ascii ="►>○•|█");
		sample = 0
		temp = ""
		full_prof ={}
		for path in loads_:
			if os.path.isfile(os.path.join(dir_path, path)):
				# if(path.find("@profile")>=0):

				loads_.desc = " * "+path
				# res.append(path)
				prefix = path.split("@")[1]
				f_id = path.split("@")[0]
				fff = open(c.RECORDS+"/profiles/__temp__/"+ path, "r")
				strsd = fff.read()
				fff.close()
				prof_1 = json.loads(json.loads(strsd)); 
				if(f_id not in res_ls):res_ls[f_id] = {}
				for key in prof_1:
					if(key == 'farmer_img_base64'):prof_1[key]= "HIDDEN";
					if(key == 'post_harv-photo'):prof_1[key]= "HIDDEN";
					if(key == 'farm-photo'):prof_1[key]= "HIDDEN";
					res_ls[f_id]["{}__{}".format(prefix,key)] = prof_1[key]

					complete_col["{}__{}".format(prefix,key)] = {}


				if(sample >=10):
					return jsonify(res_ls)
				sample = sample + 1

		# return jsonify(complete_col)
		# # return jsonify(res_ls)