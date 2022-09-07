# user.py
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class User:
    DB = 'users'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def is_valid_user(cls,user):
        is_valid = True 

        if len(user['first_name']) <= 0:
            is_valid = False
            flash('Field is required')
        if len(user['last_name']) <= 0:
            is_valid = False
            flash('Field is required')
        if len(user['email']) <= 0:
            is_valid = False
            flash('Field is required')