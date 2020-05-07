# Service 2 Routes by Sara edited by PP

from application import app
from flask import request, Response
from random import randint

@app.route('/selection/colour', methods=['GET'])
def get_colour():
    colour = ['red', 'white', 'green', 'orange', 'black']
    return Response(colour[randint(0,4)], mimetype='text/plain')
