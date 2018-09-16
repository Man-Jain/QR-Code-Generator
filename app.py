from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_qrcode import QRcode
SECRET_KEY = 'p9Bv<3Eid9%$i01'

app = Flask(__name__)

QRcode(app)
Bootstrap(app)

class NameForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	submit = SubmitField('Create QRCode')

@app.route('/',methods=['POST','GET'])
@app.route('/index',methods=['POST','GET'])
def index():
	form = NameForm(csrf_enabled=False)
	if form.validate_on_submit():
		name = form.name.data
		return render_template('index.html',name=name, form=form)
	return render_template('index.html',form=form)

if __name__=="__main__":
	app.run(debug=True)