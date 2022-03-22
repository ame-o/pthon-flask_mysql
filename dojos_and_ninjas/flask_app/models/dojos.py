#import database connection from MySQL to flask, using class methods

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        all_dojos = []
        for dict in results:
            all_dojos.append(cls(dict))
        return all_dojos

    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_one_dojo_with_ninjas(cls,data):
        query = """SELECT * FROM dojos 
        JOIN ninjas ON dojos.id= ninjas.dojo_id 
        WHERE dojos.id = %(dojo_id)s"""
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return results

    @classmethod
    def create_new_dojo(cls,data):
        #create new instances of user class linked to database
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        results= connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        return results
