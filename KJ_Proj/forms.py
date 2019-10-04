from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, IntegerField, RadioField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, HiddenField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required, NumberRange, ValidationError
from trinity.models import User, Organizer

class UserForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired(), Length(max = 30)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Done')

	def validateEmail(self, Email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email taken, enter a different one')

class OrgForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired(), Length(max=30)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	kind = SelectField('Type', choices = [('0','Parties'), ('1', 'Wedding'), ('2', 'Corporate')], validators = [Required()])
	dateOrg = StringField('Date', validators=[DataRequired()])
	venueOrg = SelectField('Venue', choices = [('0', 'Hall'),('1', 'Lawn'), ('2', 'Resort'), ('3', 'Custom Venue')], validators = [DataRequired()])
	about = TextAreaField('About your organization', validators = [DataRequired()])
	photo1 = FileField('Add picture of your services here',validators=[FileAllowed(['jpg', 'png'])])
	photo2 = FileField('It gives the user a better preview',validators=[FileAllowed(['jpg', 'png'])])
	photo3 = FileField('You may add pictures later too',validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Make Me Discoverable')

	def validateEmail(self, Email):
		org = Organizer.query.filter_by(email=email.data).first()
		if org:
			raise ValidationError('Email taken, enter a different one')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')

class UpdateDetails(FlaskForm):
	name = StringField('Name', validators = [Length(max=30)])
	email = StringField('Email', validators = [Email()])
	password = PasswordField('New Password')
	kind = SelectField('Type', choices = [('0','Parties'), ('1', 'Wedding'), ('2', 'Corporate')], validators = [Required()])
	dateOrg = StringField('Date')
	venueOrg = SelectField('Venue', choices = [('0', 'Hall'),('1', 'Lawn'), ('2', 'Resort'), ('3', 'Custom Venue')])
	about = TextAreaField('About your organization')
	photo1 = FileField('Photo 1',validators=[FileAllowed(['jpg', 'png'])])
	photo2 = FileField('Photo 2',validators=[FileAllowed(['jpg', 'png'])])
	photo3 = FileField('Photo 3',validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update details')

	def validateEmail(self, Email):
		org = Organizer.query.filter_by(email=email.data).first()
		if org:
			raise ValidationError('Email taken, enter a different one')

class FilterForm(FlaskForm):
	dateUser = StringField('Date', validators=[DataRequired()])
	venueUser = SelectField('Venue', choices = [('0', 'Hall'),('1', 'Lawn'), ('2', 'Resort'), ('3', 'Custom Venue')], validators = [DataRequired()])
	submit = SubmitField('Show me')
