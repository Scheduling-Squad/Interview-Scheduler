db = db.getSiblingDB("interview_db");
db.employee_tb.drop();
db.candidate_tb.drop();
db.interview_tb.drop();

db.employee_tb.insertMany([
    {
        "id": 1,
        "name": "Selva"
    },
    {
        "id": 2,
        "name": "Ramu"
    },
    {
        "id": 3,
        "name": "Sai"
    },
]);

db.candidate_tb.insertMany([
    {
        "id": 1,
        "name": "Shankar"
    },
    {
        "id": 2,
        "name": "Thiru"
    },
    {
        "id": 3,
        "name": "Bala"
    },
]);

db.interview_tb.insertMany([
    {
        "id": 1,
        "Candidate": 1,
        "Employees": [1, 2],
        "date": date(12, 02, 2023),
        "interview_start_time": ISODate("2023-02-08T12:30"),
        "interview_start_time": ISODate("2023-02-08T13:30"),
        "status": False
    },
]);