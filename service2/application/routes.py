# Service 2 Routes by Sara edited by PP

from application import app
from flask import request, Response
from random import randint

@app.route('/selection/colour', methods=['GET'])
def get_colour():
    colour = ['red', 'white', 'green', 'orange', 'black']
 #  colour = colours[randint(0,4)]
    return Response(colour[randint(0,4)], mimetype='text/plain')
 #  return Response(colour, mimetype='text/plain')

# """ We don't need this - PP
""" @app.route('/post/colour', methods=['POST'])
def post_colour():
    return Response(request.data.decode("utf-8"), mimetype='text/plain')
 """

#  start testing - PP
colour = get_colour()
print(colour)
#  end testing - PP
