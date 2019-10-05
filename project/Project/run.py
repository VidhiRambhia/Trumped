from flask import Flask,render_template,url_for
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'apple'
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

@app.route("/")
@app.route("/home")
def home():
	form = RegistrationForm()
	return render_template('index.html',form = form)


if __name__ == '__main__':
	app.run(debug=True)