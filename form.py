from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

#App Config

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d4456ew6e8r9dsa65'

class ReusableForm(Form):
	username = TextField('username :', validators=[validators.required()])
	password = TextField('password :', validators=[validators.required(), validators.Length(min=3, max=10)])
	
@app.route("/", methods=['GET', 'POST'])
def hello():
	form = ReusableForm(request.form)
	
	print(form.errors)
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		
		if form.validate():
			#Save the comment here.
			flash(" " + 'a.n' + " " + username + " " + 'sudah melakukan login')
			return render_template('profil.html')
		else:
			flash('Isilah semua bagian form. ')
		
	return render_template('form.html', form=form)
	
@app.route('/profil', methods=['GET', 'POST'])
def profil():
   return render_template('profil.html')
   
@app.route('/kampus', methods=['GET', 'POST'])
def kampus():
   return render_template('kampus.html')
   
@app.route('/')
def form():
   return hello
	
if __name__ == "__main__":
	app.run()