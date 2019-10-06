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
from project import app, db
from project.forms import UserForm, LoginForm, UpdateDetails,PublishForm
from project.models import User, Posts, Blacklist
from PIL import Image
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


### ESSENTIAL ROUTES ###

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

@app.route("/userRegister", methods = ['GET', 'POST'])
def userRegister():
	global ID_COUNT
	form = UserForm()
	if form.validate_on_submit():
		
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
		user = User(email=form.email.data, name=form.name.data, password = hashed_password)
		
		print(user.id)

		db.session.add(user)
		db.session.commit()
		print(user)
		print(user)

		return redirect(url_for('login'))
	else:
		print('form not validated')
		print(form.errors)
	return render_template('userRegister.html', title='Register', form=form)


@app.route("/login", methods = ['GET','POST'])
def login():
	form = LoginForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
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

		user = User(email=updateForm.email.data, name=updateForm.name.data, password=updateForm.password.data)
		user.type = 'user'

		db.session.commit()
		print(user)
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))

	elif request.method == 'GET':
		updateForm.email.data = user.email
		updateForm.name.data = user.name
		updateForm.password.data = user.password
		print('Previous content loaded')

	return render_template("account.html", title='Account', form=updateForm, user=user)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))
	flash('You have been logged out', 'success')



### METAMASK ###

@app.route("/payTrumped")
def payTrumped():
	return render_template('payTrumped.html', title='Security Deposit')

@app.route("/payAuth")
def payAuth():
	return render_template('payAuth.html', title='Encourage Authenticity')



### FUNCTIONALITIES ###

@app.route("/publish",methods = ['GET','POST'])
@login_required
def publish():
	user = User.query.filter_by(id=current_user.id).first()
	print(user)
	form = PublishForm()
	if form.validate_on_submit():
		post = Posts(title = form.title.data,author = form.author.data,text = form.text.data,user_id = user.id)
		print(post)

		##### ML CODE RUNS HERE
		docs_new= post.author+''+post.title+''+post.text
		docs_new = [docs_new]

		#LOAD MODEL
		loaded_vec = CountVectorizer(vocabulary=pickle.load(open("project/count_vector_fake.pkl", "rb")))
		loaded_tfidf = pickle.load(open("project/tfidf_fake.pkl","rb"))
		loaded_model = pickle.load(open("project/logreg_fake.pkl","rb"))

		X_new_counts = loaded_vec.transform(docs_new)
		X_new_tfidf = loaded_tfidf.transform(X_new_counts)
		predicted = loaded_model.predict(X_new_tfidf)

		print(predicted[0])

		## Uncomment this part
		if predicted[0] == 0:
			post.real = 1
			category_list = ["sport", "world", "us", "business", "health", "entertainment", "sci_tech"]

			

#LOAD MODEL
			loaded_vec = CountVectorizer(vocabulary=pickle.load(open("project/count_vector_type.pkl", "rb")))
			loaded_tfidf = pickle.load(open("project/tfidf_type.pkl","rb"))
			loaded_model = pickle.load(open("project/nb_model_type.pkl","rb"))

			X_new_counts = loaded_vec.transform(docs_new)
			X_new_tfidf = loaded_tfidf.transform(X_new_counts)
			predicted = loaded_model.predict(X_new_tfidf)

			print(category_list[predicted[0]])

			###### Type of post ML code runs here
			type_of_post = str(category_list[predicted[0]])
			post.type_of_post = type_of_post
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('account'))

		else:
			blacklisted_user = Blacklist(email = user.email,user_id = user.id)
			db.session.add(blacklisted_user)
			db.session.commit()
			return render_template("blacklist.html", title='Fake Alert!')

	else:
		print("Form not validated")

	return render_template("publish.html", title='Publish', form=form, user = user)


@app.route("/viewuser/<user_id>", methods = ['GET', 'POST'])
def user2_account(org_id):

	user = User.query.filter_by(id = org_id).first()
	return render_template('viewUserAccount.html', title='ViewUser', user=user)


@app.route("/view")
def view():
	return render_template("view.html",title = 'View Custom News')


@app.route("/viewList/<type>")
def viewList(type):
	newsList = Posts.query.filter_by(type_of_post=type).all()
	return render_template("viewList.html",title = 'View News', newsList = newsList)


@app.route("/viewNews/<id>")
def viewNews(id):
	newsArticle = Posts.query.filter_by(id=id).first()
	return render_template('viewNews.html', title='News', newsArticle=newsArticle)