from app import app 
from database import db
from user import User 
from flask import render_template

@app.route('/hello')
def hello():
    user = User.query.get(1)
    return "Hello, World2!" + user.username

@app.route('/hello2')
def hello2():
    user = User.query.get(1)
    return render_template('hello.html', name=user.username)

if __name__ == "__main__":
    app.run()
