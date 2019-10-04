import os
import secrets
import requests
import hashlib
import time
import dialogflow, json, pusher, requests, csv
from flask import request
from flask_login import login_user, current_user, logout_user, login_required, UserMixin
from flask import Flask, session, render_template, url_for, flash, redirect, request, send_from_directory, jsonify
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from app import app, db
from app.forms import UserForm, LoginForm, UpdateDetails
from app.models import User
from PIL import Image

### ESSENTIAL ROUTES ###

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

@app.route("/userRegister", methods = ['GET', 'POST'])
def userRegister():
	form = UserForm()
	if form.validate_on_submit():
		
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
	
		user = user(email=form.email.data, name=form.name.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		print("before pic")

		if form.photo.data:
			photo_file = save_photo(form.photo1.data)
			user.photo = photo_file
			photo = url_for('static', filename='user/' + user.photo1)

		db.session.add(user)
		db.session.commit()
		print(user)

		return redirect(url_for('login'))

	print('form not validated')
	print(form.errors)
	return render_template('user.html', title='user', form=form)

def save_photo(form_photo):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_photo.filename)
	photo_fn = random_hex + f_ext
	## Don't use static\user, pass them as separate arguments
	photo_path = os.path.join(app.root_path, 'static','user', photo_fn)
	print('PHOTO TO BE SAVED:: ', photo_path)
	output_size = (125, 125)
	i = Image.open(form_photo)
	i.thumbnail(output_size)
	#this will fail if static/user folder doesn't exist
	i.save(photo_path)
	return photo_fn


@app.route("/login", methods = ['GET','POST'])
def login():
	form = LoginForm(request.form)

	if form.validate_on_submit():
		user = user.query.filter_by(email=form.email.data).first()
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		now_hash = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())

		if (user and (user.password==now_hash)):
			login_user(user)
			print("hash correct")
			return redirect(url_for('account'))

		else:
			print('Nahin hua')
			flash('Login Unsuccessful. Please check email and password', 'danger')

	return render_template('login.html', title='Login', form=form)


@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
	updateForm = UpdateDetails()
	user = User.query.filter_by(id=current_user.id).first()
	print(user)
	if updateForm.validate_on_submit():

		user = user(email=updateForm.email.data, name=updateForm.name.data, password=updateForm.password.data)
		user.type = 'user'

		# IF ANY PHOTOS ARE UPDATED (Current)
		if updateForm.photo.data:
			photo_file = save_photo(updateForm.photo.data)
			user.photo = photo_file

		db.session.commit()
		print(user)
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))

	elif request.method == 'GET':
		updateForm.email.data = user.email
		updateForm.name.data = user.name
		updateForm.password.data = user.password
		print('Previous content loaded')
	# OLD PHOTO (registration ke waqt ka)
	photo = url_for('static', filename='user/' + user.photo)

	return render_template("account.html", title='Account', form=updateForm, user=user, photo=photo)


@app.route("/viewuser/<user_id>", methods = ['GET', 'POST'])
def user2_account(org_id):

	user = User.query.filter_by(id = org_id).first()
	return render_template('viewUserAccount.html', title='ViewUser', user=user)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))
	flash('You have been logged out', 'success')


### DIALOGFLOW WEBHOOK ### 

def retrieveFavourites():

	print('retrieving favourites')
	userStockPair = Favourites.query.filter_by(user_id = current_user.id).first() 
	print(userStockPair)
	return userStockPair

@app.route('showFav', methods=['POST'])
def showFavourites():

	userStockPair = retrieveFavourites()
	favourites = []
	for pair in userStockPair:
		stockDetails = Stocks.query.filter_by(stockID = pair.stock_name).first()
		favourites.append(stockDetails)
	
	favDict = dict((element[1], element[2:]) for element in favourites) 
	return favDict
	

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():

	data = request.get_json(silent=True, force=True)
	print('Data: '+json.dumps(data, indent=4))
	req = data

	if req['queryResult']['action'] == "showFavourites":
		print('showFavourites identified')
		response = showFavourites()
		r = jsonify(response)
		print ("\nRESPONSE\n")
		for i in response:
			print("", i, ":", response[i])
		r.headers['Content-Type'] = 'application/json'
		return r


	elif ['queryResult']['action']=='showGraph':
		print('showGraph identified')
		response = showGraph() # confirm redirection to site?
		r = jsonify(response)
		print ("\nRESPONSE\n")
		for i in response:
			print("", i, ":", response[i])
		r.headers['Content-Type'] = 'application/json'
		return r
