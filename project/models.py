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

	def __repr__(self):
		return f"User('{self.name}', '{self.email}')"