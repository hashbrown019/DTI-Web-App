from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connections import mysql
import Configurations as c
import os
import json

app = Blueprint("api",__name__)

rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)

farm_details = None

class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg

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
