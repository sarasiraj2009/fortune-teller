from application import app
from flask import request, Response
from random import randint
@app.route('/number', methods = ['GET'])
def number():
    numbers = random.randint(1,8)
    return Response(numbers[randint(0,7)], mimetype='text/plain')

