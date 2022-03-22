#import database connection from MySQL to flask, using class methods
from flask_app.config.mysqlconnection import connectToMySQL

# from flask_app import app
from flask_app.models import dojos

class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all_ninjas(cls):
        query="SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        all_ninjas = []
        for dict in results:
            all_ninjas.append(cls(dict))
        return all_ninjas

    @classmethod
    def get_all_ninjas_one_dojo(cls,data):
        query = """SELECT * FROM ninjas 
        JOIN dojos ON dojos.id= ninjas.dojo_id 
        WHERE ninjas.dojo_id = %(ninjas.dojo_id)s"""
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return results

    @classmethod
    def create_new_ninja(cls,data):
        #create new instances of user class linked to database
        query = "INSERT INTO ninjas (first_name, last_name, age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        return results