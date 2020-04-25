from application import app
from flask import request, Response
import requests

@app.route('/selection/sentence', methods =  ['POST', 'GET'])
def sentence():
    sentences = ['You are a winner!', 'Fortune 2','Fortune 3','Fortune 4','Fortune 5','Fortune 6','Fortune 7','Fortune 8']
    fortune = requests.get('http://service1:5000/selection/sentence')
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
    #elif colour == "white":

    send_result = {"result": result}        
    return send_result

