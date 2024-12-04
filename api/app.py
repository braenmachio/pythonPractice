import json
from flask import Flask, jsonify, request

app = Flask(__name__) # create a flask application

employees = [   { 'id': 1, 'name': 'Ashley'}, 
                { 'id': 2, 'name': 'Kate'},  
                { 'id': 3, 'name': 'Joe'}]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId