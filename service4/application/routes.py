from application import app
from flask import request, Response, jsonify
import requests

@app.route('/selection/sentence', methods =  ['POST', 'GET'])
def sentence():
    sentences = [   'A secret admirer will soon send you a sign of affection',
                    'Your heart is in a place to draw true happiness',
                    'A thrilling time is in your near future',
                    'The one you love is closer than you think',
                    'Plan for many pleasures ahead',
                    'Something you lost will turn up soon',
                    'You are a winner',
                    'You will have a great day']

    response = requests.get('http://service1:5000/get/colour')
    fortune = response.json()
    colour = fortune["colour"]
    number = int(fortune["number"])-1

    result = ""

    if (colour == 'red' and number == 1):
        result = "You are a WINNER :)"
    elif (colour == 'black' and number == 8):
        result = "You are a LOSER :("
    else:
        result = sentences[number]
    

    dic = {}
    dic["colour"] = colour
    dic["number"] = number+1
    dic["result"] = result
    return jsonify(dic)
