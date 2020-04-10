# Service 3 routes by Nida

from application import app
from flask import request, Response
from random import randint
@app.route('/get/number', methods = ['GET'])
def number():
    numbers = random.randint(1,8)
    return Response(numbers, mimetype='text/plain')

