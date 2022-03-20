from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail
app = Flask(__name__)


app.config.from_pyfile('config.py')
app.config.from_pyfile('mail-config.py')

db = SQLAlchemy(app)
mail = Mail(app)

Bootstrap(app)


from views import *

if __name__ == '__main__':
    db.create_all()
    print("starting application....")
    app.run(host='0.0.0.0',port=8000,debug=True,threaded=True)
