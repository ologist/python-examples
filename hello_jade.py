from app import app 
from database import db
from user import User 
from flask import render_template

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/hello')
def hello():
    user = User.query.get(1)
    return render_template('hello.jade', name=user.username)

if __name__ == "__main__":
    app.run()
