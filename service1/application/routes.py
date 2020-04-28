from flask import render_template, jsonify
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Fortune Teller - Home')



@app.route('/get/colour', methods = ['GET', 'POST'])
def colour():
    colour = requests.get('http://service2:5002/selection/colour')
    number = requests.get('http://service3:5003/selection/number')
    return jsonify({"colour": colour, "number": number})
    
@app.route('/get/fortune', methods = ['GET', 'POST'])
def fortune():
    sentence = requests.get('http://service4:5004/selection/sentence')
    sentence = sentence.json()
    colour = sentence["colour"]
    number = sentence["number"]
    result = sentence["result"]
    return render_template('fortune.html', title='Fortunes', colour=colour, number=number, result=result)