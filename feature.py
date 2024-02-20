from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField

API = Flask(__name__)


@API.route('/htmlforms',methods = ['GET','POST'])
def htmlforms():
    if request.method == 'POST':
        fd = request.form
        return fd['un']
    return render_template('htmlforms.html')

class NameForm(Form):
    name = StringField()
    age = IntegerField()
    submit = SubmitField()

@API.route('/webForms',methods = ['GET','POST'])
def webForms():
    NFO = NameForm()
    if request.method == 'POST':
        NFDO = NameForm(request.form)
        if NFDO.validate():
            return NFDO.name.data,NFDO.age.data
    return render_template('webForms.html',NFO=NFO)

if __name__ == '__main__':
    API.run(debug=True)