import socket

host_name = socket.gethostname()
IP_address = socket.gethostbyname(host_name)



# --- SYSTEM CONFIG --- #
SECRET_KEY = "@002342562988603673976#131452@HHPLHKHHH"
# HOST = host_name
HOST = "0.0.0.0"
CUSTOM_HOST = "192.168.0.1"
PORT = 5000
_PORT = 5000
IS_DEBUG = True

SQLITE_DB_LOCAL = "assets/DB/dti_rapidxi.db"
SQLITE_DB_SERVER = "/home/dtirapid/DTI-Web-App/assets/DB/dti_rapidxi.db"

RECORDS_SERVER = "/home/dtirapid/DTI-Web-App/assets/records/"
# SQLITE_DB_SERVER = "/home/crisnotbrown/DTI-Web-App/assets/DB/dti_rapidxi.db"
SQLITE_DB = "none"

RECORDS_LOCAL = "assets/records/"
SQLITE_DB_SERVER = "/home/dtirapid/DTI-Web-App/assets/DB/dti_rapidxi.db"

RECORDS_SERVER = "/home/dtirapid/DTI-Web-App/assets/records/"
# RECORDS_SERVER = "/home/crisnotbrown/DTI-Web-App/assets/records/"
RECORDS = "none"


M_APPVER_LOCAL = ""
M_APPVER_SERVER = "/home/dtirapid/DTI-Web-App/"
# M_APPVER_SERVER = "/home/crisnotbrown/DTI-Web-App/"
M_APPVER = "none"
# --- DATABASE---- #

LOCAL_PORT=3306
LOCAL_HOST = "localhost"
LOCAL_USER = "root"
LOCAL_PASSWORD = ""
LOCAL_DATABASE = "dti_rapidxi"

SERVER_PORT=3306
SERVER_HOST = "172.26.158.126"
SERVER_USER = "rapid_apps"
SERVER_PASSWORD = "none"
SERVER_DATABASE = "dti_rapidxi"


# {
# 	"font_size": 8,
# 	"ignored_packages":
# 	[
# 		"Vintage",
# 	],
# 	"theme": "Adaptive.sublime-theme",
# 	"color_scheme": "Monokai.sublime-color-scheme",
# 	"spell_check": true,
# 	"drag_text": false,
# 	"show_tab_close_buttons": false,
# 	"hide_new_tab_button": true,
# 	"show_encoding": true,
# 	"show_line_endings": true,
# 	// "show_full_path": false,
# 	"show_rel_path": true,
# 	"show_project_first": true,
# }
