#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_text(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ""
    for i in range(parameter):
        numbers += f"{i}\n"
    return numbers 

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
        return str(result)
    elif operation == '-':
        result = num1 -num2
        return str(result)
    elif operation == '*':
        result = num1 * num2
        return str(result)
    elif operation == 'div':
        result =  num1/num2
        return str(result)
    elif operation == '%':
        return str(num1 % num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)




