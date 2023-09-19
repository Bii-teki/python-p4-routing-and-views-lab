#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/print/<parameter>')
def hello(parameter):
    print (parameter)
    return f'{parameter}'

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<string:param>")
def print_string(param):
    return f'{param}'

@app.route('/count/<int:param>')
def count(param):
    numbers = [str(i) + "\n" for i in range(param)]
    return ''.join(numbers)

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operation(num1,operation, num2 ):
    if operation == "+":
        result = num1 + num2
        
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Division by zero'}), 400
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            return jsonify({'error': 'Modulo by zero'}), 400
    else:
        result = num1 - num2

    
    return str(result)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
