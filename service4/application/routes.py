from application import app
from Flask import request, Response

@app.route('/selection/sentence', methods =  ['POST'])
def sentence():
    sentences = ['You are a winner!', 'Fortune 2','Fortune 3','Fortune 4','Fortune 5','Fortune 6','Fortune 7','Fortune 8']