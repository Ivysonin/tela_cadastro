from app import app
from flask import render_template, redirect, url_for
from app.forms import UsersForm
from flask_login import login_user, login_required


# Pág cadastrar
@app.route('/', methods=['GET','POST'])
def cadastrar():
    form = UsersForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
    return render_template('cadastrar.html', form=form)