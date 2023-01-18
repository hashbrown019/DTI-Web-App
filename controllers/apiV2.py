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
import compress_json
import gzip

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

	@app.route("/api/v2/set_data_return_")
	def set_data_return_():
		return _main.set_data_return()

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
	
	def thread_chunking(args):
		print(" ************* START thread_chunking")
		all_data  =  _main.list_all_profile___()
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
		# asyncio.run(_main.thread_chunking(1))
		_main.thread_chunking(1)
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

		# resp = Response(all_data)
		# resp.headers['Content-Length'] = file_stats.st_size
		# resp.headers['X-File-Length'] = file_stats.st_size
		# resp.headers['total'] = file_stats.st_size

		content = gzip.compress(all_data.encode('utf8'), 5)
		resp = Response(content)
		print(len(content)/1000000)
		resp.headers['Content-Length'] = file_stats.st_size
		resp.headers['X-File-Length'] = file_stats.st_size
		resp.headers['total'] = file_stats.st_size
		resp.headers['Content-Encoding'] = 'gzip'
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


	@app.route("/api/v2/excel_export_a_mobile/<region>/<entry>",methods=["POST","GET"])
	def excel_export_a_mobile(region,entry):
		region = region.replace("_"," ").upper()
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
				
				# res.append(path)
				prefix = path.split("@")[1]
				f_id = path.split("@")[0]

				fff = open(c.RECORDS+"/profiles/__temp__/"+ path, "r")
				strsd = fff.read()
				fff.close()
				# print(prof_1['farmer_code'])
				try:
					prof_1 = json.loads(json.loads(strsd));
				except Exception as e:
					print("Skipping Profiles : Error in Farmer Data Structure || " +path)

				USER = rapid.select("SELECT * from `users` WHERE `id`={} ;".format(prof_1['USER_ID']))
				if(len(USER)!=0):
					if(USER[0]['rcu']==region):
						loads_.desc = "Profiles : ["+str(sample)+"] || "+path
						if(prof_1['farmer_code']==" " or prof_1['farmer_code']=="" ):
							continue

						if(f_id not in res_ls):res_ls[f_id] = {}
						for key in prof_1:
							if(key == 'farmer_img_base64'):prof_1[key]= "HIDDEN";
							if(key == 'post_harv-photo'):prof_1[key]= "HIDDEN";
							if(key == 'farm-photo'):prof_1[key]= "HIDDEN";

							res_ls[f_id]["{}__{}".format(prefix,key)] = str(prof_1[key])

							# complete_col["{}__{}".format(prefix,key)] = {}
						if(entry!="all"):
							if(sample >=int(entry)): break
						# if(sample >=10): return jsonify(res_ls)
						if(prefix=="profile"):
							sample = sample + 1;
					else:
						loads_.desc = "Skipping Profiles : ["+str(sample)+"] || "+path
				else:
					print("Skipping Profiles : No User Associated || " +path)
		new_f_ls = []
		
		for key2 in res_ls:
			new_f_ls_IND = {}
			for key_new in MOBILE_DATA_ROWS_FORM_A:
				if(key_new not in res_ls[key2]):
					res_ls[key2][key_new] = "NO_DATA"
				new_f_ls_IND[key_new] = res_ls[key2][key_new]
			new_f_ls.append(new_f_ls_IND)

		count_f_ls = 0
		new_new_f_ls = []
		for ind_rec_ in new_f_ls:
			if(ind_rec_['profile__farmer_code'] != "NO_DATA"):
				new_new_f_ls.append(ind_rec_)


		# for key2 in res_ls:
		# 	if( "profile__farmer_code" in res_ls[key2]):
		# 		for key_for_add_ in MOBILE_DATA_ROWS_FORM_A:
		# 			if(key_for_add_ not in res_ls[key2]):
		# 				res_ls[key2][key_for_add_] = "NONE"
		# 		new_f_ls.append(res_ls[key2])

		return json.dumps(new_new_f_ls)
		# return jsonify(new_f_ls)

		# return jsonify(complete_col)
		# # return jsonify(res_ls)

MOBILE_DATA_ROWS_FORM_A = ["profile__USER_ID", "profile__f_name", "profile__m_name","profile__l_name", "profile__farmer_name", "profile__addr_brgy", "profile__addr_city", "profile__addr_prov", "profile__addr_region", "profile__addr_street_purok_sitio", "profile__datetime", "profile__ext_name", "profile__farmer-age", "profile__farmer-bday", "profile__farmer-civil_status", "profile__farmer-coords_lat", "profile__farmer-coords_long", "profile__farmer-email", "profile__farmer-fo_designation", "profile__farmer-fo_member_since", "profile__farmer-fo_name_rapid", "profile__farmer-fo_position", "profile__farmer-head_of_house", "profile__farmer-highest_education", "profile__farmer-ihead-hh-p", "profile__farmer-ihead-hh-s_ip", "profile__farmer-ihead-hh-s_ofw", "profile__farmer-ihead-hh-s_pwd", "profile__farmer-ip", "profile__farmer-ip_sex_head_hh", "profile__farmer-is_bday_sure", "profile__farmer-is_ip", "profile__farmer-is_ofw", "profile__farmer-is_pwd", "profile__farmer-marital_partner_name", "profile__farmer-name_head_hh", "profile__farmer-number", "profile__farmer-primary_crop", "profile__farmer-relation_head_hh", "profile__farmer-rsbsa", "profile__farmer-vocational", "profile__farmer-yearsfarming", "profile__farmer_code", "profile__farmer_dip_ref", "profile__farmer_img_base64", "profile__farmer_sex", "profile__farmer_sex_head_hh", "profile__form-remarks", "profile__is_synced", "add_farm__USER_ID", "add_farm__addr_brgy", "add_farm__addr_city", "add_farm__addr_prov", "add_farm__addr_region", "add_farm__addr_street_purok_sitio", "add_farm__datetime", "add_farm__farm-area_land_expansion_slope", "add_farm__farm-area_land_expasnion_flat", "add_farm__farm-area_land_rehab_flat", "add_farm__farm-area_land_rehab_slope", "add_farm__farm-bearing_plants", "add_farm__farm-declare_area", "add_farm__farm-is_multi_crop", "add_farm__farm-non_bearing_plants", "add_farm__farm-others_crops", "add_farm__farm-palin_hectares", "add_farm__farm-photo", "add_farm__farm-primary_crop", "add_farm__farm-primary_crop_av_prof_vol", "add_farm__farm-primary_crop_cycle_year", "add_farm__farm-primary_crop_total_land_area", "add_farm__farm-secondary_crop", "add_farm__farm-secondary_crop_av_prod_vol", "add_farm__farm-secondary_crop_cycle_year", "add_farm__farm-secondary_crop_total_land_area", "add_farm__farm-slope_hectars", "add_farm__farm-tenurial_Usfruc", "add_farm__farm-tenurial_cloa", "add_farm__farm-tenurial_co", "add_farm__farm-tenurial_others", "add_farm__farm-tenurial_so", "add_farm__farm-tenurial_stew", "add_farm__farm-tenurial_ten", "add_farm__farm-total_no_tenurial_lots", "add_farm__farmer-coords_lat", "add_farm__farmer-coords_long", "add_farm__farmer_code", "add_farm__form-remarks", "add_farm__is_synced", "hh_profile__USER_ID", "hh_profile__datetime", "hh_profile__farmer_code", "hh_profile__form-remarks", "hh_profile__hh-est_total_income_livestock", "hh_profile__hh-est_total_income_primary_crop", "hh_profile__hh-est_total_income_secondary_crop", "hh_profile__hh-mem_ip_f", "hh_profile__hh-mem_ip_m", "hh_profile__hh-mem_ofw_f", "hh_profile__hh-mem_ofw_m", "hh_profile__hh-mem_pwd_f", "hh_profile__hh-mem_pwd_m", "hh_profile__hh-non_farm_income_business", "hh_profile__hh-non_farm_income_employment", "hh_profile__hh-non_farm_income_others", "hh_profile__hh-non_farm_income_pantawid", "hh_profile__hh-non_farm_income_pension", "hh_profile__hh-non_farm_income_skilled", "hh_profile__hh-non_farm_remittance", "hh_profile__hh-rsbsa_no", "hh_profile__hh-total_hh_mem_0_17_f", "hh_profile__hh-total_hh_mem_0_17_m", "hh_profile__hh-total_hh_mem_18_30_f", "hh_profile__hh-total_hh_mem_18_30_m", "hh_profile__hh-total_hh_mem_31_59_f", "hh_profile__hh-total_hh_mem_31_59_m", "hh_profile__hh-total_hh_mem_60_up_f", "hh_profile__hh-total_hh_mem_60_up_m", "hh_profile__is_synced","workers_laborers__USER_ID", "workers_laborers__datetime", "workers_laborers__farmer_code", "workers_laborers__form-remarks", "workers_laborers__is_synced", "workers_laborers__workers-fam_is_ip", "workers_laborers__workers-fam_isfarmer", "workers_laborers__workers-fam_isofw", "workers_laborers__workers-fam_ispwd", "workers_laborers__workers-fam_isyouth", "workers_laborers__workers-fam_ls_ip", "workers_laborers__workers-fam_ls_ip_f", "workers_laborers__workers-fam_num_ip", "workers_laborers__workers-fam_num_ip_f", "workers_laborers__workers-fam_num_ofw", "workers_laborers__workers-fam_num_ofw_f", "workers_laborers__workers-fam_num_pwd", "workers_laborers__workers-fam_num_pwd_f", "workers_laborers__workers-fam_num_sr", "workers_laborers__workers-fam_num_youth_f", "workers_laborers__workers-fam_num_youth_m", "workers_laborers__workers-fam_srcitizen", "workers_laborers__workers-fam_total_female", "workers_laborers__workers-fam_total_male", "workers_laborers__workers-fam_year_salary_female", "workers_laborers__workers-fam_year_salary_male", "workers_laborers__workers-isfarmer", "workers_laborers__workers-non_fam_is_ip", "workers_laborers__workers-non_fam_isfarmer", "workers_laborers__workers-non_fam_isyouth", "workers_laborers__workers-non_fam_ls_ip", "workers_laborers__workers-non_fam_ls_ip_f", "workers_laborers__workers-non_fam_num__ofw_f", "workers_laborers__workers-non_fam_num_ip", "workers_laborers__workers-non_fam_num_ip_f", "workers_laborers__workers-non_fam_num_ofw", "workers_laborers__workers-non_fam_num_pwd", "workers_laborers__workers-non_fam_num_pwd_f", "workers_laborers__workers-non_fam_num_sr", "workers_laborers__workers-non_fam_num_sr_f", "workers_laborers__workers-non_fam_num_youth", "workers_laborers__workers-non_fam_num_youth_f", "workers_laborers__workers-non_fam_ofw", "workers_laborers__workers-non_fam_pwd", "workers_laborers__workers-non_fam_srcitizen", "workers_laborers__workers-non_fam_total_female", "workers_laborers__workers-non_fam_total_male", "workers_laborers__workers-non_fam_year_salary_female", "workers_laborers__workers-non_fam_year_salary_male","prod_cost__USER_ID", "prod_cost__datetime", "prod_cost__farmer_code", "prod_cost__form-remarks", "prod_cost__is_synced", "prod_cost__prodcost-crop_cycle_year", "prod_cost__prodcost-crop_harvest", "prod_cost__prodcost-is_keep_record", "prod_cost__prodcost-labor_crop_harvest", "prod_cost__prodcost-labor_crop_maintenance_act", "prod_cost__prodcost-labor_land_dev_prep", "prod_cost__prodcost-labor_post_harvest_act", "prod_cost__prodcost-materials__act", "prod_cost__prodcost-materials_land_dev_prep", "prod_cost__prodcost-post_harvest_act", "marketing_sales__USER_ID", "marketing_sales__datetime", "marketing_sales__farmer_code", "marketing_sales__form-remarks", "marketing_sales__is_synced", "marketing_sales__market-is_anchor_firm", "marketing_sales__market-is_anchor_firm1", "marketing_sales__market-is_anchor_firm12", "marketing_sales__market-is_anchor_firm123", "marketing_sales__market-is_coop", "marketing_sales__market-is_coop1", "marketing_sales__market-is_coop12", "marketing_sales__market-is_coop123", "marketing_sales__market-is_negosyo_center", "marketing_sales__market-is_negosyo_center1", "marketing_sales__market-is_negosyo_center12", "marketing_sales__market-is_negosyo_center123", "marketing_sales__market-is_others", "marketing_sales__market-is_others1", "marketing_sales__market-is_others12", "marketing_sales__market-is_others123", "marketing_sales__market-is_sme", "marketing_sales__market-is_sme1", "marketing_sales__market-is_sme12", "marketing_sales__market-is_sme123", "marketing_sales__market-name_anchor_firm", "marketing_sales__market-name_anchor_firm1", "marketing_sales__market-name_anchor_firm12", "marketing_sales__market-name_anchor_firm123", "marketing_sales__market-name_coop", "marketing_sales__market-name_coop1", "marketing_sales__market-name_coop12", "marketing_sales__market-name_coop123", "marketing_sales__market-name_others", "marketing_sales__market-name_others1", "marketing_sales__market-name_others12", "marketing_sales__market-name_others123", "marketing_sales__market-name_sme", "marketing_sales__market-name_sme1", "marketing_sales__market-name_sme12", "marketing_sales__market-name_sme123", "marketing_sales__market-primary_crop_buyer_others", "marketing_sales__market-primary_crop_buyer_others1", "marketing_sales__market-primary_crop_buyer_others12", "marketing_sales__market-primary_crop_buyer_others123", "marketing_sales__market-primary_crop_dist_others", "marketing_sales__market-primary_crop_dist_others1", "marketing_sales__market-primary_crop_dist_others12", "marketing_sales__market-primary_crop_dist_others123", "marketing_sales__market-primary_crop_dist_point", "marketing_sales__market-primary_crop_dist_point1", "marketing_sales__market-primary_crop_dist_point12", "marketing_sales__market-primary_crop_dist_point123", "marketing_sales__market-primary_crop_product_fgp", "marketing_sales__market-primary_crop_product_fgp1", "marketing_sales__market-primary_crop_product_fgp12", "marketing_sales__market-primary_crop_product_fgp123", "marketing_sales__market-primary_crop_product_fgp_unit", "marketing_sales__market-primary_crop_product_fgp_unit1", "marketing_sales__market-primary_crop_product_fgp_unit12", "marketing_sales__market-primary_crop_product_fgp_unit123", "marketing_sales__market-primary_crop_type", "marketing_sales__market-primary_crop_type1", "marketing_sales__market-primary_crop_type12", "marketing_sales__market-primary_crop_type123", "marketing_sales__market-primary_crop_type_buyer", "marketing_sales__market-primary_crop_type_buyer1", "marketing_sales__market-primary_crop_type_buyer12", "marketing_sales__market-primary_crop_type_buyer123", "marketing_sales__market-primary_vol_del", "marketing_sales__market-primary_vol_del1", "marketing_sales__market-primary_vol_del12", "marketing_sales__market-primary_vol_del123", "marketing_sales__record_num", "post_harvest__USER_ID", "post_harvest__addr_brgy", "post_harvest__addr_brgy1", "post_harvest__addr_brgy12", "post_harvest__addr_city", "post_harvest__addr_city1", "post_harvest__addr_city12", "post_harvest__addr_prov", "post_harvest__addr_prov1", "post_harvest__addr_prov12", "post_harvest__addr_region", "post_harvest__addr_region1", "post_harvest__addr_region12", "post_harvest__addr_street_purok_sitio", "post_harvest__addr_street_purok_sitio1", "post_harvest__addr_street_purok_sitio12", "post_harvest__datetime", "post_harvest__farmer-coords_lat", "post_harvest__farmer-coords_lat1", "post_harvest__farmer-coords_lat12", "post_harvest__farmer-coords_long", "post_harvest__farmer-coords_long1", "post_harvest__farmer-coords_long12", "post_harvest__farmer_code", "post_harvest__form-remarks", "post_harvest__is_synced", "post_harvest__post_harv-capacity", "post_harvest__post_harv-capacity1", "post_harvest__post_harv-capacity12", "post_harvest__post_harv-capacity_unit", "post_harvest__post_harv-capacity_unit1", "post_harvest__post_harv-capacity_unit12", "post_harvest__post_harv-capacity_unit_time", "post_harvest__post_harv-capacity_unit_time1", "post_harvest__post_harv-capacity_unit_time12", "post_harvest__post_harv-ph_product_form", "post_harvest__post_harv-ph_product_form1", "post_harvest__post_harv-ph_product_form12", "post_harvest__post_harv-phcropothers", "post_harvest__post_harv-phcropothers1", "post_harvest__post_harv-phcropothers12", "post_harvest__post_harv-photo", "post_harvest__post_harv-photo1", "post_harvest__post_harv-photo12", "post_harvest__post_harv-type_faci_equip", "post_harvest__post_harv-type_faci_equip1", "post_harvest__post_harv-type_faci_equip12", "post_harvest__post_harv-type_faci_equip_name", "post_harvest__post_harv-type_faci_equip_name1", "post_harvest__post_harv-type_faci_equip_name12", "post_harvest__record_duplicate_id", "post_harvest__record_num", "access_financial__USER_ID", "access_financial__datetime", "access_financial__farmer_code", "access_financial__financial-if_loan_bank", "access_financial__financial-if_loan_non_bank", "access_financial__financial-is_crop_deposit", "access_financial__financial-is_crop_insurance", "access_financial__financial-is_crop_others", "access_financial__financial-is_crop_payments", "access_financial__financial-is_loan", "access_financial__financial-is_primary_crop_distribution", "access_financial__financial-is_remmitances", "access_financial__financial-loan_govbank_name", "access_financial__financial-loan_govbank_type", "access_financial__financial-loan_if_nonbank_others", "access_financial__financial-loan_name_fo", "access_financial__financial-loan_name_lending", "access_financial__financial-loan_name_ngo", "access_financial__financial-loan_name_others", "access_financial__financial-loan_private_name", "access_financial__financial-loan_private_type", "access_financial__financial-loan_type_fo", "access_financial__financial-loan_type_lending", "access_financial__financial-loan_type_ngo", "access_financial__financial-loan_type_others", "access_financial__financial-type_deposit", "access_financial__financial-type_deposit_bank", "access_financial__financial-type_deposit_non_bank", "access_financial__financial-type_insurance", "access_financial__financial-type_insurance_bank", "access_financial__financial-type_insurance_non_bank", "access_financial__financial-type_others_bank", "access_financial__financial-type_others_non_bank", "access_financial__financial-type_payments", "access_financial__financial-type_payments_bank", "access_financial__financial-type_payments_non_bank", "access_financial__financial-type_remmittance_name", "access_financial__form-remarks", "access_financial__is_synced", "feedback__USER_ID", "feedback__datetime", "feedback__farmer-Banana", "feedback__farmer-Cacao", "feedback__farmer-Calamansi", "feedback__farmer-Coconut", "feedback__farmer-Coffee", "feedback__farmer-Jackfruit", "feedback__farmer-Mango", "feedback__farmer-Other_fruits_nuts", "feedback__farmer-Others", "feedback__farmer-Pili_Nut", "feedback__farmer_code", "feedback__feedback-cert_acquired", "feedback__feedback-commnets", "feedback__feedback-num_of_trainings_2_3_years", "feedback__feedback-remarks", "feedback__feedback-support_need", "feedback__feedback-type_mobile", "feedback__feedback[]-freq", "feedback__feedback[]-freq1", "feedback__feedback[]-freq12", "feedback__feedback[]-freq123", "feedback__feedback[]-freq1234", "feedback__feedback[]-freq12345", "feedback__feedback[]-media", "feedback__feedback[]-media1", "feedback__feedback[]-media12", "feedback__feedback[]-media123", "feedback__feedback[]-media1234", "feedback__feedback[]-media12345", "feedback__is_synced", "feedback__record_num", ]