from application import app
from application.temp import db, Employee
from flask import request, json, make_response


@app.route("/register", endpoint='register', methods=['POST'])
def register():
    if request.method == 'POST':
        req_data = json.loads(request.data)
        first_name = req_data['username']
        password = req_data['password']
        sample = Employee(first_name, password)
        db.session.add(sample)
        db.session.commit()
        response = make_response("<h1>Success</h1>",200)
        return response
    else:
        return "Please send POST requests"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
