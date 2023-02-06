from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
user_name = "HR"
pass_ = "Password123"

cluster = MongoClient(f"mongodb+srv://{user_name}:{pass_}@interview.nuuublq.mongodb.net/test")
db = cluster['interview']
collection = db['schedule']

CORS(app)


@app.route('/home', method=['GET', 'DELETE'])
def home_page():
    # GET Interview data from database
    if request.method == 'GET':
        result = collection.aggregate([
            {
                '$lookup': {'from': 'employee', 'localField': 'Employees', 'foreignField': '_id', 'as': 'Employees'}
            },
            {
                "$lookup": {'from': 'candidate', 'localField': 'Candidate', 'foreignField': '_id', 'as': 'Candidate'}
            },
            {
                "$project": {
                    "_id": 0,
                    "interview_id": 1,
                    "Employees": "$Employees.e_id",
                    "Candidate": "$Candidate.c_id",
                    "date": 1,
                    "interview_start_time": 1,
                    "interview_end_time": 1,
                    "status": 1
                }
            }
        ])
        interview_slots = []
        for c in result:
            interview_slots.append(dict(c))

        return jsonify(interview_slots)

    if request.method == 'DELETE':
        body = request.json
        id = body['interview_id']

        db.schedule.delete_one({'interview_id': id})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Interview ID: ' + id + ' is deleted!'})

@app.route('/NewInterview', method=['POST', 'GET'])
def schedule_interview():

    # GET employee and candidate data from database
    if request.method == 'GET':
        employee_data = db.employee.find()
        candidate_data = db.candidate.find()

        EmployeeJson = []
        CandidateJson = []

        for data in employee_data:
            id = data['e_id']
            name = data['e_name']
            emp_dataDict = {
                'EmployeeID': str(id),
                'EmployeeName': name,
            }
            EmployeeJson.append(emp_dataDict)
        for data in candidate_data:
            id = data['c_id']
            name = data['c_name']
            can_dataDict = {
                'CandidateID': str(id),
                'CandidateName': name,
            }
            CandidateJson.append(can_dataDict)

        dataJson = {"Candidate data" : CandidateJson,
                     "Employee data" : EmployeeJson}

        print(dataJson)
        return jsonify(dataJson)

    # POST interview data to database
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
    app.debug = True
    app.run()