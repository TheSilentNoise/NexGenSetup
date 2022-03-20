from flask import render_template,redirect,url_for,request,json,flash,abort
from app import app
import datetime
from forms import *
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from sqlalchemy import desc
from models import db
from werkzeug.utils import secure_filename
import sys,os

from utils import *

from itsdangerous import URLSafeTimedSerializer
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


from flask import session


headers = {'content-type': "application/json"}

@login_required
@app.route('/student-profile' ,methods = ['GET', 'POST'])
def student_profile():
    form = StudentDetailsForm()
    profile_img = STUDENT_DEFAULT_IMG
    student = Student.query.filter_by(fk_user_id=current_user.id).first()

    form.user_fname.data = current_user.user_fname
    form.user_lname.data = current_user.user_lname
    form.user_phoneno.data = current_user.user_phoneno

    if student is not None:

        form.linkedin_url.data = student.linkedin_url
        form.gender.data = student.gender
        form.date_of_birth.data = student.date_of_birth
        form.address.data = student.address
        form.city.data = student.city
        form.state.data = student.state
        form.country.data = student.country
        form.company_name.data = student.company_name
        form.industry_type.data = student.industry_type
        form.designation.data = student.designation
        form.experience.data = student.experience
        form.skills.data = student.skills
        form.year_of_passing.data = student.year_of_passing
        form.institution_name.data = student.institution_name
        form.department.data = student.department
        form.qualification.data = student.qualification

        profile_img = student.profile_image_path

        if (profile_img is None) or (profile_img is ""):
            profile_img = STUDENT_DEFAULT_IMG

    if form.validate_on_submit():

        if student is not None:
            form.linkedin_url.data = student.linkedin_url
            form.gender.data = student.gender
            form.date_of_birth.data = student.date_of_birth
            form.address.data = student.address
            form.city.data = student.city
            form.state.data = student.state
            form.country.data = student.country
            form.company_name.data = student.company_name
            form.industry_type.data = student.industry_type
            form.designation.data = student.designation
            form.experience.data = student.experience
            form.skills.data = student.skills
            form.year_of_passing.data = student.year_of_passing
            form.institution_name.data = student.institution_name
            form.department.data = student.department
            form.qualification.data = student.qualification

            form = StudentDetailsForm()

            # update user

            user = current_user
            user.user_fname = form.user_fname.data;
            user.user_lname = form.user_lname.data;
            user.user_phoneno = form.user_phoneno.data;
            db.session.add(user)
            db.session.commit()

            # update student

            student.linkedin_url = form.linkedin_url.data;
            student.gender = form.gender.data;
            student.date_of_birth = form.date_of_birth.data;
            student.address = form.address.data;
            student.city = form.city.data;
            student.state = form.state.data;
            student.country = form.country.data;
            student.company_name = form.company_name.data;
            student.industry_type = form.industry_type.data;
            student.designation = form.designation.data;
            student.experience = form.experience.data;
            student.skills = form.skills.data;
            student.institution_name = form.institution_name.data;
            student.department = form.department.data;
            student.year_of_passing = form.year_of_passing.data;
            student.qualification = form.qualification.data;
            student.last_updated = datetime.datetime.now();

            db.session.add(student)
            db.session.commit()
            flash("Data saved sucessfully!")
            return render_template('student-profile.html', form=form,profile_img=profile_img)

        else:
            # insert
            new_student = Student(
                fk_user_id=current_user.id,
                linkedin_url=form.linkedin_url.data,
                gender = form.gender.data,
                date_of_birth=form.date_of_birth.data,
                address =form.address.data,
                city=form.city.data,
                state=form.state.data,
                country=form.country.data,
                company_name=form.company_name.data,
                industry_type=form.industry_type.data,
                designation=form.designation.data,
                experience=form.experience.data,
                skills=form.skills.data,
                institution_name=form.institution_name.data,
                department=form.department.data,
                year_of_passing = form.year_of_passing.data,
                qualification = form.qualification.data,
                last_updated=datetime.datetime.now()
            )

            db.session.add(new_student)
            db.session.commit()
            flash("Data saved sucessfully!")
            return render_template('student-profile.html', form=form ,profile_img=profile_img)
    return render_template('student-profile.html' ,form=form ,profile_img=profile_img)


@app.route('/upload-profile-img' ,methods = ['POST'])
def upload_img():
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('Please select a file !')
        elif file.filename == '':
            flash('Please select a file !')
        elif file and allowed_img(file.filename):
            student = Student.query.filter_by(fk_user_id=current_user.id).first()
            filename = student.pk_student_id +"_"+secure_filename(file.filename)
            imgpath = os.path.join(STUDENT_IMG_UPLOAD_FOLDER, filename)
            file.save(imgpath)
            if student is not None:
                student.profile_image_path = STUDENT_IMG_SERVER + filename
                student.last_updated = datetime.datetime.now();
                db.session.add(student)
                db.session.commit()
            flash('Image has been saved !')
            return redirect(url_for('student_profile'))
        else:
            flash('File format is not allowded!')
    return redirect(url_for('student_profile'))



@app.route('/upload' ,methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('Please select a file !')
        elif file.filename == '':
            flash('Please select a file !')
        elif file and allowed_file(file.filename):
            student = Student.query.filter_by(fk_user_id=current_user.id).first()
            filename = student.pk_student_id +"_"+secure_filename(file.filename)
            imgpath = os.path.join(STUDENT_RESUME_UPLOAD_FOLDER, filename)
            file.save(imgpath)
            if student is not None:
                student.resume_path = STUDENT_FILE_SERVER + filename
                student.last_updated = datetime.datetime.now();
                db.session.add(student)
                db.session.commit()
            flash('File has been saved !')
            return redirect(url_for('student_profile'))
        else:
            flash('File format is not allowded!')
    return redirect(url_for('student_profile'))




@app.route('/apply-internship')
def apply_internship():
    student = Student.query.filter_by(fk_user_id=current_user.id).first()
    pk_internship_id = request.args['pk_internship_id']
    if student is not None:
        pk_student_id = student.pk_student_id
        payload =  {
                        "fk_student_id": pk_student_id,
                        "fk_internship_id": pk_internship_id
                   }
        json_data = json.dumps(payload)
        print (json_data)
        response = requests.request("POST",
                                    STUDENT_INTERNSHIP_APPLICATION_URL,
                                    data=json_data,headers=headers)
        print (response.status_code)
        if (response.status_code == 201):
            flash('You have successfully applied.')
            return redirect(url_for('internship_details', id=pk_internship_id))
        else:
            flash('You have already applied this !')
            return redirect(url_for('internship_details', id=pk_internship_id))
    else:
        flash('Please update your profile .. !')
        return redirect(url_for('internship_details', id=pk_internship_id))



@app.route('/myinternships')
def my_internships():
    if (current_user.has_role() == 1):
        student = Student.query.filter_by(fk_user_id=current_user.id).first()
        if student is not None:
            applications = api_request_GET(STUDENT_INTERSHIP_APPLICATION_URL + student.pk_student_id)
            #print(applications)
            return render_template('internships/my-internships.html', applications=applications)
        else:
            return render_template('internships/my-internships.html')
    else:
        abort(404)