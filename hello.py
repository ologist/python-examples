from app import app,db
from flask import render_template

@app.route('/hello')
def hello():
    return render_template('hello.html', name=user.username)

if __name__ == "__main__":
    app.run()
