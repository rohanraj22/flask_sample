from flask import Flask, jsonify, request

app=Flask(__name__)

employee_dict={'000':'Employee-0'}

# Get all employees
@app.route('/employee', methods=['GET'])
def getAllEmployees():
    try:
        return jsonify(employee_dict), 200
    except(Exception) as ex:
        print(ex)
        return 'Error while processing request', 500

# Get employee by ID
@app.route('/employee/<empId>', methods=['GET'])
def getEmployeeById(empId):
    try:
        if not empId in employee_dict.keys():
            return 'Employee not found', 404    
        return jsonify({empId:employee_dict[empId]}), 200
    except(Exception) as ex:
        print(ex)
        return 'Error while processing request', 500

# Create a new employee
@app.route('/employee', methods=['POST'])
def CreateEmployee():
    try:        
        id = request.json['id']
        name= request.json['name']
        if id in employee_dict.keys():
            return 'employee already exists', 400
        employee_dict[id]=name
        return jsonify({id:name}), 201
    except(Exception) as ex:
        print(ex)
        return 'Error while processing request', 500
    
#  Update and existing employee
@app.route('/employee/<empId>', methods=['PUT'])
def UpdateEmployee(empId):
    try:
        if not empId in employee_dict.keys():
            return 'Employee not found', 404
        employee_dict[empId]=request.json['name']
        return jsonify({empId:employee_dict[empId]}), 200
    except(Exception) as ex:
        print(ex)
        return 'Error while processing request', 500

# Delete an employee
@app.route('/employee/<empId>', methods=['DELETE'])
def DeleteEmployee(empId):
    try:
        if not empId in employee_dict.keys():
            return 'Employee not found', 404
        del employee_dict[empId]
        return 'Employee deleted', 204
    except(Exception) as ex:
        print(ex)
        return 'Error while processing request', 500
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000)