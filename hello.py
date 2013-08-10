from infra.database import app,db 
from domain.user import User 

@app.route("/hello")
def hello():
    user = User.query.get(1)
    return "Hello World2!" + user.username

if __name__ == "__main__":
    app.run()
