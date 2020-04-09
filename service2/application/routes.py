from application import app
from flask import request, Response
from random import randint

@app.route('get/color', method=['GET'])
def get_color():
    animals = ['red', 'white', 'green', 'orange']
    animal = animals[randint(0,3)]
    return Response(animal, mimetypr='text/plain')

@app.route('post/color', method=['POST'])
def post_color():
    return Response(request.data.decode("utf-8"), mimetype='text/plain')

