from app import app
from flask import render_template


# Pág home
@app.route('/')
def home():
    return render_template('home.html')


# Pág end
@app.route('/end/')
def end():
    return render_template('end.html')