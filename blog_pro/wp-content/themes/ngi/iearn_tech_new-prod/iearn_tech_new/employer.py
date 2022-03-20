import os
from flask import json,abort,request,flash,redirect,url_for
from app import app
import datetime
from forms import *
from flask_login import current_user,login_required
from models import db
import requests
from werkzeug.utils import secure_filename
from flask_paginate import Pagination, get_page_args
from functools import wraps

#import socket
#socket.getaddrinfo('127.0.0.1', 8889)


### Employer Profile

@login_required
@app.route('/employers-profile',methods = ['GET', 'POST'])
def employers_profile():

    if(current_user.has_role() == 2):

        form = EmployerDetailsForm()
        logo = EMPLOYER_DEFAULT_IMG
        employer = Employer.query.filter_by(fk_user_id=current_user.id).first()

        form.user_fname.data = current_user.user_fname
        form.user_lname.data = current_user.user_lname
        form.user_phoneno.data = current_user.user_phoneno

        if employer is not None:
            form.linkedin_url.data = employer.linkedin_url
            form.company_name.data = employer.company_name
            form.company_url.data = employer.company_url
            form.industry_type.data = employer.industry_type
            form.head_count.data = employer.head_count
            form.established_year.data = employer.established_year
            form.company_info.data = employer.company_info
            form.company_address.data = employer.company_address
            form.city.data = employer.city
            form.state.data = employer.state
            form.country.data = employer.country

            logo = employer.logo_path

            if (logo is  None) or (logo is "") :
                logo = EMPLOYER_DEFAULT_IMG

        if form.validate_on_submit():
            if employer is not None:
                form.linkedin_url.data = employer.linkedin_url
                form.company_name.data = employer.company_name
                form.company_url.data = employer.company_url
                form.industry_type.data = employer.industry_type
                form.head_count.data = employer.head_count
                form.established_year.data = employer.established_year
                form.company_info.data = employer.company_info
                form.company_address.data = employer.company_address
                form.city.data = employer.city
                form.state.data = employer.state
                form.country.data = employer.country
                form = EmployerDetailsForm()

                # update user
                user = current_user
                user.user_fname = form.user_fname.data;
                user.user_lname = form.user_lname.data;
                user.user_phoneno = form.user_phoneno.data;
                db.session.add(user)
                db.session.commit()

                # update employer
                employer.linkedin_url = form.linkedin_url.data;
                employer.company_name = form.company_name.data;
                employer.company_url = form.company_url.data;
                employer.industry_type = form.industry_type.data;
                employer.head_count = form.head_count.data;
                employer.established_year = form.established_year.data;
                employer.company_info = form.company_info.data;
                employer.company_address = form.company_address.data;
                employer.city = form.city.data;
                employer.state = form.state.data;
                employer.country = form.country.data;
                employer.last_updated = datetime.datetime.now();
                db.session.add(employer)
                db.session.commit()
                flash("Data saved sucessfully!")
                return render_template('employer/employer-profile.html',form=form,logo=logo)
            else:
                # insert
                new_employer = Employer(
                        fk_user_id=current_user.id,
                        linkedin_url=form.linkedin_url.data,
                        company_name=form.company_name.data,
                        company_url=form.company_url.data,
                        industry_type=form.industry_type.data,
                        head_count=form.head_count.data,
                        established_year=form.established_year.data,
                        company_info=form.company_info.data,
                        company_address=form.company_address.data,
                        city=form.city.data,
                        state=form.state.data,
                        country=form.country.data,
                        verified=0,
                        last_updated=datetime.datetime.now()
                )
                db.session.add(new_employer)
                db.session.commit()
                flash("Data saved sucessfully!")
                return render_template('employer/employer-profile.html', form=form,logo=logo)
        return render_template('employer/employer-profile.html',form=form,logo=logo)
    else:
        abort(404)


@app.route('/upload-logo',methods = ['POST'])
def upload_logo():
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('Please select a file !')
        elif file.filename == '':
            flash('Please select a file !')
        elif file and allowed_img(file.filename):
            employer = Employer.query.filter_by(fk_user_id=current_user.id).first()
            filename = employer.pk_employer_id +"_"+secure_filename(file.filename)
            imgpath = os.path.join(EMPLOYER_IMG_UPLOAD_FOLDER, filename)
            file.save(imgpath)
            if employer is not None:
                employer.logo_path = EMPLOYER_IMG_SERVER + filename
                employer.last_updated = datetime.datetime.now();
                db.session.add(employer)
                db.session.commit()
            flash('Logo has been saved !')
            return redirect(url_for('employers_profile'))
        else:
            flash('File format is not allowded!')
    return redirect(url_for('employers_profile'))




@login_required
@app.route('/employers-offers',methods = ['GET', 'POST'])
def employer_offers():
    if (current_user.has_role() == 2):
        form = InternshipPostForm()
        employer = Employer.query.filter_by(fk_user_id=current_user.id).first()
        if employer is not None:
            if form.validate_on_submit():
                payload = {
                        "start_date": str(form.startDate.data),
                        "contact_email": form.contactEmail.data,
                        "last_application_date": str(form.lastApplicationDate.data),
                        "state": form.state.data,
                        "compensation": form.compensation.data,
                        "fk_employer_id": employer.pk_employer_id,
                        "experience": form.experience.data,
                        "city": form.city.data,
                        "publish_date": datetime.datetime.now(),
                        "address": form.address.data,
                        "skills": form.skills.data,
                        "description": form.description.data,
                        "paid_type": form.paidType.data,
                        "stream": form.stream.data,
                        "title": form.title.data,
                        "qualification": form.qualification.data,
                        "contact_phone": form.contactPhone.data,
                        "position": form.designation.data,
                        "internship_type": form.internshipType.data,
                        "end_date": str(form.endDate.data),
                        "country": form.country.data
                }
                headers = {'content-type': "application/json"}
                json_data = json.dumps(payload)
                response = requests.request("POST", EMPLOYER_OFFER_POSTS_URL, data=json_data, headers=headers)
                if (response.status_code == 201):
                    flash("Your offer is sucessfuly posted!")
                else:
                    flash("Something went wrong ! Please try again.")
                return redirect(url_for('employer_offers'))
            return render_template('employer/employer-offers-post.html',form=form)
        else:
            flash("Please update your profile!")
            return render_template('employer/employer-offers-post.html', form=form)
    else:
        abort(404)




### view all internships


def get_internships(internships,offset=0, per_page=10):
  return internships[offset: offset + per_page]



@app.route('/internships')
def internships():
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        internships = api_request_GET(VIEW_ALL_INTERNSHIPS_URL)
        total = len(internships)
        pagination_internships = get_internships(internships,offset=offset, per_page=per_page)
        pagination = Pagination(page=page,per_page=per_page,total=total,search=False,
                                css_framework='bootstrap4')
        return render_template('internships/internships.html',internships=pagination_internships,
                               page=page,per_page=per_page,pagination=pagination)



##### view internship details


@app.route('/internship/id=<id>')
def internship_details(id):
    isapplied = False
    url = VIEW_INTERNSHIP_DETAILS_URL + str(id)
    response = requests.request("GET", url)
    internship = response.text
    internshipJson = json.loads(internship)
    if (current_user.is_authenticated):
        student = Student.query.filter_by(fk_user_id=current_user.id).first()
        if student is not None:
            internships = InternApplication.query. \
                filter_by(fk_student_id=student.pk_student_id, fk_internship_id=id).first()
            if internships is not None:
                isapplied = True
        return render_template("internships/internship-details.html", internshipJson=internshipJson,isapplied=isapplied)
    else:
        return render_template("internships/internship-details.html", internshipJson=internshipJson)





@app.route('/applicants')
def applicant_details():
    if (current_user.has_role() == 2):
        employer = Employer.query.filter_by(fk_user_id=current_user.id).first()
        if employer is not None:
            applicants = api_request_GET(EMPLOYER_APPLICANT_DETAILS_URL +employer.pk_employer_id)
            return render_template('employer/employer-applicants.html', applicants=applicants)
        else:
            return render_template('employer/employer-applicants.html')
    else:
        abort(404)


@app.route('/myoffers')
def employer_myoffers():
    if (current_user.has_role() == 2):
        employer = Employer.query.filter_by(fk_user_id=current_user.id).first()
        if employer is not None:
            offers = api_request_GET(EMPLOYER_INTERNSHIP_OFFER_URL + employer.pk_employer_id)
            print(offers)
            return render_template('employer/employer-offers.html', offers=offers)
        else:
            return render_template('employer/employer-offers.html')
    else:
        abort(404)










