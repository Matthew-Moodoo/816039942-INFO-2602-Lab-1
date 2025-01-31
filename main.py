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
    return jsonify(data)# return student data in response

# route variables
@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student['id'] == id: # filter out the students without the specified id
            return jsonify(student)

app.run(host='0.0.0.0', port=8080, debug=True)
