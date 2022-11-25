from flask import Flask, Blueprint, render_template, url_for, json, jsonify, send_file
import urllib.request
import pandas as pd

app = Blueprint("excel_migration",__name__)

@app.route('/excel_main/<num_entries>')
def index():
    # get_url= urllib.request.urlopen('https://dtirapid.pythonanywhere.com/api/v2/sample')
    # print("Response Status: "+ str(get_url.getcode()) )
    # _DATA_ = json.loads(get_url.read())
    df = pd.read_json (r'https://dtirapid.pythonanywhere.com/api/v2/sample/')
    df.to_csv (r'exported_file.csv', index = 'profile__farmer_code')
    
    # return send_file('exported_file.csv')
    return "DONE :::::"


    

if __name__ == "__main__":
    app.run(debug=True)

    # sample edit