from database import db 

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255), unique=True)
    age = db.Column(db.Integer)

    def __init__(self,username,age):
        self.username = username
        self.age = age

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    user1 = User('ologist', 10)
    user2 = User('josh', 20)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    # user = User.query.filter_by(username='josh').first()
    user = User.query.get(1)
    print user.username
    print user.age 
    print User.query.all()
