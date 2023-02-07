from application import app
from flask import jsonify, request
from pymongo import MongoClient
from flask_cors import CORS

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
                '$lookup': {'from': 'employee', 'localField': 'employees', 'foreignField': '_id', 'as': 'employees'}
            },
            {
                "$lookup": {'from': 'candidate', 'localField': 'candidate', 'foreignField': '_id', 'as': 'candidate'}
            },
            {
                "$project": {
                    "_id": 0,
                    "interview_id": 1,
                    "employees": ["$employees.e_id", "$employees.e_name"],
                    "candidate": ["$candidate.c_id", "$candidate.c_name"],
                    "date": {"Year": {"$year": "$date"},
                             "Month": {"$month": "$date"},
                             "Day": {"$dayOfMonth": "$date"}
                             },
                    "interview_start_time": 1,
                    "interview_end_time": 1,
                    "status": 1
                }
            }
        ])
        interview_slots = []
        for c in result:
            interview_slots.append(dict(c))

        for interview in interview_slots:
            interview['employees'] = list(
                map(lambda x: {"id": x[0], "name": x[1]}, zip(interview['employees'][0], interview['employees'][1])))
            interview['candidate'] = {"id": interview['candidate'][0][0], "name": interview['candidate'][1][0]}

        return jsonify(interview_slots)

    # DELETE a interview slot
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
                'employee_id': str(id),
                'employee_name': name,
            }
            EmployeeJson.append(emp_dataDict)
        for data in candidate_data:
            id = data['c_id']
            name = data['c_name']
            can_dataDict = {
                'candidate_id': str(id),
                'candidate_name': name,
            }
            CandidateJson.append(can_dataDict)

        dataJson = {"candidate data" : CandidateJson,
                     "employee data" : EmployeeJson}

        print(dataJson)
        return jsonify(dataJson)

    # POST interview data to database
    if request.method == 'POST':
        body = request.json

        ID = body['interview_id']
        candidate = body['candidate']
        itm = db.candidate.find_one({"c_id": candidate})
        candidate_id = itm.get('_id')

        employees = body['employees']
        itm = [db.employee.find_one({"e_id": emp}) for emp in employees]
        employees_id = [item.get('_id') for item in itm]

        status = body['status']
        date = body['date']

        # db.users.insert_one({
        db['schedule'].insert_one({
            "interview_id": ID,
            "candidate": candidate_id,
            "employees": employees_id,
            "date": date,
            "status": status,
            "status": False
        })
        return jsonify({
            'status': 'Scheduled an interview for the candidate '+candidate_id,
            'interview_id': ID,
            'date': date,
            'candidate': candidate,
            'panel_members': employees
        })

@app.route('/interview/<string:id>', methods=['GET', 'PUT'])
def onedata(id):

    # GET a specific interview data by interview id
    if request.method == 'GET':

        result = collection.aggregate([
            {
                '$lookup': {'from': 'employee', 'localField': 'employees', 'foreignField': '_id', 'as': 'employees'}
            },
            {
                "$lookup": {'from': 'candidate', 'localField': 'candidate', 'foreignField': '_id', 'as': 'candidate'}
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
            },
            {
                "$match": {"interview_id": id}
            }
        ])

        interview = []
        for c in result:
            interview.append(dict(c))

        return jsonify(interview[0])

    # UPDATE a interview slot details by id
    if request.method == 'PUT':
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
        status = body['status']

        db['schedule'].update_one(
            {'interview_id': ID},
            {
                "$set": {
                    "date": date,
                    "interview_start_time": start_time,
                    "interview_end_time": end_time,
                    "Candidate": candidate_id,
                    "Employees": employees_id,
                    "status": status
                }
            }
        )

        return jsonify({'status': 'Interview id: ' + id + ' is updated!'})