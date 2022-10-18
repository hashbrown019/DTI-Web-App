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
from tqdm import tqdm

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
		return _main.list_all_profile___();

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
		return jsonify(res)

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

