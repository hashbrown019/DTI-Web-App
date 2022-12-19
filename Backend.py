from modules.Connections import mysql,sqlite
from modules import Utility as util
import Configurations as c
import os
import json
from flask_cors import CORS,cross_origin
import base64
import sys
import random
from tqdm import tqdm
import warnings
import csv
import sys
import pandas as pd
# import threading
# from multiprocessing import Pool, Process
import asyncio

c.RECORDS=c.RECORDS_SERVER
c.SQLITE_DB=c.SQLITE_DB_SERVER
rapid= sqlite(c.SQLITE_DB)

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
	# res = excel_popu()
	# res = res + excel_popu()
	random.shuffle(res)
	return res

def profile_info_farmer(path):
	f = open(c.RECORDS+"/profiles/__temp__/"+ path, "r")
	strsd = f.read()
	f.close()
	prof_1 = "ERROR"
	prof_1 = json.loads(json.loads(strsd));
	prof_1['addr_region'] = region_name_cleaner(prof_1['addr_region'])
	prof_1['farmer-primary_crop'] = crops_name_cleaner(prof_1['farmer-primary_crop'])
	prof_1['farmer-fo_name_rapid']  = other_name_cleaner(prof_1['farmer-fo_name_rapid'])
	prof_1['farmer_dip_ref']  = other_name_cleaner(prof_1['farmer_dip_ref'])
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


# =========================================================
def thread_chunking(args):
	print(" ************* START thread_chunking")
	all_data  =  list_all_profile___()
	f = open(c.RECORDS+"/profiles/farmer_profile.json", "w")
	f.write(json.dumps(all_data))
	f.close()
	print(" ************* FINISHED thread_chunking")
	pass



def thread_chunking_append_excel(args):
	print(" ************* START thread_chunking appending excel_popu ")
	excel_popu()
	# f = open(c.RECORDS+"/profiles/farmer_profile.json", "r")
	# __data = json.loads(f.read())
	# f.close()

	# all_data = __data + excel_popu()
	# f = open(c.RECORDS+"/profiles/farmer_profile.json", "w")
	# f.write(json.dumps(all_data))
	# f.close()
	print(" ************* FINISHED thread_chunking appending excel_popu")
	pass

# ===============================================================
def init_excel_list_farmer():
	dir_path = c.RECORDS+"/spreadsheets/"
	f = open(c.RECORDS+"/profiles/farmer_profile_EXCEL_LIST.json", "w")
	f.write(json.dumps(os.listdir(dir_path)))
	f.close()

def excel_popu():
	FROM_EXCEL_RPOFILES = []
	loads_ = tqdm(os.listdir(dir_path))
	for path in loads_:
		PATH__ = os.path.join(dir_path, path)
		loads_.desc = path
		if os.path.isfile(PATH__):
			if PATH__.find("._DELETED_FILE_")<0:	
				# print(PATH__)
				file_name =  PATH__ # path to file + file name
				# file_name =  c.RECORDS+"/spreadsheets/93#2022-09-19#NSAMAR_vc_a_1.xlsx" # path to file + file name
				sheet =  "VC FORM A" # sheet name or sheet number or list of sheet numbers and names
				try:
					df = pd.read_excel(io=file_name, sheet_name=sheet, engine='openpyxl')
				except Exception as e:
					print(" * Error in [{}] :: {}".format(path,e))
					continue

				EXCEL_DATA = df.iterrows()

				_result = {} 
				LLL = dict(EXCEL_DATA)
				for key in (LLL):
					_result[key] = [] 
					for val in LLL[key]:
						_result[key].append(val)
				del _result[0]

				f = open(c.RECORDS+"/profiles/farmer_profile_EXCEL.json", "r")
				__data = json.loads(f.read())
				f.close()

				__data.append(append_data_excel_mdata(_result,path))
				f = open(c.RECORDS+"/profiles/farmer_profile_EXCEL.json", "w")
				f.write(json.dumps(__data))
				f.close()
				# FROM_EXCEL_RPOFILES = FROM_EXCEL_RPOFILES + append_data_excel_mdata(_result,path)

	return (FROM_EXCEL_RPOFILES)
	# return jsonify(FROM_EXCEL_RPOFILES)



def append_data_excel_mdata(datas,path):
	farmer_from_excel = []
	# datas = (excel_popu())
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

		_farmer[40] = region_name_cleaner(_farmer[40])
		_farmer[47] = crops_name_cleaner(_farmer[47])

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
			'farmer-fo_name_rapid': other_name_cleaner(_farmer[32]),
			'farmer_dip_ref': other_name_cleaner(_farmer[27])
		})
	# return str(len(datas))
	return farmer_from_excel

def region_name_cleaner(region):
	region = str(region)
	roman_numerals = ["i","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii","xiii"]
	num_digits = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
	region = region.lower()
	region = region.replace(" ","")
	region = region.replace("caraga","13")
	region = region.replace("car","13")
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
	crops = str(crops);
	crops = crops.lower();
	crops = crops.replace(" ","");
	if(crops==""):crops = 'Untagged';
	return crops

# THIS FUNCTION FIX THE crops name with SIMILAR AREA
def other_name_cleaner(strs):
	strs = str(strs);
	strs = strs.lower();
	strs = strs.replace("  "," ");
	strs = strs.replace(" - ","-");
	strs = strs.replace(" -","-");
	strs = strs.replace("- ","-");
	if(strs==""):strs = 'Untagged';
	return strs.upper();



 
n = (sys.argv[1])
if(n==None):
	print(" * No Argument defined")
if(n=="mobile"):
	thread_chunking(1)
if(n=="excel"):
	thread_chunking_append_excel(1)
if(n=="excel_list_init"):
	init_excel_list_farmer()