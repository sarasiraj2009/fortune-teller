# Service 3 routes by Nida edited by PP

from application import app
from flask import request, Response
from random import randint

@app.route('/selection/number', methods = ['GET'])
def number():
    numbers = randint(1,8)
    number_string = str(numbers)
    return Response(number_string, mimetype='text/plain')

