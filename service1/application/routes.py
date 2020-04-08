from flask import render_template
from application import app

@app.route('/')
def home():
    return render_template('home.html', title='Fortune Teller - Home')
