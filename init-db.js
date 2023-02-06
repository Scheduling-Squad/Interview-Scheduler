db = db.getSiblingDB("interview_db");
db.employee_tb.drop();
db.candidate_tb.drop();
db.interview_tb.drop();

db.employee_tb.insertMany([
    {
        "e_id": 1,
        "e_name": "Selva"
    },
    {
        "e_id": 2,
        "e_name": "Ramu"
    },
    {
        "e_id": 3,
        "e_name": "Sai"
    },
]);

db.candidate_tb.insertMany([
    {
        "c_id": 1,
        "c_name": "Shankar"
    },
    {
        "c_id": 2,
        "c_name": "Thiru"
    },
    {
        "c_id": 3,
        "c_name": "Bala"
    },
]);

db.interview_tb.insertMany([
    {
        "id": 1,
        "Candidate": 1,
        "Employees": [1, 2],
        "date": Date("2023-02-14"),
        "interview_start_time": ISODate("2023-02-08T12:30"),
        "interview_start_time": ISODate("2023-02-08T13:30"),
        "status": false
    },
]);