from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+0[a-zA-Z]+$')

from flask import flash
#model page creates class for Table 1
class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# =========================================================
    #Validations
# =========================================================
    
    @staticmethod
    def validate_register(user): #checking if email is registered
        is_valid = True
        query = "SELECT * FROM users WHERE email =%(email)s;"
        results = connectToMySQL("login_and_reg").query_db(query,user)
        if len(results) >= 1:
            flash("Email is already taken","register")
            is_valis = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!","register")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid=False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid=False
        if len(user['password']) != user['confirm']:
            flash("Passwords don't match","register")
            is_valid=False
        
        return is_valid

# =========================================================
    #Query Methods
# =========================================================
    
# =========================================================
    #get all instances in table1 <- from database
# =========================================================
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("login_and_reg").query_db(query)
        all_users = []
        for dict in results:
            all_users.append(cls(dict))
        return all_users
# =========================================================
    #create a new instance in table1 -> send to database
# =========================================================
    @classmethod
    def create_instance(cls,data):
        #create new instances of user class linked to database
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s)"
        return connectToMySQL("login_and_reg").query_db(query,data)
        
# =========================================================
    #get only 1 instance in table1 <- from database
# =========================================================
    @classmethod    
    def get_one_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_and_reg").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod    
    def get_one_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("login_and_reg").query_db(query, data)
        return cls(results[0])

