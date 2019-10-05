from flask_login import UserMixin
from project import login_manager, db

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model,UserMixin):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(30),unique=True,nullable = False)
	name = db.Column(db.String(30), nullable = False)
	password = db.Column(db.String(128), unique = False, nullable = False)
	address = db.Column(db.String(500), unique= True, nullable = True)
	posts_relation = db.relationship("Posts", backref="user",lazy = 'dynamic')
	is_blacklisted = db.relationship("Blacklist", backref="user",lazy = 'dynamic')
	def __repr__(self):
		return f"User('{self.id}', {self.name}', '{self.email}')"

class Posts(db.Model):
	"""docstring for Posts"""
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(1000), nullable = False)
	text = db.Column(db.String(3000),unique=True,nullable = False)
	author = db.Column(db.String(128), unique = False, nullable = False)
	type_of_post = db.Column(db.String(500), unique= True, nullable = True)
	real = db.Column(db.Integer, nullable=True)
	#user_id = db.relationship("User_id", back_populates = "user")
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

	def __repr__(self):
		return f"User('{self.id}', {self.title}', '{self.author}', '{self.type_of_post}', '{self.real}', '{self.user_id}')"	

class Blacklist(db.Model):
	__tablename__ = 'blacklist'
	email = db.Column(db.String(30),primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
