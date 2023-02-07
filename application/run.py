import os
import sys

sys.path.append(os.path.abspath('.'))
from application import app
from application.mongo import get_client
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS

client = get_client()
#client.server_info()
#database_names = client.list_database_names()
db = client["interview_db"]
collection = db['interview_tb']

CORS(app)


@app.route('/NewInterview',endpoint='schedule_interview', methods=['POST', 'GET'])
def schedule_interview():
    # GET employee and candidate data from database
    if request.method == 'GET':
        employee_data = db.employee_tb.find()
        candidate_data = db.candidate_tb.find()

        EmployeeJson = []
        CandidateJson = []

        for data in employee_data:
            id_1 = data['e_id']
            name = data['e_name']
            emp_dataDict = {
                'EmployeeID': str(id_1),
                'EmployeeName': name,
                'flag':'emp'
            }
            EmployeeJson.append(emp_dataDict)
        for data in candidate_data:
            id_2 = data['c_id']
            name = data['c_name']
            can_dataDict = {
                'CandidateID': str(id_2),
                'CandidateName': name,
                'flag':'can'
            }
            CandidateJson.append(can_dataDict)

        dataJson = {"Candidate data": CandidateJson,
                    "Employee data": EmployeeJson}

        print(dataJson)
        return jsonify(dataJson)

    # POST a data to database
    if request.method == 'POST':
        body = request.json

        ID = body['InterviewID']
        candidate = body['Candidate']
        itm = db.candidate.find_one({"c_id": candidate})
        candidate_id = itm.get('_id')

        employees = body['Employees']
        itm = [db.employee.find_one({"e_id": emp}) for emp in employees]
        employees_id = [item.get('_id') for item in itm]

        start_time = body['StartTime']
        end_time = body['EndTime']
        date = body['Date']

        # db.users.insert_one({
        db['schedule'].insert_one({
            "interview_id": ID,
            "Candidate": candidate_id,
            "Employees": employees_id,
            "date": date,
            "interview_start_time": start_time,
            "interview_end_time": end_time
        })
        return jsonify({
            'status': 'Data is posted to MongoDB!',
            'InterviewID': ID,
            'Date': date,
            'Candidate': candidate,
            'PanelMembers': employees
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
