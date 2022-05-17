import mysql.connector as connects
import sqlite3
import socket

class sqlite:
	def init_db(db):
		conn = None
		try:
			conn = sqlite3.connect(db)
		except Error as e:
			print(e)
		return conn

	def do(sql):
		conn = sqlite.init_db()
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		return cur.lastrowid

	def select(sql):
		conn = sqlite.init_db()
		cur = conn.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		return rows

class mysql:
	def __init__(self, host,user,password,database):
		super(mysql, self).__init__()
		self.host=host
		self.user=user
		self.password=password
		self.database=database
		
	def init_db(self):
		hostname = socket.gethostname()
		ip_address = socket.gethostbyname(hostname)
		mydb = connects.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database)
		return mydb

	def do(self,sql):
		conn = mysql.init_db(self)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		return cur.lastrowid

	def select(self,sql):
		conn = mysql.init_db(self)
		cur = conn.cursor(dictionary=True)
		cur.execute(sql)
		rows = cur.fetchall()
		return rows
