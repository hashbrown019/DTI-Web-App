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
import warnings
warnings.filterwarnings('ignore')

app = Blueprint("migrations",__name__)
cors = CORS(app)

rapid= sqlite(c.SQLITE_DB)

mysqldb = mysql(c._HOST,c._USER,c._PASSWORD,c._DATABASE)

FORM_A_LS = [
	{"file":"profile" , "label":"Farmer Basic Info" },
	{"file":"add_farm" , "label":"Farm Information" },
	{"file":"hh_profile" , "label":"Household Profiles" },
	{"file":"prod_cost" , "label":"Production Cost" },
	{"file":"workers_laborers" , "label":"Farm Workers and Labors" },
	{"file":"post_harvest" , "label":"Post Harvest" },
	{"file":"marketing_sales" , "label":"Marketing/Sales Distribution Channels" },
	{"file":"access_financial" , "label":"Access to Financial Services and Products" },
	{"file":"feedback" , "label":"Industry Feedback" },
]

class _main:
	@app.route("/migrationtest",methods=["POST","GET"])
	def migrationtest():
		resp = "database : {}".format(str(mysqldb.select("SELECT VERSION()") ))
		note = resp + " || end DB"
		print(note)
		return note


	@app.route("/migrations/export_excel",methods=["POST","GET"])
	def export_excel():
		print("===========================")
		ls = json.loads(request.form["ls"])
		ids = request.form["ls"]
		res = []
		dir_path = c.RECORDS+"/profiles/__temp__/"

		data_fr = pd.DataFrame(columns = ["profile__farmer_code","profile__is_synced","profile__datetime","profile__farmer_img_base64","profile__f_name","profile__m_name","profile__l_name","profile__ext_name","profile__farmer_name","profile__farmer_sex","profile__farmer-number","profile__farmer-email","profile__farmer-bday","profile__farmer-is_bday_sure","profile__farmer-age","profile__farmer-civil_status","profile__farmer-marital_partner_name","profile__farmer-head_of_house","profile__farmer-name_head_hh","profile__farmer-relation_head_hh","profile__farmer_sex_head_hh","profile__farmer-ihead-hh-s_pwd","profile__farmer-ihead-hh-s_ofw","profile__farmer-ihead-hh-s_ip","profile__farmer-ihead-hh-p","profile__farmer-coords_long","profile__farmer-coords_lat","profile__addr_region","profile__addr_prov","profile__addr_city","profile__addr_brgy","profile__addr_street_purok_sitio","profile__farmer-primary_crop","profile__farmer_dip_ref","profile__farmer-is_pwd","profile__farmer-is_ofw","profile__farmer-is_ip","profile__farmer-ip","profile__farmer-yearsfarming","profile__farmer-fo_name_rapid","profile__farmer-fo_position","profile__farmer-fo_designation","profile__farmer-fo_member_since","profile__farmer-rsbsa","profile__farmer-highest_education","profile__farmer-vocational","profile__form-remarks","profile__USER_ID","profile__farm-photo","profile__post_harv-photo","add_farm__farmer_code","add_farm__is_synced","add_farm__datetime","add_farm__farm-photo","add_farm__farmer-coords_long","add_farm__farmer-coords_lat","add_farm__addr_region","add_farm__addr_prov","add_farm__addr_city","add_farm__addr_brgy","add_farm__addr_street_purok_sitio","add_farm__farm-declare_area","add_farm__farm-is_multi_crop","add_farm__farm-primary_crop","add_farm__farm-others_crops","add_farm__farm-slope_hectars","add_farm__farm-palin_hectares","add_farm__farm-bearing_plants","add_farm__farm-non_bearing_plants","add_farm__farm-tenurial_so","add_farm__farm-tenurial_co","add_farm__farm-tenurial_cloa","add_farm__farm-tenurial_stew","add_farm__farm-tenurial_Usfruc","add_farm__farm-tenurial_ten","add_farm__farm-tenurial_others","add_farm__farm-total_no_tenurial_lots","add_farm__farm-primary_crop_av_prof_vol","add_farm__farm-primary_crop_total_land_area","add_farm__farm-primary_crop_cycle_year","add_farm__farm-secondary_crop","add_farm__farm-secondary_crop_av_prod_vol","add_farm__farm-secondary_crop_total_land_area","add_farm__farm-secondary_crop_cycle_year","add_farm__farm-area_land_expansion_slope","add_farm__farm-area_land_expasnion_flat","add_farm__farm-area_land_rehab_slope","add_farm__farm-area_land_rehab_flat","add_farm__form-remarks","add_farm__USER_ID","add_farm__post_harv-photo","add_farm__farmer_img_base64","hh_profile__farmer_code","hh_profile__is_synced","hh_profile__datetime","hh_profile__hh-total_hh_mem_0_17_m","hh_profile__hh-total_hh_mem_0_17_f","hh_profile__hh-total_hh_mem_18_30_m","hh_profile__hh-total_hh_mem_18_30_f","hh_profile__hh-total_hh_mem_31_59_m","hh_profile__hh-total_hh_mem_31_59_f","hh_profile__hh-total_hh_mem_60_up_m","hh_profile__hh-total_hh_mem_60_up_f","hh_profile__hh-mem_pwd_m","hh_profile__hh-mem_pwd_f","hh_profile__hh-mem_ofw_m","hh_profile__hh-mem_ofw_f","hh_profile__hh-mem_ip_m","hh_profile__hh-mem_ip_f","hh_profile__hh-est_total_income_primary_crop","hh_profile__hh-est_total_income_secondary_crop","hh_profile__hh-est_total_income_livestock","hh_profile__hh-non_farm_remittance","hh_profile__hh-non_farm_income_employment","hh_profile__hh-non_farm_income_skilled","hh_profile__hh-non_farm_income_business","hh_profile__hh-non_farm_income_pension","hh_profile__hh-non_farm_income_pantawid","hh_profile__hh-non_farm_income_others","hh_profile__hh-rsbsa_no","hh_profile__form-remarks","hh_profile__USER_ID","hh_profile__farm-photo","hh_profile__post_harv-photo","hh_profile__farmer_img_base64","prod_cost__farmer_code","prod_cost__is_synced","prod_cost__datetime","prod_cost__prodcost-is_keep_record","prod_cost__prodcost-crop_cycle_year","prod_cost__prodcost-labor_land_dev_prep","prod_cost__prodcost-labor_crop_maintenance_act","prod_cost__prodcost-labor_crop_harvest","prod_cost__prodcost-labor_post_harvest_act","prod_cost__prodcost-materials_land_dev_prep","prod_cost__prodcost-materials__act","prod_cost__prodcost-crop_harvest","prod_cost__prodcost-post_harvest_act","prod_cost__form-remarks","prod_cost__USER_ID","prod_cost__farm-photo","prod_cost__post_harv-photo","prod_cost__farmer_img_base64","workers_laborers__farmer_code","workers_laborers__is_synced","workers_laborers__datetime","workers_laborers__workers-fam_isfarmer","workers_laborers__workers-fam_isyouth","workers_laborers__workers-isfarmer","workers_laborers__workers-fam_srcitizen","workers_laborers__workers-fam_ispwd","workers_laborers__workers-fam_isofw","workers_laborers__workers-fam_is_ip","workers_laborers__workers-fam_total_male","workers_laborers__workers-fam_num_youth_m","workers_laborers__workers-fam_num_sr","workers_laborers__workers-fam_num_pwd","workers_laborers__workers-fam_num_ofw","workers_laborers__workers-fam_num_ip","workers_laborers__workers-fam_ls_ip","workers_laborers__workers-fam_year_salary_male","workers_laborers__workers-fam_total_female","workers_laborers__workers-fam_num_youth_f","workers_laborers__workers-fam_num_ip_f","workers_laborers__workers-fam_num_pwd_f","workers_laborers__workers-fam_num_ofw_f","workers_laborers__workers-fam_ls_ip_f","workers_laborers__workers-fam_year_salary_female","workers_laborers__workers-non_fam_isfarmer","workers_laborers__workers-non_fam_isyouth","workers_laborers__workers-non_fam_srcitizen","workers_laborers__workers-non_fam_pwd","workers_laborers__workers-non_fam_ofw","workers_laborers__workers-non_fam_is_ip","workers_laborers__workers-non_fam_total_male","workers_laborers__workers-non_fam_num_youth","workers_laborers__workers-non_fam_num_sr","workers_laborers__workers-non_fam_num_pwd","workers_laborers__workers-non_fam_num_ofw","workers_laborers__workers-non_fam_num_ip","workers_laborers__workers-non_fam_ls_ip","workers_laborers__workers-non_fam_year_salary_male","workers_laborers__workers-non_fam_total_female","workers_laborers__workers-non_fam_num_youth_f","workers_laborers__workers-non_fam_num_sr_f","workers_laborers__workers-non_fam_num_pwd_f","workers_laborers__workers-non_fam_num__ofw_f","workers_laborers__workers-non_fam_num_ip_f","workers_laborers__workers-non_fam_ls_ip_f","workers_laborers__workers-non_fam_year_salary_female","workers_laborers__form-remarks","workers_laborers__USER_ID","workers_laborers__farm-photo","workers_laborers__post_harv-photo","workers_laborers__farmer_img_base64","post_harvest__record_num","post_harvest__record_duplicate_id","post_harvest__farmer_code","post_harvest__is_synced","post_harvest__datetime","post_harvest__post_harv-type_faci_equip","post_harvest__post_harv-type_faci_equip_name","post_harvest__farmer-coords_long","post_harvest__farmer-coords_lat","post_harvest__addr_region","post_harvest__addr_prov","post_harvest__addr_city","post_harvest__addr_brgy","post_harvest__addr_street_purok_sitio","post_harvest__post_harv-ph_product_form","post_harvest__post_harv-phcropothers","post_harvest__post_harv-capacity","post_harvest__post_harv-capacity_unit","post_harvest__post_harv-capacity_unit_time","post_harvest__post_harv-photo","post_harvest__form-remarks","post_harvest__USER_ID","post_harvest__farm-photo","post_harvest__farmer_img_base64","marketing_sales__record_num","marketing_sales__farmer_code","marketing_sales__is_synced","marketing_sales__datetime","marketing_sales__market-primary_crop_type","marketing_sales__market-primary_vol_del","marketing_sales__market-is_coop","marketing_sales__market-is_sme","marketing_sales__market-is_anchor_firm","marketing_sales__market-is_negosyo_center","marketing_sales__market-is_others","marketing_sales__market-name_coop","marketing_sales__market-name_sme","marketing_sales__market-name_anchor_firm","marketing_sales__market-name_others","marketing_sales__market-primary_crop_dist_point","marketing_sales__market-primary_crop_dist_others","marketing_sales__market-primary_crop_type_buyer","marketing_sales__market-primary_crop_buyer_others","marketing_sales__market-primary_crop_product_fgp","marketing_sales__market-primary_crop_product_fgp_unit","marketing_sales__form-remarks","marketing_sales__USER_ID","marketing_sales__farm-photo","marketing_sales__post_harv-photo","marketing_sales__farmer_img_base64","access_financial__farmer_code","access_financial__is_synced","access_financial__datetime","access_financial__financial-is_loan","access_financial__financial-is_primary_crop_distribution","access_financial__financial-if_loan_bank","access_financial__financial-loan_govbank_name","access_financial__financial-loan_govbank_type","access_financial__financial-loan_private_name","access_financial__financial-loan_private_type","access_financial__financial-if_loan_non_bank","access_financial__financial-loan_name_fo","access_financial__financial-loan_type_fo","access_financial__financial-loan_name_ngo","access_financial__financial-loan_type_ngo","access_financial__financial-loan_name_lending","access_financial__financial-loan_type_lending","access_financial__financial-loan_if_nonbank_others","access_financial__financial-loan_name_others","access_financial__financial-loan_type_others","access_financial__financial-is_crop_deposit","access_financial__financial-type_deposit","access_financial__financial-type_deposit_bank","access_financial__financial-type_deposit_non_bank","access_financial__financial-is_crop_insurance","access_financial__financial-type_insurance","access_financial__financial-type_insurance_bank","access_financial__financial-type_insurance_non_bank","access_financial__financial-is_crop_payments","access_financial__financial-type_payments","access_financial__financial-type_payments_bank","access_financial__financial-type_payments_non_bank","access_financial__financial-is_remmitances","access_financial__financial-type_remmittance_name","access_financial__financial-is_crop_others","access_financial__financial-type_others_bank","access_financial__financial-type_others_non_bank","access_financial__form-remarks","access_financial__USER_ID","access_financial__farm-photo","access_financial__post_harv-photo","access_financial__farmer_img_base64","feedback__record_num","feedback__farmer_code","feedback__is_synced","feedback__datetime","feedback__feedback-num_of_trainings_2_3_years","feedback__farmer-Cacao","feedback__farmer-Coffee","feedback__farmer-Coconut","feedback__farmer-Banana","feedback__farmer-Calamansi","feedback__farmer-Jackfruit","feedback__farmer-Mango","feedback__farmer-Pili_Nut","feedback__farmer-Other_fruits_nuts","feedback__farmer-Others","feedback__feedback-cert_acquired","feedback__feedback-support_need","feedback__feedback[]-media","feedback__feedback[]-freq","feedback__feedback-type_mobile","feedback__feedback-commnets","feedback__feedback-remarks","feedback__USER_ID","feedback__farm-photo","feedback__post_harv-photo","feedback__farmer_img_base64"])

		# for path in os.listdir(dir_path):
		for path in ls:
			ffname = path
			farmer_DATA = {}
			for form_ in FORM_A_LS:
				file_ind_name = ffname+"@"+form_['file']
				if(os.path.isfile(c.RECORDS+"/profiles/__temp__/"+file_ind_name)):
					f = open(c.RECORDS+"/profiles/__temp__/"+file_ind_name, "r")
					strsd = f.read()
					f.close()
					# try:
					prof_1 = json.loads(json.loads(strsd))
					prof_1["farm-photo"] = ""
					prof_1["post_harv-photo"] = ""
					prof_1["farmer_img_base64"] = ""
					for keys in prof_1:
						# print(form_['file']+"__"+keys)
						farmer_DATA[form_['file']+"__"+keys] = prof_1[keys]
				else:
					# print("Not_found >>> "+ file_ind_name)
					pass
			data_fr.append(pd.DataFrame(farmer_DATA),ignore_index = True)
			# print(farmer_DATA)
			print(ffname)
			print("===========================")
				# res.append(_main.profile_info_farmer(path))
		# writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')
		data_fr.append({"profile__farmer_code":"haaaays"},ignore_index = True)
		writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
		print(pd)
		data_fr.to_excel(writer, sheet_name='Mobile Data', index=False)
		writer.save()
		return ("===========CREATING EXCEL FINISH================")

	def profile_info_farmer(path,form):
		f = open(c.RECORDS+"/profiles/__temp__/"+ path+"@"+form, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		# try:
		prof_1 = json.loads(json.loads(strsd))
		prof_1['addr_region'] = migrations.region_name_cleaner(prof_1['addr_region'])
		prof_1['farmer-primary_crop'] = migrations.crops_name_cleaner(prof_1['farmer-primary_crop'])
		prof_1['farmer-fo_name_rapid']  = migrations.other_name_cleaner(prof_1['farmer-fo_name_rapid'])
		prof_1['farmer_dip_ref']  = migrations.other_name_cleaner(prof_1['farmer_dip_ref'])
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
				'farmer-fo_name_rapid': _main.other_name_cleaner(_farmer[32]),
				'farmer_dip_ref': _main.other_name_cleaner(_farmer[27])
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
	# THIS FUNCTION FIX THE crops name with SIMILAR AREA
	def other_name_cleaner(strs):
		strs = str(strs)
		strs = strs.lower()
		strs = strs.replace("  "," ")
		strs = strs.replace(" - ","-")
		strs = strs.replace(" -","-")
		strs = strs.replace("- ","-")
		if(strs==""):strs = 'Untagged';
		return strs.upper()