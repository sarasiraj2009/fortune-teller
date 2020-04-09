from flask import render_template
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Fortune Teller - Home')

@app.route('/fortune', methods=['GET'])
def fortune():    
    return render_template('fortune.html', title='Fortune Results')


@app.route('/get/colour', methods = ['GET'])
def colour():
    colour = requests.get('http://service2:5002/get/colour')
    return render_template('fortune.html', title='Fortune', colour=colour.text)

