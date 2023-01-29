from flask_sqlalchemy import SQLAlchemy
from application import app
# adding configuration for using a mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://selva:se1va888@localhost:3306/cctest'
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # emp_id = db.Column(db.Integer,primary_key = True)
    emp_username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self,name,hash):
        self.emp_username = name
        self.password_hash = hash
    def __repr__(self):
        return f'<Employee:{self.emp_username}>'
