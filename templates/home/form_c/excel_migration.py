from flask import Flask, Blueprint, render_template, url_for, json, jsonify, send_file
import urllib.request
import pandas as pd
app = Blueprint("excel_migration",__name__)

@app.route('/excel_main/<num_entries>')
def index(num_entries):
    # get_url= urllib.request.urlopen('https://dtirapid.pythonanywhere.com/api/v2/sample')
    # print("Response Status: "+ str(get_url.getcode()) )
    # _DATA_ = json.loads(get_url.read())
    df = pd.read_json (r'https://dtirapid.pythonanywhere.com/api/v2/sample/'+num_entries)
    df.to_csv (r'exported_file.csv', index = 'profile__farmer_code')
    header_names = ['profile USER ID',
'profile f name',
'profile m name',
'profile l name',
'profile farmer name',
'profile addr brgy',
'profile addr city',
'profile addr prov',
'profile addr region',
'profile addr street purok sitio',
'profile datetime',
'profile ext name',
'profile farmer-age',
'profile farmer-bday',
'profile farmer-civil status',
'profile farmer-coords lat',
'profile farmer-coords long',
'profile farmer-email',
'profile farmer-fo designation',
'profile farmer-fo member since',
'profile farmer-fo name rapid',
'profile farmer-fo position',
'profile farmer-head of house',
'profile farmer-highest education',
'profile farmer-ihead-hh-p',
'profile farmer-ihead-hh-s ip',
'profile farmer-ihead-hh-s ofw',
'profile farmer-ihead-hh-s pwd',
'profile farmer-ip',
'profile farmer-ip sex head hh',
'profile farmer-is bday sure',
'profile farmer-is ip',
'profile farmer-is ofw',
'profile farmer-is pwd',
'profile farmer-marital partner name',
'profile farmer-name head hh',
'profile farmer-number',
'profile farmer-primary crop',
'profile farmer-relation head hh',
'profile farmer-rsbsa',
'profile farmer-vocational',
'profile farmer-yearsfarming',
'profile farmer code',
'profile farmer dip ref',
'profile farmer img base64',
'profile farmer sex',
'profile farmer sex head hh',
'profile form-remarks',
'profile is synced',
'add farm USER ID',
'add farm addr brgy',
'add farm addr city',
'add farm addr prov',
'add farm addr region',
'add farm addr street purok sitio',
'add farm datetime',
'add farm farm-area land expansion slope',
'add farm farm-area land expasnion flat',
'add farm farm-area land rehab flat',
'add farm farm-area land rehab slope',
'add farm farm-bearing plants',
'add farm farm-declare area',
'add farm farm-is multi crop',
'add farm farm-non bearing plants',
'add farm farm-others crops',
'add farm farm-palin hectares',
'add farm farm-photo',
'add farm farm-primary crop',
'add farm farm-primary crop av prof vol',
'add farm farm-primary crop cycle year',
'add farm farm-primary crop total land area',
'add farm farm-secondary crop',
'add farm farm-secondary crop av prod vol',
'add farm farm-secondary crop cycle year',
'add farm farm-secondary crop total land area',
'add farm farm-slope hectars',
'add farm farm-tenurial Usfruc',
'add farm farm-tenurial cloa',
'add farm farm-tenurial co',
'add farm farm-tenurial others',
'add farm farm-tenurial so',
'add farm farm-tenurial stew',
'add farm farm-tenurial ten',
'add farm farm-total no tenurial lots',
'add farm farmer-coords lat',
'add farm farmer-coords long',
'add farm farmer code',
'add farm form-remarks',
'add farm is synced',
'hh profile USER ID',
'hh profile datetime',
'hh profile farmer code',
'hh profile form-remarks',
'hh profile hh-est total income livestock',
'hh profile hh-est total income primary crop',
'hh profile hh-est total income secondary crop',
'hh profile hh-mem ip f',
'hh profile hh-mem ip m',
'hh profile hh-mem ofw f',
'hh profile hh-mem ofw m',
'hh profile hh-mem pwd f',
'hh profile hh-mem pwd m',
'hh profile hh-non farm income business',
'hh profile hh-non farm income employment',
'hh profile hh-non farm income others',
'hh profile hh-non farm income pantawid',
'hh profile hh-non farm income pension',
'hh profile hh-non farm income skilled',
'hh profile hh-non farm remittance',
'hh profile hh-rsbsa no',
'hh profile hh-total hh mem 0 17 f',
'hh profile hh-total hh mem 0 17 m',
'hh profile hh-total hh mem 18 30 f',
'hh profile hh-total hh mem 18 30 m',
'hh profile hh-total hh mem 31 59 f',
'hh profile hh-total hh mem 31 59 m',
'hh profile hh-total hh mem 60 up f',
'hh profile hh-total hh mem 60 up m',
'hh profile is synced',
'workers laborers USER ID',
'workers laborers datetime',
'workers laborers farmer code',
'workers laborers form-remarks',
'workers laborers is synced',
'workers laborers workers-fam is ip',
'workers laborers workers-fam isfarmer',
'workers laborers workers-fam isofw',
'workers laborers workers-fam ispwd',
'workers laborers workers-fam isyouth',
'workers laborers workers-fam ls ip',
'workers laborers workers-fam ls ip f',
'workers laborers workers-fam num ip',
'workers laborers workers-fam num ip f',
'workers laborers workers-fam num ofw',
'workers laborers workers-fam num ofw f',
'workers laborers workers-fam num pwd',
'workers laborers workers-fam num pwd f',
'workers laborers workers-fam num sr',
'workers laborers workers-fam num youth f',
'workers laborers workers-fam num youth m',
'workers laborers workers-fam srcitizen',
'workers laborers workers-fam total female',
'workers laborers workers-fam total male',
'workers laborers workers-fam year salary female',
'workers laborers workers-fam year salary male',
'workers laborers workers-isfarmer',
'workers laborers workers-non fam is ip',
'workers laborers workers-non fam isfarmer',
'workers laborers workers-non fam isyouth',
'workers laborers workers-non fam ls ip',
'workers laborers workers-non fam ls ip f',
'workers laborers workers-non fam num ofw f',
'workers laborers workers-non fam num ip',
'workers laborers workers-non fam num ip f',
'workers laborers workers-non fam num ofw',
'workers laborers workers-non fam num pwd',
'workers laborers workers-non fam num pwd f',
'workers laborers workers-non fam num sr',
'workers laborers workers-non fam num sr f',
'workers laborers workers-non fam num youth',
'workers laborers workers-non fam num youth f',
'workers laborers workers-non fam ofw',
'workers laborers workers-non fam pwd',
'workers laborers workers-non fam srcitizen',
'workers laborers workers-non fam total female',
'workers laborers workers-non fam total male',
'workers laborers workers-non fam year salary female',
'workers laborers workers-non fam year salary male',
'prod cost USER ID',
'prod cost datetime',
'prod cost farmer code',
'prod cost form-remarks',
'prod cost is synced',
'prod cost prodcost-crop cycle year',
'prod cost prodcost-crop harvest',
'prod cost prodcost-is keep record',
'prod cost prodcost-labor crop harvest',
'prod cost prodcost-labor crop maintenance act',
'prod cost prodcost-labor land dev prep',
'prod cost prodcost-labor post harvest act',
'prod cost prodcost-materials act',
'prod cost prodcost-materials land dev prep',
'prod cost prodcost-post harvest act',
'marketing sales USER ID',
'marketing sales datetime',
'marketing sales farmer code',
'marketing sales form-remarks',
'marketing sales is synced',
'marketing sales market-is anchor firm',
'marketing sales market-is anchor firm1',
'marketing sales market-is anchor firm12',
'marketing sales market-is anchor firm123',
'marketing sales market-is coop',
'marketing sales market-is coop1',
'marketing sales market-is coop12',
'marketing sales market-is coop123',
'marketing sales market-is negosyo center',
'marketing sales market-is negosyo center1',
'marketing sales market-is negosyo center12',
'marketing sales market-is negosyo center123',
'marketing sales market-is others',
'marketing sales market-is others1',
'marketing sales market-is others12',
'marketing sales market-is others123',
'marketing sales market-is sme',
'marketing sales market-is sme1',
'marketing sales market-is sme12',
'marketing sales market-is sme123',
'marketing sales market-name anchor firm',
'marketing sales market-name anchor firm1',
'marketing sales market-name anchor firm12',
'marketing sales market-name anchor firm123',
'marketing sales market-name coop',
'marketing sales market-name coop1',
'marketing sales market-name coop12',
'marketing sales market-name coop123',
'marketing sales market-name others',
'marketing sales market-name others1',
'marketing sales market-name others12',
'marketing sales market-name others123',
'marketing sales market-name sme',
'marketing sales market-name sme1',
'marketing sales market-name sme12',
'marketing sales market-name sme123',
'marketing sales market-primary crop buyer others',
'marketing sales market-primary crop buyer others1',
'marketing sales market-primary crop buyer others12',
'marketing sales market-primary crop buyer others123',
'marketing sales market-primary crop dist others',
'marketing sales market-primary crop dist others1',
'marketing sales market-primary crop dist others12',
'marketing sales market-primary crop dist others123',
'marketing sales market-primary crop dist point',
'marketing sales market-primary crop dist point1',
'marketing sales market-primary crop dist point12',
'marketing sales market-primary crop dist point123',
'marketing sales market-primary crop product fgp',
'marketing sales market-primary crop product fgp1',
'marketing sales market-primary crop product fgp12',
'marketing sales market-primary crop product fgp123',
'marketing sales market-primary crop product fgp unit',
'marketing sales market-primary crop product fgp unit1',
'marketing sales market-primary crop product fgp unit12',
'marketing sales market-primary crop product fgp unit123',
'marketing sales market-primary crop type',
'marketing sales market-primary crop type1',
'marketing sales market-primary crop type12',
'marketing sales market-primary crop type123',
'marketing sales market-primary crop type buyer',
'marketing sales market-primary crop type buyer1',
'marketing sales market-primary crop type buyer12',
'marketing sales market-primary crop type buyer123',
'marketing sales market-primary vol del',
'marketing sales market-primary vol del1',
'marketing sales market-primary vol del12',
'marketing sales market-primary vol del123',
'marketing sales record num',
'post harvest USER ID',
'post harvest addr brgy',
'post harvest addr brgy1',
'post harvest addr brgy12',
'post harvest addr city',
'post harvest addr city1',
'post harvest addr city12',
'post harvest addr prov',
'post harvest addr prov1',
'post harvest addr prov12',
'post harvest addr region',
'post harvest addr region1',
'post harvest addr region12',
'post harvest addr street purok sitio',
'post harvest addr street purok sitio1',
'post harvest addr street purok sitio12',
'post harvest datetime',
'post harvest farmer-coords lat',
'post harvest farmer-coords lat1',
'post harvest farmer-coords lat12',
'post harvest farmer-coords long',
'post harvest farmer-coords long1',
'post harvest farmer-coords long12',
'post harvest farmer code',
'post harvest form-remarks',
'post harvest is synced',
'post harvest post harv-capacity',
'post harvest post harv-capacity1',
'post harvest post harv-capacity12',
'post harvest post harv-capacity unit',
'post harvest post harv-capacity unit1',
'post harvest post harv-capacity unit12',
'post harvest post harv-capacity unit time',
'post harvest post harv-capacity unit time1',
'post harvest post harv-capacity unit time12',
'post harvest post harv-ph product form',
'post harvest post harv-ph product form1',
'post harvest post harv-ph product form12',
'post harvest post harv-phcropothers',
'post harvest post harv-phcropothers1',
'post harvest post harv-phcropothers12',
'post harvest post harv-photo',
'post harvest post harv-photo1',
'post harvest post harv-photo12',
'post harvest post harv-type faci equip',
'post harvest post harv-type faci equip1',
'post harvest post harv-type faci equip12',
'post harvest post harv-type faci equip name',
'post harvest post harv-type faci equip name1',
'post harvest post harv-type faci equip name12',
'post harvest record duplicate id',
'post harvest record num',
'access financial USER ID',
'access financial datetime',
'access financial farmer code',
'access financial financial-if loan bank',
'access financial financial-if loan non bank',
'access financial financial-is crop deposit',
'access financial financial-is crop insurance',
'access financial financial-is crop others',
'access financial financial-is crop payments',
'access financial financial-is loan',
'access financial financial-is primary crop distribution',
'access financial financial-is remmitances',
'access financial financial-loan govbank name',
'access financial financial-loan govbank type',
'access financial financial-loan if nonbank others',
'access financial financial-loan name fo',
'access financial financial-loan name lending',
'access financial financial-loan name ngo',
'access financial financial-loan name others',
'access financial financial-loan private name',
'access financial financial-loan private type',
'access financial financial-loan type fo',
'access financial financial-loan type lending',
'access financial financial-loan type ngo',
'access financial financial-loan type others',
'access financial financial-type deposit',
'access financial financial-type deposit bank',
'access financial financial-type deposit non bank',
'access financial financial-type insurance',
'access financial financial-type insurance bank',
'access financial financial-type insurance non bank',
'access financial financial-type others bank',
'access financial financial-type others non bank',
'access financial financial-type payments',
'access financial financial-type payments bank',
'access financial financial-type payments non bank',
'access financial financial-type remmittance name',
'access financial form-remarks',
'access financial is synced',
'feedback USER ID',
'feedback datetime',
'feedback farmer-Banana',
'feedback farmer-Cacao',
'feedback farmer-Calamansi',
'feedback farmer-Coconut',
'feedback farmer-Coffee',
'feedback farmer-Jackfruit',
'feedback farmer-Mango',
'feedback farmer-Other fruits nuts',
'feedback farmer-Others',
'feedback farmer-Pili Nut',
'feedback farmer code',
'feedback feedback-cert acquired',
'feedback feedback-commnets',
'feedback feedback-num of trainings 2 3 years',
'feedback feedback-remarks',
'feedback feedback-support need',
'feedback feedback-type mobile',
'feedback feedback[]-freq',
'feedback feedback[]-freq1',
'feedback feedback[]-freq12',
'feedback feedback[]-freq123',
'feedback feedback[]-freq1234',
'feedback feedback[]-freq12345',
'feedback feedback[]-media',
'feedback feedback[]-media1',
'feedback feedback[]-media12',
'feedback feedback[]-media123',
'feedback feedback[]-media1234',
'feedback feedback[]-media12345',
'feedback is synced',
'feedback record num']
    df=pd.read_csv('exported_file.csv',header=None, skiprows=1,names=header_names)
    writer = pd.ExcelWriter('exported_file.xlsx') 
    df.to_excel(writer, sheet_name='exported_file',index=False )

    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets['exported_file'].set_column(col_idx, col_idx, column_width)

    workbook  = writer.book
    worksheet = writer.sheets['exported_file']
    header_format = workbook.add_format({'bold': True,'text_wrap': True,'valign': 'top','fg_color': '#00cc66','border': 1})
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
    writer.save()
    return send_file('exported_file.xlsx')
    


    

if __name__ == "__main__":
    app.run(debug=True)

    # sample edit