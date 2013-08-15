from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'mydb'}
app.config['SECRET_KEY'] = ''
app.debug = True

db = MongoEngine(app)

if __name__ == '__name__':
    app.run()
