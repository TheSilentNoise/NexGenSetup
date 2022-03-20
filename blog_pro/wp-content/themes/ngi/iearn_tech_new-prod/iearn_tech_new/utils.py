from flask import render_template,json
from app import mail
from forms import *
from flask_mail import Message
import requests
import subprocess
import models

ip = subprocess.getoutput('wget -qO - http://169.254.169.254/latest/meta-data/public-ipv4')
print(ip)
INTERNSHIP_HOST = "http://"+ip+":8889" #change

IMG_UPLOAD_SERVER = 'http://'+ip+':9090'  #change

#IMG_SERVER_PATH = '/home/nivedita/Softwares/apache-tomcat-8.5.23/webapps/ROOT' #change

IMG_SERVER_PATH = '/opt/tomcat/latest/webapps/ROOT'



############################### INTERNSHIP API Url


EMPLOYER_OFFER_POSTS_URL = INTERNSHIP_HOST+"/intearn/internship/"

VIEW_ALL_INTERNSHIPS_URL = INTERNSHIP_HOST+"/intearn/internship/"

VIEW_INTERNSHIP_DETAILS_URL = INTERNSHIP_HOST+"/intearn/internship/"

STUDENT_INTERNSHIP_APPLICATION_URL = INTERNSHIP_HOST + "/intearn/application/intern"

EMPLOYER_APPLICANT_DETAILS_URL = INTERNSHIP_HOST + "/intearn/employers/intern/applicants/"

STUDENT_INTERSHIP_APPLICATION_URL = INTERNSHIP_HOST + "/intearn/students/internships/"

EMPLOYER_INTERNSHIP_OFFER_URL = INTERNSHIP_HOST + "/intearn/employers/internships/"



######################################################################################


EMPLOYER_DEFAULT_IMG="../static/img/icon/company-logo.png"

STUDENT_DEFAULT_IMG="../static/img/icon/profile.png"


## File Upload


EMPLOYER_IMG_UPLOAD_FOLDER =  IMG_SERVER_PATH + '/image/employer/'

STUDENT_IMG_UPLOAD_FOLDER = IMG_SERVER_PATH + '/image/student'

STUDENT_RESUME_UPLOAD_FOLDER = IMG_SERVER_PATH + '/image/student'

IMG_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

FILE_ALLOWED_EXTENSIONS = set(['pdf','docx'])


EMPLOYER_IMG_SERVER = IMG_UPLOAD_SERVER +'/image/employer/'

STUDENT_IMG_SERVER = IMG_UPLOAD_SERVER +'/image/student/'

STUDENT_FILE_SERVER = IMG_UPLOAD_SERVER +'/file/student/'


def allowed_img(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMG_ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_ALLOWED_EXTENSIONS







#### Email-Sender

sender='admin@iearn.tech'

def send_mail(subject,recipients,url,html):
    message = Message(subject,
                      sender=sender,
                      recipients=[recipients])
    message.html = render_template('mail/'+html,
                                   recover_url=url,
                                   email=recipients)
    mail.send(message)




#### populate user_role_type_dropdown

user_role = Role.query.with_entities(Role.id,Role.role_name).all()

user_role_list = []
user_role_list.append(('', '--Select Category--'))
for i in user_role:
    role_tup = (str(i.id), i.role_name)
    user_role_list.append(role_tup)




def api_request_GET(url):
    res = requests.request("GET", url)
    response = json.loads(res.text)
    return response
