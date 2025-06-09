from app import app
from flask import render_template, redirect, url_for
from app.forms import UsersForm


# Pág home
@app.route('/')
def home():
    return render_template('home.html')


# Pág cadastrar
@app.route('/cadastrar/', methods=['GET','POST'])
def cadastrar():
    form = UsersForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('end'))
    return render_template('cadastrar.html', form=form)


# Pág end
@app.route('/end/')
def end():
    return render_template('end.html')