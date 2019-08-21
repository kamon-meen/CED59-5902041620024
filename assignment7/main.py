from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class meenRegister(FlaskForm):
    Fastname = StringField("FirstName", validators=[InputRequired()])
    Lastname = StringField("Lastname", validators=[InputRequired()])
    Email = StringField("Email",  validators=[InputRequired("Please enter your email."), Email("Please enter your email again.")])
    Username = StringField("Username", validators=[InputRequired()])
    Password = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Please enter password 8 character.")])

@app.route('/')
def regis():
    form = meenRegister()
    return render_template('Register.html', form=form)


@app.route('/MeenRegister', methods=["GET", "POST"])
def MeenRegister():
    form = meenRegister()
    if form.validate_on_submit():
        return "Sumbit now"
    return render_template('Register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)