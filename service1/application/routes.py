from flask import render_template
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Fortune Teller - Home')



@app.route('/get/colour', methods = ['GET', 'POST'])
def colour():
    colour = requests.get('http://service2:5002/selection/colour')
    number = requests.get('http://service3:5003/selection/number')
    sentence = fortune.json('http://service4:5004/selection/sentence', json={"colour": colour.text, "number": number.text})
    return render_template('fortune.html', title='Fortunes', colour=colour.text, number=number.text, sentence=sentence)

