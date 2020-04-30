from application import app
from flask import request, Response, jsonify
import requests

@app.route('/selection/sentence', methods =  ['POST', 'GET'])
def sentence():
    sentences = ['You are a winner!', 'Fortune 2','Fortune 3','Fortune 4','Fortune 5','Fortune 6','Fortune 7','Fortune 8']
    response = requests.get('http://service1:5000/get/colour')
    fortune = response.json()
    colour = fortune["colour"]
    number = fortune["number"]

    result = ""

    if colour == "green":
        if number == "1":
            result = "You'll have a green1 day"
        elif number == "2":
            result = "You'll have green2 day"
    elif colour == "red":
        if number == "1":
            result = "You'll have a red1 day"
    else:
        result = "You are a LOSER!"

    dic = {}
    dic["colour"] = colour
    dic["number"] = number
    dic["result"] = result
    return jsonify(dic)
