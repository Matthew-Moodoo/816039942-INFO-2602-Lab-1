#816039942 INFO 2602 LAB 1

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref') # get the parameter from url
    if pref:
        for student in data: # iterate dataset
            if student['pref'] == pref: # select only the students with a given meal preference
                result.append(student) # add match student to the result
        return jsonify(result) # return filtered set if parameter is supplied
    return jsonify(data) # return entire dataset if no parameter supplied

#Exercise 1
#----------------------------

@app.route('/stats')
def get_counts():
    chickencount = 0;
    fishcount = 0;
    vegcount = 0;
    compscimajors = 0;
    compscispecs = 0;
    itmajors = 0;
    itspecs = 0;

    for student in data:
        if student['pref'] == 'Chicken':
            chickencount += 1
        if student['pref'] == 'Fish':
            fishcount += 1
        if student['pref'] == 'Vegetable':
            vegcount += 1
        if student['programme'] == 'Computer Science (Major)':
            compscimajors += 1
        if student['programme'] == 'Computer Science (Special)':
            compscispecs += 1
        if student['programme'] == 'Information Technology (Major)':
            itmajors += 1
        if student['programme'] == 'Information Technology (Special)':
            itspecs += 1
    message = f'Chicken: {chickencount}  Fish: {fishcount}  Vegetable: {vegcount}  Computer Science (Major): {compscimajors}  Computer Science (Special): {compscispecs}  Information Technology (Major): {itmajors}  Information Technology (Special): {itmajors}'
    return jsonify(message)

#Exercise 2
#-----------------------------------

@app.route('/add/<int:a>/<int:b>')
def add_nums(a, b):
    sum = a + b
    message = f'The sum of {a} and {b} is {sum}.'
    return jsonify(message)

@app.route('/subtract/<int:a>/<int:b>')
def subtract_nums(a, b):
    diff = a - b
    message = f'The difference of {a} and {b} is {diff}.'
    return jsonify(message)

@app.route('/multiply/<int:a>/<int:b>')
def multiply_nums(a, b):
    product = a * b
    message = f'The product of {a} and {b} is {product}.'
    return jsonify(message)

@app.route('/divide/<int:a>/<int:b>')
def divide_nums(a, b):
    quotient = a / b
    message = f'The quotient of {a} and {b} is {quotient}.'
    return jsonify(message)
    

app.run(host='0.0.0.0', port=8080, debug=True)
