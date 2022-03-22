from mysqlconnection import connectToMySQL
#import database connection from MySQL to flask, using class methods

class User:
    def __init__(self,data):
        self.id = data ["id"]
        self.first_name = data ["first_name"]
        self.last_name = data ["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        all_users = []
        #iterate over the database "results"
        for dict in results:
            all_users.append( cls(dict) )
        return all_users

    @classmethod    
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def save_instance(cls,data):
        #create new instances of user class linked to database
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW(), NOW())"
        return connectToMySQL("users_schema").query_db(query,data)
    
    @classmethod
    def edit_instance(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("users_schema").query_db(query,data)

    @classmethod
    def delete_instance(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("users_schema").query_db(query,data)

        