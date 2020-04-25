from application import app
from Flask import request, Response

@app.route('/selection/sentence', methods =  ['POST', 'GET'])
def sentence():
    sentences = ['You are a winner!', 'Fortune 2','Fortune 3','Fortune 4','Fortune 5','Fortune 6','Fortune 7','Fortune 8']
    fortune = requests.get('http://service1:5000/selection/sentence', json={"colour": colour.text, "number": number.text})
    if colour == "green":
        if number == "1":