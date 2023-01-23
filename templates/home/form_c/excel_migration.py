from flask import Flask, Blueprint, render_template, url_for, json, jsonify, send_file, redirect, request
import urllib.request
import pandas as pd
from controllers import apiV2 as v2
import Configurations as c
from tqdm import tqdm
import os
from modules.Connections import mysql,sqlite
import glob
from pandas.io.json import json_normalize

app = Blueprint("excel_migration",__name__)
rapid= sqlite(c.SQLITE_DB)

@app.route('/excel_export_a/<user>/<region>/<num_entries>/<exist>')
def index(user,region,num_entries,exist):
	if(exist != "yes"):
		__JSN = __populate_response(user,region,num_entries);
		__JSN_excel = json.dumps(excel_export_a_get_excel(user,region,num_entries))
	else:
		raw_mobile_ = open(c.RECORDS+"/exports/TEMP/temp_a_mobile__{}.json".format(user))
		__JSN = (json.loads(raw_mobile_.read()))
		raw_mobile_.close()
		# return (__JSN)

		raw_excel_ = open(c.RECORDS+"/exports/TEMP/temp_a_excel__{}.json".format(user))
		__JSN_excel = raw_excel_.read()
		raw_excel_.close()

	return merge_excel_ss(user,region,__JSN,__JSN_excel)
	df = pd.read_json(__JSN)

	__TO_DL_EXCEL = c.RECORDS+'/exports/spreadsheets/{}.xlsx'.format(user)

	df.to_csv (c.RECORDS+'/exports/csv/__TEMP__CSV.csv', index = 'profile__farmer_code')
	header_names = ['profile USER ID','profile f name','profile m name','profile l name','profile farmer name','profile addr brgy','profile addr city','profile addr prov','profile addr region','profile addr street purok sitio','profile datetime','profile ext name','profile farmer-age','profile farmer-bday','profile farmer-civil status','profile farmer-coords lat','profile farmer-coords long','profile farmer-email','profile farmer-fo designation','profile farmer-fo member since','profile farmer-fo name rapid','profile farmer-fo position','profile farmer-head of house','profile farmer-highest education','profile farmer-ihead-hh-p','profile farmer-ihead-hh-s ip','profile farmer-ihead-hh-s ofw','profile farmer-ihead-hh-s pwd','profile farmer-ip','profile farmer-ip sex head hh','profile farmer-is bday sure','profile farmer-is ip','profile farmer-is ofw','profile farmer-is pwd','profile farmer-marital partner name','profile farmer-name head hh','profile farmer-number','profile farmer-primary crop','profile farmer-relation head hh','profile farmer-rsbsa','profile farmer-vocational','profile farmer-yearsfarming','profile farmer code','profile farmer dip ref','profile farmer img base64','profile farmer sex','profile farmer sex head hh','profile form-remarks','profile is synced','add farm USER ID','add farm addr brgy','add farm addr city','add farm addr prov','add farm addr region','add farm addr street purok sitio','add farm datetime','add farm farm-area land expansion slope','add farm farm-area land expasnion flat','add farm farm-area land rehab flat','add farm farm-area land rehab slope','add farm farm-bearing plants','add farm farm-declare area','add farm farm-is multi crop','add farm farm-non bearing plants','add farm farm-others crops','add farm farm-palin hectares','add farm farm-photo','add farm farm-primary crop','add farm farm-primary crop av prof vol','add farm farm-primary crop cycle year','add farm farm-primary crop total land area','add farm farm-secondary crop','add farm farm-secondary crop av prod vol','add farm farm-secondary crop cycle year','add farm farm-secondary crop total land area','add farm farm-slope hectars','add farm farm-tenurial Usfruc','add farm farm-tenurial cloa','add farm farm-tenurial co','add farm farm-tenurial others','add farm farm-tenurial so','add farm farm-tenurial stew','add farm farm-tenurial ten','add farm farm-total no tenurial lots','add farm farmer-coords lat','add farm farmer-coords long','add farm farmer code','add farm form-remarks','add farm is synced','hh profile USER ID','hh profile datetime','hh profile farmer code','hh profile form-remarks','hh profile hh-est total income livestock','hh profile hh-est total income primary crop','hh profile hh-est total income secondary crop','hh profile hh-mem ip f','hh profile hh-mem ip m','hh profile hh-mem ofw f','hh profile hh-mem ofw m','hh profile hh-mem pwd f','hh profile hh-mem pwd m','hh profile hh-non farm income business','hh profile hh-non farm income employment','hh profile hh-non farm income others','hh profile hh-non farm income pantawid','hh profile hh-non farm income pension','hh profile hh-non farm income skilled','hh profile hh-non farm remittance','hh profile hh-rsbsa no','hh profile hh-total hh mem 0 17 f','hh profile hh-total hh mem 0 17 m','hh profile hh-total hh mem 18 30 f','hh profile hh-total hh mem 18 30 m','hh profile hh-total hh mem 31 59 f','hh profile hh-total hh mem 31 59 m','hh profile hh-total hh mem 60 up f','hh profile hh-total hh mem 60 up m','hh profile is synced','workers laborers USER ID','workers laborers datetime','workers laborers farmer code','workers laborers form-remarks','workers laborers is synced','workers laborers workers-fam is ip','workers laborers workers-fam isfarmer','workers laborers workers-fam isofw','workers laborers workers-fam ispwd','workers laborers workers-fam isyouth','workers laborers workers-fam ls ip','workers laborers workers-fam ls ip f','workers laborers workers-fam num ip','workers laborers workers-fam num ip f','workers laborers workers-fam num ofw','workers laborers workers-fam num ofw f','workers laborers workers-fam num pwd','workers laborers workers-fam num pwd f','workers laborers workers-fam num sr','workers laborers workers-fam num youth f','workers laborers workers-fam num youth m','workers laborers workers-fam srcitizen','workers laborers workers-fam total female','workers laborers workers-fam total male','workers laborers workers-fam year salary female','workers laborers workers-fam year salary male','workers laborers workers-isfarmer','workers laborers workers-non fam is ip','workers laborers workers-non fam isfarmer','workers laborers workers-non fam isyouth','workers laborers workers-non fam ls ip','workers laborers workers-non fam ls ip f','workers laborers workers-non fam num ofw f','workers laborers workers-non fam num ip','workers laborers workers-non fam num ip f','workers laborers workers-non fam num ofw','workers laborers workers-non fam num pwd','workers laborers workers-non fam num pwd f','workers laborers workers-non fam num sr','workers laborers workers-non fam num sr f','workers laborers workers-non fam num youth','workers laborers workers-non fam num youth f','workers laborers workers-non fam ofw','workers laborers workers-non fam pwd','workers laborers workers-non fam srcitizen','workers laborers workers-non fam total female','workers laborers workers-non fam total male','workers laborers workers-non fam year salary female','workers laborers workers-non fam year salary male','prod cost USER ID','prod cost datetime','prod cost farmer code','prod cost form-remarks','prod cost is synced','prod cost prodcost-crop cycle year','prod cost prodcost-crop harvest','prod cost prodcost-is keep record','prod cost prodcost-labor crop harvest','prod cost prodcost-labor crop maintenance act','prod cost prodcost-labor land dev prep','prod cost prodcost-labor post harvest act','prod cost prodcost-materials act','prod cost prodcost-materials land dev prep','prod cost prodcost-post harvest act','marketing sales USER ID','marketing sales datetime','marketing sales farmer code','marketing sales form-remarks','marketing sales is synced','marketing sales market-is anchor firm','marketing sales market-is anchor firm1','marketing sales market-is anchor firm12','marketing sales market-is anchor firm123','marketing sales market-is coop','marketing sales market-is coop1','marketing sales market-is coop12','marketing sales market-is coop123','marketing sales market-is negosyo center','marketing sales market-is negosyo center1','marketing sales market-is negosyo center12','marketing sales market-is negosyo center123','marketing sales market-is others','marketing sales market-is others1','marketing sales market-is others12','marketing sales market-is others123','marketing sales market-is sme','marketing sales market-is sme1','marketing sales market-is sme12','marketing sales market-is sme123','marketing sales market-name anchor firm','marketing sales market-name anchor firm1','marketing sales market-name anchor firm12','marketing sales market-name anchor firm123','marketing sales market-name coop','marketing sales market-name coop1','marketing sales market-name coop12','marketing sales market-name coop123','marketing sales market-name others','marketing sales market-name others1','marketing sales market-name others12','marketing sales market-name others123','marketing sales market-name sme','marketing sales market-name sme1','marketing sales market-name sme12','marketing sales market-name sme123','marketing sales market-primary crop buyer others','marketing sales market-primary crop buyer others1','marketing sales market-primary crop buyer others12','marketing sales market-primary crop buyer others123','marketing sales market-primary crop dist others','marketing sales market-primary crop dist others1','marketing sales market-primary crop dist others12','marketing sales market-primary crop dist others123','marketing sales market-primary crop dist point','marketing sales market-primary crop dist point1','marketing sales market-primary crop dist point12','marketing sales market-primary crop dist point123','marketing sales market-primary crop product fgp','marketing sales market-primary crop product fgp1','marketing sales market-primary crop product fgp12','marketing sales market-primary crop product fgp123','marketing sales market-primary crop product fgp unit','marketing sales market-primary crop product fgp unit1','marketing sales market-primary crop product fgp unit12','marketing sales market-primary crop product fgp unit123','marketing sales market-primary crop type','marketing sales market-primary crop type1','marketing sales market-primary crop type12','marketing sales market-primary crop type123','marketing sales market-primary crop type buyer','marketing sales market-primary crop type buyer1','marketing sales market-primary crop type buyer12','marketing sales market-primary crop type buyer123','marketing sales market-primary vol del','marketing sales market-primary vol del1','marketing sales market-primary vol del12','marketing sales market-primary vol del123','marketing sales record num','post harvest USER ID','post harvest addr brgy','post harvest addr brgy1','post harvest addr brgy12','post harvest addr city','post harvest addr city1','post harvest addr city12','post harvest addr prov','post harvest addr prov1','post harvest addr prov12','post harvest addr region','post harvest addr region1','post harvest addr region12','post harvest addr street purok sitio','post harvest addr street purok sitio1','post harvest addr street purok sitio12','post harvest datetime','post harvest farmer-coords lat','post harvest farmer-coords lat1','post harvest farmer-coords lat12','post harvest farmer-coords long','post harvest farmer-coords long1','post harvest farmer-coords long12','post harvest farmer code','post harvest form-remarks','post harvest is synced','post harvest post harv-capacity','post harvest post harv-capacity1','post harvest post harv-capacity12','post harvest post harv-capacity unit','post harvest post harv-capacity unit1','post harvest post harv-capacity unit12','post harvest post harv-capacity unit time','post harvest post harv-capacity unit time1','post harvest post harv-capacity unit time12','post harvest post harv-ph product form','post harvest post harv-ph product form1','post harvest post harv-ph product form12','post harvest post harv-phcropothers','post harvest post harv-phcropothers1','post harvest post harv-phcropothers12','post harvest post harv-photo','post harvest post harv-photo1','post harvest post harv-photo12','post harvest post harv-type faci equip','post harvest post harv-type faci equip1','post harvest post harv-type faci equip12','post harvest post harv-type faci equip name','post harvest post harv-type faci equip name1','post harvest post harv-type faci equip name12','post harvest record duplicate id','post harvest record num','access financial USER ID','access financial datetime','access financial farmer code','access financial financial-if loan bank','access financial financial-if loan non bank','access financial financial-is crop deposit','access financial financial-is crop insurance','access financial financial-is crop others','access financial financial-is crop payments','access financial financial-is loan','access financial financial-is primary crop distribution','access financial financial-is remmitances','access financial financial-loan govbank name','access financial financial-loan govbank type','access financial financial-loan if nonbank others','access financial financial-loan name fo','access financial financial-loan name lending','access financial financial-loan name ngo','access financial financial-loan name others','access financial financial-loan private name','access financial financial-loan private type','access financial financial-loan type fo','access financial financial-loan type lending','access financial financial-loan type ngo','access financial financial-loan type others','access financial financial-type deposit','access financial financial-type deposit bank','access financial financial-type deposit non bank','access financial financial-type insurance','access financial financial-type insurance bank','access financial financial-type insurance non bank','access financial financial-type others bank','access financial financial-type others non bank','access financial financial-type payments','access financial financial-type payments bank','access financial financial-type payments non bank','access financial financial-type remmittance name','access financial form-remarks','access financial is synced','feedback USER ID','feedback datetime','feedback farmer-Banana','feedback farmer-Cacao','feedback farmer-Calamansi','feedback farmer-Coconut','feedback farmer-Coffee','feedback farmer-Jackfruit','feedback farmer-Mango','feedback farmer-Other fruits nuts','feedback farmer-Others','feedback farmer-Pili Nut','feedback farmer code','feedback feedback-cert acquired','feedback feedback-commnets','feedback feedback-num of trainings 2 3 years','feedback feedback-remarks','feedback feedback-support need','feedback feedback-type mobile','feedback feedback[]-freq','feedback feedback[]-freq1','feedback feedback[]-freq12','feedback feedback[]-freq123','feedback feedback[]-freq1234','feedback feedback[]-freq12345','feedback feedback[]-media','feedback feedback[]-media1','feedback feedback[]-media12','feedback feedback[]-media123','feedback feedback[]-media1234','feedback feedback[]-media12345','feedback is synced','feedback record num']
	df=pd.read_csv(c.RECORDS+'/exports/csv/__TEMP__CSV.csv',header=None, skiprows=1,names=header_names)
	
	writer = pd.ExcelWriter(__TO_DL_EXCEL) 
	df.to_excel(writer, sheet_name='mobile_imports',index=False )

	for column in df:
		column_width = max(df[column].astype(str).map(len).max(), len(column))
		col_idx = df.columns.get_loc(column)
		writer.sheets['mobile_imports'].set_column(col_idx, col_idx, column_width)

	workbook  = writer.book
	worksheet = writer.sheets['mobile_imports']
	header_format = workbook.add_format({'bold': True,'text_wrap': True,'valign': 'top','fg_color': '#00cc66','border': 1})
	for col_num, value in enumerate(df.columns.values):
		worksheet.write(0, col_num, value, header_format)
	writer.save()

	df2 = pd.read_json(__JSN_excel)
	# df2 = pd.DataFrame(excel_export_a_get_excel(user,region,num_entries))

	with pd.ExcelWriter(__TO_DL_EXCEL, engine='openpyxl', mode='a') as writer:  
		df2.to_excel(writer, sheet_name='excel_imports')

	return send_file(__TO_DL_EXCEL)

	

def __populate_response(user,region,num_entries):
	_d = v2._main.excel_export_a_mobile(region,num_entries)
	json_save_as_file(_d ,"temp_a_mobile__{}".format(user))
	return (_d)


# ========================================================================

@app.route("/excel_export_a/get_excel/<user>/<region>/<num_entries>",methods=["POST","GET"])
def excel_export_a_get_excel(user,region,num_entries):
	region = region.replace("_"," ").upper()
	dir_path = c.RECORDS+"/spreadsheets/"
	FROM_EXCEL_RPOFILES = {}
	loads_ = tqdm(os.listdir(dir_path))
	count = 0
	for path in loads_:
		PATH__ = os.path.join(dir_path, path)
		loads_.desc = "Scanning || {}".format( path)
		if os.path.isfile(PATH__):
			if PATH__.find("._DELETED_FILE_")<0:    
				# print(PATH__)
				file_name =  PATH__ # path to file + file name
				_ID_ = path.split("#")[0]
				loads_.desc = "Retriveing [{}]|| {}".format( _ID_, path)
				USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ; ".format(_ID_) )
				if(len(USER)!=0):
					if(USER[0]['rcu']==region or region=="ALL"):
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
						FROM_EXCEL_RPOFILES.update(_result)

					else:
						loads_.desc = "Skipping Profiles : ["+str(file_name)+"] || "+path
				else:
					print("Skipping Profiles : No User Associated || " +path)
				# if(num_entries!="all"):
				#     if(count>=int(num_entries)):break
				# count = count + 1

	KEYS = ["ID","First name","Middle name","Last name","Extension name","Sex","Mobile number","email address","birthday","bday not sure","civil status","is head og household","name of head of household","head hh name","head hh relationship","head hh sex","head hh pwd","head hh ofw","head hh ip","longitude","latitude","region","province","city municipality","brgy","purok sitio street","primary crop","DIP name","Farmer pwd","Farmer ofw","farmer ip","years of farming","Name of coop","position in coop","coop member since","is listed in RSBSA","highest educational attainment","Vocational Skills","Longitude","Latitude","municipality","Brgy","street/purok/sitio","declared area (Ha.)","is intercroping?","Primary crop","sloping area in hectares (greater than 18 degrees)","flat/[lain area in hectares","No. bearing trees planted","No. bearing non-trees planted","Sole ownership","co-ownership","CLOA/individual EP","stewardship","usufruct","tenancy","others","Primary crop Ave. Production volume (w018-2019) (kg/cycle)","Primary Crop total land area covered (Ha.)","Primary Crop No of Cycle ","Secondary Crop if Any","Sloping ","Flat/Plain","Sloping","flat/plain","No. Male","no. Female","List of IP group Presentt in the HH","Estimated Total Annual Income (Php) - Primary Crop ","Estimated Total Annual Income (Php) - Secondary Crop ","Estimated Total Annual Income (Php) - Livestock/Fishing etc","Family Remittnaces","Employment","Skilled Labor","Business","Social Pension","Pantawid Beneficary","Other Subsidies","If Others, Please specify","Does Farmer Keep Records","Crop Cycle Per year","Land Development Preperation","Crop Maintenance Activities","Crop Harvesting","Post-Harvest Activities","Youth","Senior Citizen","PWD","OFW","IP","List of IP group Present for FAMILY Workers","List of IP group Present for NON-FAMILY Workers","Male Family Income (Yearly)","Female Family Income (Yearly)","Male NON-Family Income (Yearly)","Female NON-Family Income (Yearly)","Type of PH Facility/Equipment","Name of Equipment/Facility","Region","Province","City/Municipality","PH Product Form","PH Capacity (qty)","PH Capacity unit (kg/metric_tons/sac/crate/box)","PH Capacity Frequency (hr, day,month, year, cycle/harvest)","Primary crop/Product Type","Primary crop/Product Delivery","Farmers Org","SME","Anchor Firm","Negosyo Center","Others","Payment Terms (Consignment, Cash, Credit, Others)","Buyer Type (Trader, Consolidator, Processor. Others)","Farm Gate Price (FGP) on Php","Unit (Kg, Metric_tons, Sack/box)","Crop Insurance (yes, No)","Name of Govt. Bank (LBP. DBP) if any","Type of Loan","Name of Private Bank if any","Loan Initiative (Relatives, Informal Lenders)","Type of Deposits if any","Name of bank if the  FSP is Bank","Name of non-bank if the  FSP is non-Bank","Type of Insurance if any","Type of Payments if any","Name of Non Bank FSP","Number of Farm-Related Trainings attended in the last 2-3 years","List of Value Chain","Farm Certification Acquired if any","List of Medium/source of information","List of  frequency of Medium/source of information ","Owns what Type of Mobile Phone (None, Smartphone, Legacy_phone)","Support Needed to improve farm productivity","Farmer Comments about Rapid","Enumerator Remarks"]
	KEYS_DATA = []

	# return jsonify(KEYS)

	# return "done"
	# print(KEYS)
	# del FROM_EXCEL_RPOFILES[0][1]

	# for kkk in FROM_EXCEL_RPOFILES:
		# print(kkk)
	for key in FROM_EXCEL_RPOFILES:
		_count = 0
		_temp_data = {} 
		for key2 in KEYS:
		# for key2 in FROM_EXCEL_RPOFILES[key]:
			kkk = str(FROM_EXCEL_RPOFILES[key][_count])
			# kkk = KEYS[_count]
			# ddd = FROM_EXCEL_RPOFILES[key][key2]
			ddd = str(key2)
			_temp_data.update({kkk:ddd})
			_count = _count + 1

		# print(_temp_data)
		KEYS_DATA.append(_temp_data)
	json_save_as_file(KEYS_DATA,"temp_a_excel__{}".format(user))
	# json_save_as_file(KEYS_DATA,"sample")
	# # return json.jsonify(FROM_EXCEL_RPOFILES)
	# json_save_as_file(KEYS_DATA,"temp_a_excel")
	return (KEYS_DATA)
# ================================================================================================
def merge_excel(user,region):
	path = c.RECORDS+"/spreadsheets/"

	# csv files in the path
	# file_list = glob.glob(path + "/*.xlsx")
	# loads_ = tqdm(file_list)
	loads_ = tqdm(os.listdir(path))
	excl_list = []

	for load in loads_:
		print("++++++++++++++++++++++++++++++++++")
		print(path+load)
		PATH__ = os.path.join(path,load)
		if PATH__.find("._DELETED_FILE_")<0:
			_ID_ = load.split("#")[0]
			# USER = rapid.select("SELECT * FROM `users` WHERE `id`={} ; ".format(_ID_) )
			# if(len(USER)!=0):
			# 	if(USER[0]['rcu']==region or region=="ALL"):
			excl_list.append(pd.read_excel(path+load))
					
	# list of excel files we want to merge.
	# pd.read_excel(file_path) reads the 
	# excel data into pandas dataframe.

	# for file in file_list:
	# 	excl_list.append(pd.read_excel(file))

	# concatenate all DataFrames in the list
	# into a single DataFrame, returns new
	# DataFrame.
	excl_merged = pd.concat(excl_list, ignore_index=True)

	# exports the dataframe into excel file
	# with specified name.
	excl_merged.to_excel('Bank_Stocks.xlsx', index=False)
	return "done"


# ================================================================================================
def merge_excel_ss(user,region,__JSN,__JSN_excel):
	c.RECORDS+'/exports/csv/__TEMP__CSV.csv'

	# df = pd.DataFrame(json.loads(__JSN_excel))
	# df.to_excel(c.RECORDS+'/exports/csv/{}_temp.csv'.format(user))

	df = json_normalize(json.loads(__JSN_excel))
	df.to_csv(c.RECORDS+'/exports/csv/{}_temp.csv'.format(user), sep=',', encoding='utf-8')
	return "DONE"
# =================================================
def json_save_as_file(data,name):
	ss = open(c.RECORDS+"/exports/TEMP/{}.json".format(name),"w")
	ss.write(json.dumps((data)))
	ss.close()

if __name__ == "__main__":
	app.run(debug=True)

	# sample edit