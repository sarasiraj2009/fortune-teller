# Service 2 Routes by Sara

from application import app
from flask import request, Response
from random import randint

@app.route('/get/colour', methods=['GET'])
def get_colour():
    colours = ['red', 'white', 'green', 'orange', 'black']
    colour = colours[randint(0,4)]
    return colour
 #  return Response(colour, mimetype='text/plain')

@app.route('/post/colour', methods=['POST'])
def post_colour():
    return Response(request.data.decode("utf-8"), mimetype='text/plain')

colour = get_colour()
print(colour)
