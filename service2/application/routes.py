from application import app
from flask import request, Response
from random import randint

@app.route('/get/colour', methods=['GET'])
def get_colour():
    colours = ['red', 'white', 'green', 'orange', 'black']
    colour = colours[randint(0,3)]
    return Response(colour, mimetype='text/plain')

@app.route('/post/color', methods=['POST'])
def post_color():
    return Response(request.data.decode("utf-8"), mimetype='text/plain')

