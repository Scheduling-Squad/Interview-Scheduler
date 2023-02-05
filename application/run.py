import sys
import os

sys.path.append(os.path.abspath('.'))
from application import app
from application.mongo import get_db
from flask import request, json, make_response

db = get_db()


@app.route("/addinterview", endpoint='addinterview', methods=['POST'])
def addinterview():
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')
