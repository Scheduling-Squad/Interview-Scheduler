from application import app
from application.temp import db, Employee
from flask import request,json
from cryptography.fernet import Fernet


@app.route("/register", endpoint='chumma',methods=['GET','POST'])
def chumma():
    req_data = json.loads(request.data)
    first_name = req_data['username']
    password = req_data['password']
    # sample = Employee("selva", "abc132")
    # db.session.add(sample)
    # db.session.commit()
    return "First:{fname}".format(fname=first_name)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
