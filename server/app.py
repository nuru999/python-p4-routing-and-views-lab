#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:word>')
def print_string(word):
    print(word)
    return word

@app.route('/count/<int:num>')
def count(num):
    result = ''
    for x in range(num):
        result += str(x) + '\n'
    return result
    
@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid operation'

    return result
if __name__ == '__main__':
    app.run(port=5555, debug=True)