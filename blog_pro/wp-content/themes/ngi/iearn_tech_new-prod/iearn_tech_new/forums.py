
from flask import render_template,redirect,url_for,request,json,flash
from app import app
import datetime
from flask_mail import Message
from app import db,mail
from forms import *
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from sqlalchemy import desc
from models import db



@app.route('/forums')
def forums():
    #form = ContactUsForm()
    if current_user.is_authenticated:
      return render_template('forums.html',name=current_user.user_fname)
    return render_template('forums.html')


