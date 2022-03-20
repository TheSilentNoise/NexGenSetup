from flask import  render_template,jsonify
from app import app
import requests
import json
from models import *


'''
@app.route('/change-password',methods=['POST'])
def change_password():
    user = User.query.filter_by(id=current_user.id).first()
    currentpassword = request.form['currentpassword'];
    newpassword = request.form['newpassword'];
    hashed_password = generate_password_hash(newpassword, method='sha256')
    if (check_password_hash(user.user_password, currentpassword)):
        user = current_user
        user.user_password = hashed_password
        db.session.add(user)
        db.session.commit()
        return "True"
    else:
        return "False"


import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'User':
        return User(obj['name'], obj['username'])
    return obj



@app.route('/users/', defaults={'page_num': 1})
@app.route('/users/<int:page_num>')
def users(page_num):
   users_list = User.query.paginate(per_page=2,page=page_num,error_out=True)
   print(users_list)
   return render_template("users.html",  users=users_list)

from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


@app.route('/users')
def users():
   url = "http://localhost:8888/api/intearn/internship/"
   response = requests.request("GET", url)
   user = response.text
   users = json.loads(user).paginate(per_page=2,page=1,error_out=True)
   print(users)
   pagination = Pagination(4, 2, 2)
   return render_template("users.html",users=users,pagination=pagination)
   

from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args


@app.route('/test2')
def index_1():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    users = api_request_GET("http://127.0.0.1:8888/api/intearn/internship/")
    print(users)
    total = len(users)
    pagination_users = get_users(offset=offset,per_page=per_page)
    pagination = Pagination(page=page,
                            per_page=per_page,
                            total=total,
                            search=False,
                            css_framework='bootstrap4')
    return render_template('users.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )





@app.route('/internship-apply',methods=['GET','POST'])
def internship_apply():
    form = InternshipForm()
    if form.validate_on_submit():
        try:
            date_created = datetime.datetime.now()
            new_msg = Internships(
                                  name = form.name.data,
                                  email = form.email.data,
                                  phone = form.phone.data,
                                  category = form.category.data,
                                  date_created=date_created)
            db.session.add(new_msg)
            db.session.commit()
            message = "Thank you for apply for internships , IEarn Team with get back to you soon !"
            flash(message)
            return redirect(url_for('internships'))
        except Exception as e:
            print("here .. exp")
            message = "Please Try Again !"
            flash(message)
            return redirect(url_for('internships'))
    return render_template('internships-old.html', form=form)


@login_required
@app.route('/profile')
def profile():
    if current_user.is_authenticated:
       userdata = User.query.with_entities(User.user_fname,
                                           User.user_lname,
                                           User.user_email,
                                           User.user_phoneno,
                                           User.date_created)\
                 .filter_by(id=current_user.id).all()
       return render_template('student-profile.html',name=current_user.user_fname,userdata=userdata[0])
    return redirect(url_for('index'))
    
    
    
  

@app.route('/save-profile',methods=['POST'])
def save_profile():
    try :
        fname = request.form['fname'];
        lname = request.form['lname'];
        email = request.form['email'];
        phoneno = request.form['phoneno'];
        user = current_user
        user.user_fname = fname;
        user.user_lname = lname;
        user.user_email = email;
        user.user_phoneno = phoneno;
        db.session.add(user)
        db.session.commit()
        return "True"
    except Exception as e:
        return "False"


   #users = api_request_GET("http://127.0.0.1:8889/api/intearn/internship/")
  #user1 = users["items"]  
    


from app import ma

class CountriesSchema(ma.ModelSchema):
   class Meta:
      model = Countries

@app.route("/country")
def getCountry():
   countries = Countries.query.all()
   countries_schema = CountriesSchema(many=True)
   countryJson = countries_schema.dump(countries)
   return jsonify(countryJson.data)


'''