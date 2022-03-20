from flask import render_template,redirect,url_for,request
from app import app
import datetime
from flask_mail import Message
from app import db,mail
from forms import *
from flask_login import login_required,current_user
from sqlalchemy import desc
from models import db




@app.route('/enroll-now',methods=['GET','POST'])
def enroll_now():
    if current_user.is_authenticated:
        try:
            username = current_user.user_fname
            course_id = request.args.get('course_id', type=int)
            print(course_id)
            user_id = current_user.id
            date_created = datetime.datetime.now()
            user_course = User_Course(user_id=user_id,
                                      course_id=course_id,
                                      date_created=date_created)
            db.session.add(user_course)
            db.session.commit()
            coursename = Courses.query.with_entities(Courses.course_name).filter_by(id=course_id).first()
            subject = "You are now enrolled in " + str(coursename[0])
            print(subject)
            try:
                msg = Message(subject, sender='admin@iearn.tech', recipients=[current_user.user_email])
                msg.html = render_template('mail/enrollment-success.html',coursename=coursename[0],username=username)
                mail.send(msg)
            except Exception as e:
                print("mail not sent..")
            return redirect(url_for('mycourses'))
        except Exception as e:
            return redirect(url_for('courses'))
    return redirect(url_for('courses'))





@login_required
@app.route('/mycourses')
def mycourses():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
      no_of_course = User_Course.query.with_entities(User_Course.course_id).filter_by(user_id=current_user.id).count()
      if no_of_course == 0:
          return render_template('mycourses.html',message=True)
      else:
         try:
             courseqry = Courses.query\
                        .join(User_Course, Courses.id == User_Course.course_id)\
                        .with_entities(Courses.course_name,
                                       Courses.course_img_url,
                                       Courses.course_url)\
                        .filter_by(user_id=current_user.id).distinct().all()
             user_courseList =[]
             for usr_course in courseqry:
                 user_courseList.append(usr_course)
             return render_template("mycourses.html", user_courseList=user_courseList,name=current_user.user_fname )

         except Exception:
             return render_template('mycourses.html')
    return redirect(url_for('login'))




@app.route('/courses')
def courses():
    activecourses = Courses.query.with_entities(Courses.course_name,
                                          Courses.course_img_url,
                                          Courses.course_duration,
                                          Courses.course_fees,
                                          Courses.course_mode,
                                          Courses.course_details_url,
                                          Courses.course_description) \
        .filter_by(isActive=1).order_by(desc(Courses.date_created)).all()
    activeCourseList = []
    for course in activecourses:
        activeCourseList.append(course)

    othercourses = Courses.query.with_entities(Courses.course_name,
                                          Courses.course_img_url,
                                          Courses.course_duration,
                                          Courses.course_fees,
                                          Courses.course_mode,
                                          Courses.course_details_url,
                                          Courses.course_description) \
        .filter_by(isActive=0).order_by(desc(Courses.date_created)).all()
    otherCourseList = []
    for course in othercourses:
        otherCourseList.append(course)

    if current_user.is_authenticated:
      return render_template('courses.html',otherCourseList=otherCourseList,activeCourseList=activeCourseList)
    else:
      return render_template('courses.html',
             otherCourseList=otherCourseList,activeCourseList=activeCourseList)

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


################################## course details ###########################################

'''
@app.route('/courses/data-engineering-fundamentals')
def course_data_engineering():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=1,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/data-engineering-course.html',isEnrolled=isEnrolled)
    return render_template('courses/data-engineering-course.html')



@app.route('/courses/bigdata-hadoop')
def course_bigdata_hadoop():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=2,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/bigdata-hadoop-course.html',isEnrolled=isEnrolled)
    return render_template('courses/bigdata-hadoop-course.html')


@app.route('/courses/programming-fundamentals')
def programming_fundamentals():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=2,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/programming-fundamentals-course.html',isEnrolled=isEnrolled)
    return render_template('courses/programming-fundamentals-course.html')

'''


@app.route('/courses/data-analysis-in-python')
def data_analysis_in_python():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=9,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/data-analysis-in-python.html',isEnrolled=isEnrolled)
    return render_template('courses/data-analysis-in-python.html')



@app.route('/courses/data-visualization-in-python')
def data_visualization_in_python():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=8,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/data-visualization-in-python.html',isEnrolled=isEnrolled)
    return render_template('courses/data-visualization-in-python.html')


@app.route('/courses/python-basics-course')
def python_basics_course():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=10,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/python-basics-course.html',isEnrolled=isEnrolled)
    return render_template('courses/python-basics-course.html')


@app.route('/courses/data-structure-python-course')
def data_structure_python_course():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=18,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/data-structure-python-course.html',isEnrolled=isEnrolled)
    return render_template('courses/data-structure-python-course.html')



@app.route('/courses/flask-for-beginners')
def flask_for_beginners():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=13,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/flask-for-beginners-course.html',isEnrolled=isEnrolled)
    return render_template('courses/flask-for-beginners-course.html')



@app.route('/courses/basic-statistics')
def basic_statistics():
    if current_user.is_authenticated:
      course = User_Course.query.with_entities(User_Course.user_id).filter_by(course_id=15,user_id=current_user.id).count()
      if course > 0:
          isEnrolled = True
      else:
          isEnrolled = False
      return render_template('courses/statistics-course.html',isEnrolled=isEnrolled)
    return render_template('courses/statistics-course.html')


################################ student course view #######################################

'''
@login_required
@app.route('/data-engineering-tutorial')
def data_engineering_tutorial():
    if current_user.is_authenticated:
       return render_template('student-course/data-engineering-tutorial.html')
    return redirect(url_for('login'))


@login_required
@app.route('/bigdata-hadoop-tutorial')
def big_data_hadoop_tutorial():
    if current_user.is_authenticated:
       return render_template('student-course/bigdata-hadoop-tutorial.html',name=current_user.user_fname)
    return redirect(url_for('login'))


@login_required
@app.route('/programming-fundamentals-tutorial')
def programming_fundamentals_tutorial():
    if current_user.is_authenticated:
       return render_template('student-course/programming-fundamentals-tutorial.html',name=current_user.user_fname)
    return redirect(url_for('login'))

'''


@login_required
@app.route('/data-visualization-python-tutorial')
def data_visualization_python_tutorial():
    if current_user.is_authenticated:
        course_id = Course_Feedback.query. \
            with_entities(Course_Feedback.course_id). \
            filter_by(user_id=current_user.id, course_id=8).all()
        if (course_id):
            feedback_submitted = True
        else:
            feedback_submitted = False
        return render_template('student-course/data-visualization-python-tutorial.html',feedback_submitted=feedback_submitted)
    return redirect(url_for('login'))


@login_required
@app.route('/data-analysis-using-python-tutorial')
def data_analysis_using_python():
    if current_user.is_authenticated:
        course_id = Course_Feedback.query. \
            with_entities(Course_Feedback.course_id). \
            filter_by(user_id=current_user.id, course_id=9).all()
        if (course_id):
            feedback_submitted = True
        else:
            feedback_submitted = False
        return render_template('student-course/data-analysis-using-python-tutorial.html',feedback_submitted=feedback_submitted)
    return redirect(url_for('login'))


@login_required
@app.route('/python-basics-tutorial')
def python_basics_tutorial():
    if current_user.is_authenticated:
       course_id = Course_Feedback.query.\
                    with_entities(Course_Feedback.course_id).\
                    filter_by(user_id=current_user.id,course_id=10).all()
       if (course_id):
           feedback_submitted = True
       else:
           feedback_submitted = False
       return render_template('student-course/python-basics-tutorial.html',feedback_submitted=feedback_submitted)
    return redirect(url_for('login'))




@login_required
@app.route('/data-stucture-algorithm-tutorial')
def data_stucture_algorithm_tutorial():
    if current_user.is_authenticated:
       course_id = Course_Feedback.query.\
                    with_entities(Course_Feedback.course_id).\
                    filter_by(user_id=current_user.id,course_id=18).all()
       if (course_id):
           feedback_submitted = True
       else:
           feedback_submitted = False
       return render_template('student-course/data-structure-algorithm-tutorial.html',feedback_submitted=feedback_submitted)
    return redirect(url_for('login'))


@login_required
@app.route('/flask-for-beginners-tutorial')
def flask_for_beginners_tutorial():
    if current_user.is_authenticated:
       course_id = Course_Feedback.query.\
                    with_entities(Course_Feedback.course_id).\
                    filter_by(user_id=current_user.id,course_id=13).all()
       if (course_id):
           feedback_submitted = True
       else:
           feedback_submitted = False
       return render_template('student-course/flask-for-beginners-tutorial.html',feedback_submitted=feedback_submitted)
    return redirect(url_for('login'))


@login_required
@app.route('/statistics-tutorial')
def statistics_tutorial():
    if current_user.is_authenticated:
       course_id = Course_Feedback.query.\
                    with_entities(Course_Feedback.course_id).\
                    filter_by(user_id=current_user.id,course_id=15).all()
       if (course_id):
           feedback_submitted = True
       else:
           feedback_submitted = False
       return render_template('student-course/statistics-tutorial.html',feedback_submitted=feedback_submitted)
    return redirect(url_for('login'))








