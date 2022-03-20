from app import db
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Index
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.dialects import mysql

Base = declarative_base()

import uuid

############ models




class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(500))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_fname = db.Column(db.String(500))
    user_lname = db.Column(db.String(500))
    user_email = db.Column(db.String(100),unique=True)
    user_phoneno = db.Column(db.String(100))
    user_password = db.Column(db.String(256))
    date_created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    user_status = db.Column(db.Boolean)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def has_role(self):
        role = User_Role.query.with_entities(User_Role.role_id)\
            .filter_by(user_id=self.id).first()
        role_id = role[0]
        return role_id



class User_Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,ForeignKey('user.id'))
    role_id = db.Column(db.Integer,ForeignKey('role.id'))



class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(500))
    course_category_id = db.Column(db.Integer,ForeignKey('course_category.id'))
    course_duration = db.Column(db.String(500))
    course_fees = db.Column(db.String(500))
    course_mode = db.Column(db.String(500))
    course_description = db.Column(db.String(500))
    course_details_url = db.Column(db.String(500))
    course_url = db.Column(db.String(500))
    course_img_url = db.Column(db.String(500))
    isActive = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime)
    #child = relationship("User_Course")


class Course_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_category_name = db.Column(db.String(500))



class User_Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.Integer,ForeignKey('user.id'))
    course_id =db.Column(db.Integer,ForeignKey('courses.id'))
    date_created = db.Column(db.DateTime)



class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(300))
    blog_category_id = db.Column(db.Integer,ForeignKey('blog_category.id'))
    blog_description = db.Column(db.String(5000))
    blog_content = db.Column(db.String(10000))
    blog_url = db.Column(db.String(500))
    blog_author = db.Column(db.String(50))
    date_created = db.Column(db.Date)



class Blog_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_category_name = db.Column(db.String(500))


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100))
    date_created = db.Column(db.DateTime)



class Course_Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,ForeignKey('user.id'))
    course_id = db.Column(db.Integer,ForeignKey('courses.id'))
    content_rating = db.Column(db.Integer)
    instructor_rating = db.Column(db.Integer)
    overall_rating = db.Column(db.Integer)
    comments = db.Column(db.String(500))
    date_created = db.Column(db.DateTime)




class Contactus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    message = db.Column(mysql.LONGTEXT())
    date_created = db.Column(db.DateTime)



class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    category = db.Column(db.String(100))
    linkedinurl = db.Column(db.String(100))
    date_created = db.Column(db.DateTime)



class freelance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    category = db.Column(db.String(100))
    linkedinurl = db.Column(db.String(100))
    hours = db.Column(db.String(100))
    date_created = db.Column(db.DateTime)


def generate_student_uid():
    return "STU-"+str(uuid.uuid1())


class Student(db.Model):
    pk_student_id = db.Column(db.String(100), primary_key=True, default=generate_student_uid)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    profile_image_path = db.Column(db.String(500))
    address = db.Column(db.String(300))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    institution_name = db.Column(db.String(100))
    qualification = db.Column(db.String(100))
    department = db.Column(db.String(100))
    year_of_passing = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    industry_type = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    experience = db.Column(db.Integer)
    skills = db.Column(db.String(1000))
    linkedin_url = db.Column(db.String(100))
    resume_path = db.Column(db.String(500))
    last_updated = db.Column(db.DateTime)



def generate_employer_uid():
    return "EMP-"+str(uuid.uuid1())

class Employer(db.Model):
    pk_employer_id = db.Column(db.String(100), primary_key=True,default=generate_employer_uid)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    linkedin_url = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    company_url = db.Column(db.String(100))
    industry_type = db.Column(db.String(100))
    head_count = db.Column(db.String(100))
    established_year = db.Column(db.String(100))
    company_info = db.Column(db.String(1000))
    company_address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    logo_path = db.Column(db.String(500))
    verified = db.Column(db.Boolean)
    last_updated = db.Column(db.DateTime)



class Internship(db.Model):
    pk_internship_id = db.Column(db.String(100), primary_key=True)
    fk_employer_id = db.Column(db.String(100), db.ForeignKey('employer.pk_employer_id'))
    title = db.Column(db.String(100)) #
    description = db.Column(db.String(2000))
    skills = db.Column(db.String(500)) #
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    stream = db.Column(db.String(100)) #
    qualification = db.Column(db.String(100)) #
    compensation = db.Column(db.String(100)) #
    position = db.Column(db.String(100)) #
    address = db.Column(db.String(100)) #
    experience = db.Column(db.String(100))
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    contact_no = db.Column(db.String(20))
    last_application_date = db.Column(db.DateTime)
    publish_date = db.Column(db.DateTime)
    paid_type = db.Column(db.String(100))
    internship_type = db.Column(db.String(100))

    employer = db.relationship('Employer', backref=db.backref('internship', lazy='dynamic'))



class   InternApplication(db.Model):
    pk_application_id = db.Column(db.String(100),primary_key=True)
    fk_internship_id = db.Column(db.String(100), db.ForeignKey('internship.pk_internship_id'),nullable=False)
    fk_student_id = db.Column(db.String(100), db.ForeignKey('student.pk_student_id'),nullable=False)
    status=db.Column(db.String(20))
    application_date = db.Column(db.DateTime)

    __table_args__ = (
        Index('only_one_active_', fk_internship_id, fk_student_id,
              unique=True),
    )

    student = db.relationship('Student', backref=db.backref('intern_application', lazy='dynamic'))
    internship = db.relationship('Internship', backref=db.backref('intern_application', lazy='dynamic'))



