import subprocess
DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/Practice'

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@13.57.23.191/dev_iearn_intern'

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://intern_admin:Admin123@54.219.154.147/dev_iearn_intern'
ip = subprocess.getoutput('wget -qO - http://169.254.169.254/latest/meta-data/public-ipv4')
sql_user='prod_user'
sql_pass='ProdP@$$+'
sql_db='prod_iearn_tech'
#print(ip)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+sql_user+':'+sql_pass+'@'+ip+'/'+sql_db
SECRET_KEY = "www.iearn.tech-2018"

SQLALCHEMY_TRACK_MODIFICATIONS = True

USER_ENABLE_EMAIL = True

#PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)

MAX_CONTENT_LENGTH = 6 * 1024 * 1024 # 6 MB
