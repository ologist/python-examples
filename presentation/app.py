from flask import Flask
from flask.ext.sqlalchemy import SQLAchemy
from infra import db
from user import User

@app.route('/')
def home():
    
