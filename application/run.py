from application import app
from application.temp import db, Employee


@app.route("/adduser", endpoint='chumma')
def chumma():
    sample = Employee("selva", "abc132")
    db.session.add(sample)
    db.session.commit()
    return "added sample"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
