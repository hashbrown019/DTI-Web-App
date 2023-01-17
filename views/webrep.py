from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask_session import Session
import Configurations as c


app = Blueprint("webrep",__name__,static_folder='templates/webrep/')



class _main:
	def is_on_session(): return ('USER_DATA' in session)

	def __init__(self, arg):super(_main, self).__init__();self.arg = arg


	# ======================================================================================================

	@app.route("/webrep",methods=["POST","GET"])
	def home():
		return render_template("webrep/home.html")



	@app.route("/rapid/knowledgecenter/<page>",methods=["POST","GET"])
	def knowledgecenter(page):
		print(page)
		return render_template("webrep/knowledgecenter/{}".format(page))


	@app.route("/rapid/publications/<page>",methods=["POST","GET"])
	def publications(page):
		print(page)
		return render_template("webrep/publications/{}".format(page))


	@app.route("/rapid/whatwedo/<page>",methods=["POST","GET"])
	def whatwedo(page):
		print(page)
		return render_template("webrep/whatwedo/{}".format(page))


	@app.route("/rapid/wherewework/<page>",methods=["POST","GET"])
	def wherewework(page):
		print(page)
		return render_template("webrep/wherewework/{}".format(page))


	@app.route("/rapid/whoweare/<page>",methods=["POST","GET"])
	def whoweare(page):
		print(page)
		return render_template("webrep/whoweare/{}".format(page))



		# /rapid/whatwedo/