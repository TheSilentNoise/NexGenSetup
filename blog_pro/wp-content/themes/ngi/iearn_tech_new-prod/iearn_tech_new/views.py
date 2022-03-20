from flask import render_template,redirect,url_for,request,json,flash
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


#### login_manager

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response



@app.errorhandler(404)
def page_not_found(e):
    if current_user.is_authenticated:
        return render_template('404.html',name=current_user.user_fname), 404
    return render_template('404.html') , 404



import courses,blogs,materials,forums,employer,student,test


############ login ,registration ###############





@app.route('/')
def index():
    session.permanent = True
    #print(current_user.has_role())
    activecourses = Courses.query.with_entities(Courses.course_name,
                                                Courses.course_img_url,
                                                Courses.course_duration,
                                                Courses.course_fees,
                                                Courses.course_mode,
                                                Courses.course_details_url,
                                                Courses.course_description) \
        .filter_by(isActive=1).order_by(desc(Courses.date_created)).limit(3).all()

    activeCourseList = []
    for course in activecourses:
        activeCourseList.append(course)

    blogs = Blogs.query.with_entities(Blogs.blog_name,
                                      Blogs.blog_url,
                                      Blogs.blog_description,
                                      Blogs.date_created
                                      ).order_by(desc(Blogs.date_created)).limit(4).all()
    blog_lists = []
    for blog in blogs:
        blog_lists.append(blog)

    othercourses = Courses.query.with_entities(Courses.course_name,
                                               Courses.course_img_url,
                                               Courses.course_duration,
                                               Courses.course_fees,
                                               Courses.course_mode,
                                               Courses.course_details_url,
                                               Courses.course_description) \
        .filter_by(isActive=0).order_by(desc(Courses.date_created)).limit(3).all()
    otherCourseList = []
    for course in othercourses:
        otherCourseList.append(course)

    return render_template('index.html',blog_lists=blog_lists,
                           activeCourseList=activeCourseList,
                           otherCourseList=otherCourseList)




@app.route('/login',methods=['GET','POST'])
def login():
     if not current_user.is_authenticated:
        form = Loginform()
        if form.validate_on_submit():
            user = User.query.filter_by(user_email=form.email.data).first()
          #  role = User_Role.query.with_entities(User_Role.role_id).filter_by(user_id=user.id).first()
            if user:
                if check_password_hash(user.user_password,form.password.data):
                    login_user(user,remember=form.remember.data)
                    user = current_user
                    current_datetime = datetime.datetime.now()
                    user.last_login = current_datetime
                    db.session.add(user)
                    db.session.commit()
                   # session['role_id'] = role_id
                    return redirect(url_for('index'))
            return render_template('login.html',form=form,message="Incorrect username or password")
        return render_template('login.html',form=form)
     return redirect((url_for('index')))



@app.route('/reset-password',methods=['GET','POST'])
def reset_password():
    if not current_user.is_authenticated:
        forgot_pass_form = ForgotPasswordForm()
        if forgot_pass_form.validate_on_submit():
            email = forgot_pass_form.email.data
            user = User.query.filter_by(user_email=email).first()
            if user is not None:
                token = ts.dumps(user.user_email, salt='recover-key')
                recover_url = url_for('reset_with_token',token=token,_external=True)

                subject = "Password Reset Requested | IEarn.Tech"
                html = "reset-password.html"
                send_mail(subject, email, recover_url, html)
                message="You will receive an email to reset your password in a few minutes."
                flash(message)
                return render_template('forgot-password.html',form=forgot_pass_form)
            else:
                message = "Your email id doesn't exists!"
                flash(message)
                render_template('forgot-password.html',form=forgot_pass_form)
        else:
            return render_template('forgot-password.html', form=forgot_pass_form)
    return render_template('forgot-password.html', form=forgot_pass_form)




@app.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    email = ts.loads(token, salt="recover-key", max_age=86400)
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=email).first()
        hashed_password = generate_password_hash(form.user_password.data, method='sha256')
        user.user_password = hashed_password
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('reset-password.html', form=form,token=token)




@app.route('/signup',methods=['GET','POST'])
def signup():
        form = Registrationform()
        if form.validate_on_submit():
            try:
                hashed_password = generate_password_hash(form.user_password.data, method='sha256')
                date_created = datetime.datetime.now()
                role_id = int(form.user_role.data)
                new_user = User(
                    user_fname=form.user_fname.data,
                    user_lname=form.user_lname.data,
                    user_email=form.user_email.data,
                    user_phoneno=form.user_phoneno.data,
                    user_password=hashed_password,
                    date_created=date_created,
                    last_login = date_created,
                    user_status=1)
                db.session.add(new_user)
                db.session.commit()
                #user_id = User.query.with_entities(User.id).order_by(desc(User.id)).first()
                user_role = User_Role(
                    user_id=new_user.id,
                    role_id=role_id
                )
                db.session.add(user_role)
                db.session.commit()

                try:
                    subject = "Welcome Mail from IEarn.Tech"
                    recipients = form.user_email.data
                    url=None
                    html="welcome-mail.html"
                    send_mail(subject, recipients, url, html)
                except Exception as e:
                   # print("mail not sent..")
                   return render_template('signup.html', form=form, error_msg="Email not sent !!")
                return redirect( url_for('login'))
            except Exception as e:
                return render_template('signup.html', form=form, error_msg="Username already exists!!")
        return render_template('signup.html',form=form)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))




@app.route('/contactus',methods=['GET','POST'])
def contactus():
    form = ContactUsForm()
    if form.validate_on_submit():
        try:
            date_created = datetime.datetime.now()
            new_msg = Contactus(
                                  name = form.name.data,
                                  email = form.email.data,
                                  subject = form.subject.data,
                                  message = form.message.data,
                                  date_created=date_created)
            db.session.add(new_msg)
            db.session.commit()
            message = "Thank you for contacting us , IEarn Team with get back to you soon !"
            flash(message)
            return redirect(url_for('contact'))
        except Exception as e:
            message = "Please Try Again !"
            flash(message)
            return redirect(url_for('contact'))
    return render_template('contact.html', form=form)



@app.route('/contact')
def contact():
    form = ContactUsForm()
    return render_template('contact.html',form=form)




@app.route('/job-apply',methods=['GET','POST'])
def jobs_apply():
    form = JobForm()
    if form.validate_on_submit():
        try:
            date_created = datetime.datetime.now()
            new_msg = Jobs(
                                  name = form.name.data,
                                  email = form.email.data,
                                  phone = form.phone.data,
                                  category = form.category.data,
                                  linkedinurl = form.linkedinurl.data,
                                  date_created=date_created)
            db.session.add(new_msg)
            db.session.commit()
            message = "Thank you for apply for jobs , IEarn Team with get back to you soon !"
            flash(message)
            return redirect(url_for('jobs'))
        except Exception as e:
            message = "Please Try Again !"
            flash(message)
            return redirect(url_for('jobs'))
    return render_template('jobs.html', form=form)



@app.route('/jobs')
def jobs():
    form = JobForm()
    if current_user.is_authenticated:
      return render_template('jobs.html',form=form)
    return render_template('jobs.html',form=form)



@app.route('/freelance-apply',methods=['GET','POST'])
def freelance_apply():
    form = FreelanceForm()
    if form.validate_on_submit():
        try:
            date_created = datetime.datetime.now()
            new_msg = freelance(
                                  name = form.name.data,
                                  email = form.email.data,
                                  phone = form.phone.data,
                                  category = form.category.data,
                                  linkedinurl = form.linkedinurl.data,
                                  hours = form.hours.data,
                                  date_created=date_created)
            db.session.add(new_msg)
            db.session.commit()
            message = "Thank you for apply for freelancing , IEarn Team with get back to you soon !"
            flash(message)
            return redirect(url_for('freelancer'))
        except Exception as e:
            message = "Please Try Again !"
            flash(message)
            return redirect(url_for('freelancer'))
    return render_template('freelancer.html', form=form)



@app.route('/freelancer')
def freelancer():
    form = FreelanceForm()
    if current_user.is_authenticated:
      return render_template('freelancer.html',name=current_user.user_fname,form=form)
    return render_template('freelancer.html',form=form)




@app.route('/user-email-subscription',methods=['POST'])
def user_email_subscription():
    try:
        user_email = request.form['subs_email'];
        date_created = datetime.datetime.now()
        new_subscriber = Subscription(user_email=user_email,date_created=date_created)
        db.session.add(new_subscriber)
        db.session.commit()
        return "True"
    except Exception as e:
        return "False"



@login_required
@app.route('/user-course-feedback', methods=['POST'])
def user_course_feedback():
        try:
            user_id = current_user.id;
            course_id = request.form['course_id'];
            date_created = datetime.datetime.now()
            content_rating = request.form['content_rating'];
            overall_rating = request.form['overall_rating'];
            instructor_rating = request.form['instructor_rating'];
            comments = request.form['comments'];

            add_feedback = Course_Feedback(
                user_id=user_id,
                course_id=course_id,
                content_rating=content_rating,
                instructor_rating=instructor_rating,
                overall_rating=overall_rating,
                comments=comments,
                date_created=date_created)

            db.session.add(add_feedback)
            db.session.commit()
            return "True"
        except Exception as e:
            return "False"

####### user profile ########


@login_required
@app.route('/change-password',methods=['GET','POST'])
def change_pass():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        hashed_password = generate_password_hash(new_password, method='sha256')

        if (check_password_hash(current_user.user_password, current_password)):
            user = current_user
            user.user_password = hashed_password
            db.session.add(user)
            db.session.commit()
            flash('Password updated successfully !')
        else:
            flash("Current password does not match !")
    return render_template('change-password.html',form=form)



@app.route('/videos')
def videos():
      print("video")
      return render_template('videos.html')





