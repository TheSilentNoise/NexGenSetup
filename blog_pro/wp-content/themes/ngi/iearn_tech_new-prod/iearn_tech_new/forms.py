from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,IntegerField,widgets,\
    TextAreaField,SelectField,validators,RadioField
from wtforms.validators import InputRequired,Length,Email,EqualTo,NumberRange
from wtforms.widgets import TextArea
from wtforms.fields.html5 import URLField,DateField
from models import  *
from utils import *
from flask_login import current_user

########### forms

class Loginform(FlaskForm):
    email = StringField('Username',validators=[InputRequired(), Email(message="Invalid Email")])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember me')


class Registrationform(FlaskForm):
    user_role = SelectField('Please select user type', choices=user_role_list, validators=[InputRequired()])
    user_fname = StringField('', validators=[InputRequired()])
    user_lname = StringField('', validators=[InputRequired()])
    user_email = StringField('',validators=[InputRequired(), Email(message="Invalid Email ")])
    user_phoneno = IntegerField('' ,widget = widgets.Input(input_type="number"),validators=[InputRequired()])
    user_password = PasswordField('',[InputRequired(), Length(min=8),
               EqualTo('confirm', message='Passwords & Confirm Password must match!')])
    confirm=PasswordField('')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Enter your registered Email Address',
                        validators=[InputRequired(), Email(message="Invalid Email")])



class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('', [InputRequired()])
    new_password = PasswordField('',[InputRequired(), Length(min=8),
               EqualTo('confirm_password', message='Passwords & Confirm Password must match!')])
    confirm_password = PasswordField('')


class ResetPasswordForm(FlaskForm):
    user_password = PasswordField('Password', [InputRequired(), Length(min=8),
                    EqualTo('confirm', message='Passwords & Confirm Password must match!')])
    confirm = PasswordField('Confirm Password')


class ContactUsForm(FlaskForm):
    name = StringField('', validators=[InputRequired()])
    email = StringField('',validators=[InputRequired(), Email(message="Invalid Email")])
    subject = StringField('', validators=[InputRequired()])
    message = TextAreaField('', widget=TextArea(),validators=[InputRequired()])



category = [('', '--Select Category--'),
            ('DE', 'Data Engineering'),
            ('WD', 'Web Development'),
            ('DA','Data Analytics')]



class InternshipForm(FlaskForm):
    name = StringField('', validators=[InputRequired()])
    email = StringField('', validators=[InputRequired(), Email(message="Invalid Email")])
    phone = IntegerField('', widget=widgets.Input(input_type="number"))
    category = SelectField('', choices=category, validators=[InputRequired()])



class JobForm(FlaskForm):
    name = StringField('', validators=[InputRequired()])
    email = StringField('', validators=[InputRequired(), Email(message="Invalid Email")])
    phone = IntegerField('', widget=widgets.Input(input_type="number"))
    category = SelectField('', choices=category, validators=[InputRequired()])
    linkedinurl = StringField('',validators=[InputRequired()])


class FreelanceForm(FlaskForm):
    name = StringField('', validators=[InputRequired()])
    email = StringField('', validators=[InputRequired(), Email(message="Invalid Email")])
    phone = IntegerField('', widget=widgets.Input(input_type="number"))
    category = SelectField('', choices=category, validators=[InputRequired()])
    linkedinurl = StringField('',validators=[InputRequired()])
    hours = IntegerField('', widget=widgets.Input(input_type="number"))



class EmployerDetailsForm(FlaskForm):
    user_fname = StringField('', validators=[InputRequired()])
    user_lname = StringField('', validators=[InputRequired()])
    user_phoneno = IntegerField('', widget=widgets.Input(input_type="number"),validators=[InputRequired()])
    linkedin_url = URLField('')
    company_name = StringField('',validators=[InputRequired()])
    company_url = StringField('',validators=[InputRequired()])
    industry_type = StringField('')
    head_count = IntegerField('',widget=widgets.Input(input_type="number"),validators=[InputRequired()])
    established_year = IntegerField('',widget=widgets.Input(input_type="number"),validators=[InputRequired()])
    company_info = TextAreaField('')
    company_address = TextAreaField('')
    city = StringField('',validators=[InputRequired()])
    state = StringField('',validators=[InputRequired()])
    country = StringField('',validators=[InputRequired()])



internshipType = [('', '--- Select Internship Type ---'),
            ('Office Internship', 'Office Internship'),
            ('Online Internship', 'Online Internship')]


class InternshipPostForm(FlaskForm):
    title = StringField('', validators=[InputRequired()])
    paidType = RadioField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')],
                        validators=[validators.Optional()], default='unpaid')
    internshipType = SelectField('', choices=internshipType, validators=[InputRequired()])
    compensation = StringField('')
    experience = StringField('',validators=[InputRequired()])
    designation = StringField('')
    description = TextAreaField('', validators=[InputRequired()])
    skills = StringField('',validators=[InputRequired()])
    qualification = StringField('',validators=[InputRequired()])
    stream = StringField('')
    startDate = DateField('', validators=[InputRequired()])
    endDate = DateField('',validators=[InputRequired()])
    lastApplicationDate = DateField('',validators=[InputRequired()])
    contactEmail = StringField('',validators=[InputRequired(), Email(message="Invalid Email ")])
    contactPhone = StringField('',validators=[InputRequired()])
    address = TextAreaField('')
    city = StringField('',validators=[InputRequired()])
    state = StringField('',validators=[InputRequired()])
    country = StringField('',validators=[InputRequired()])



class StudentDetailsForm(FlaskForm):
    user_fname = StringField('', validators=[InputRequired()])
    user_lname = StringField('', validators=[InputRequired()])
    user_phoneno = IntegerField('', widget=widgets.Input(input_type="number"),validators=[InputRequired()])
    date_of_birth = DateField('',validators=[validators.Optional()])
    linkedin_url = URLField('',validators=[validators.Optional()])
    gender = RadioField(choices=[('male','Male'),('female','Female')],
                       validators=[validators.Optional()],default='female')
    address = StringField('')
    city = StringField('')
    state = StringField('')
    country = StringField('')
    company_name = StringField('')
    industry_type = StringField('')
    designation = StringField('')
    experience = IntegerField('', widget=widgets.Input(input_type="number"),validators=[validators.Optional()])
    skills = TextAreaField('')
    year_of_passing = IntegerField('', widget=widgets.Input(input_type="number"),validators=[validators.Optional()])
    institution_name = StringField('')
    qualification = StringField('')
    department = StringField('')

    






