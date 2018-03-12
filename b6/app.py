#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import make_response
 
import os

app = Flask(__name__)
n = 0

@app.route('/')
def main():
    global n
    n += 1
    if n % 5 == 0:
        print('visitor', n, 'visited', flush=True)
    return 'congratulations, you are visitor #{}'.format(n) + '<tr><iframe src="https://i.fluffy.cc/q0S1XdWxrHN58Kwhj4pB91d9tmKrTqLR.gif" width="1900" height="800" frameBorder="0"></iframe>'

@app.route('/crash', methods=['GET', 'POST'])
def crash():
    if request.method == 'GET': 
        return 'You can either make a POST request to this endpoint with the json payload {"crash":"true"} (if you are cool) or you can use a command from lecture to manually kill the process'
    elif request.method == 'POST': 
        resp = request.get_json()
        if resp and 'crash' in resp:
            os.kill(os.getpid(), 9)
        return "You're on the right track! HINT: Pass content-type: application/json in the headers."
