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

c.RECORDS=c.RECORDS_SERVER
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
					res.append(profile_info_farmer(path))
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

def thread_chunking(args):
	print(" ************* START thread_chunking")
	all_data  =  list_all_profile___()
	f = open(c.RECORDS+"/profiles/farmer_profile.json", "w")
	f.write(json.dumps(all_data))
	f.close()
	print(" ************* FINISHED thread_chunking")
	pass

list_all_profile___()