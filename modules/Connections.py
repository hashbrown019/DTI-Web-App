import mysql.connector as connects
import sqlite3
import socket

class sqlite:
	def __init__(self, database):
		super(sqlite, self).__init__()
		self.database=database

	def init_db(self):
		print(self)
		conn = None
		try:
			conn = sqlite3.connect(self.database)
		except Exception as e:
			print(e)
			print("======== ERROR IN SQLITE INITIALIZATION  ========")
		return conn

	def do(self,sql):
		conn = sqlite.init_db(self)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		return cur.lastrowid

	def select(self,sql):
		conn = sqlite.init_db(self)
		cur = conn.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		return rows
		
	def dict_factory(cursor, row):
	    d = {}
	    for idx, col in enumerate(cursor.description):
	        d[col[0]] = row[idx]
	    return d

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
