##### Rename controller_"name" to reflect project #####

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_ninja
# model the class after the friend table from our database
# from flask_app import DATABASE_SCHEMA    #####
DATABASE = 'dojos_and_ninjas'
##### RENAME: class_name(cap first letter), DATABASE_SCHEMA ##### 
##### table_name, column_name, all_table_name, new_table_name_id #####

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []   ### added ###


    @classmethod
    def dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        dojo = cls(results[0])
        
        for row_from_db in results:
            print(row_from_db)
            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' : row_from_db['ninjas.created_at'],
                'updated_at' : row_from_db['ninjas.updated_at'],
                'dojo_id' : row_from_db['dojo_id']
            }

            dojo.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojo


# C *************
# C *************
# C *************

    @classmethod
    def create_dojo(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        new_dojos_id = connectToMySQL(DATABASE).query_db(query,data)

        return new_dojos_id

# R *************
# R *************
# R *************

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for dojos in results:
            all_dojos.append(cls(dojos))
        return all_dojos

    @classmethod
    def get_one(cls, **data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return results
        return cls(results[0])

# U *************
# U *************
# U *************

    @classmethod
    def update_one(cls, **data):
        query = 'UPDATE dojos SET column_name = %(coulmun_name)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)

# D *************
# D *************
# D *************

    @classmethod
    def delete_one(cls, **data):
        query = 'DELETE FROM dojos WHERE id = %(id)s'
        connectToMySQL(DATABASE).query_db(query, data)
        return id


# ************* VALIDATIONS *************

    @staticmethod
    def validate_dojos(**data):
        is_valid = True

        if len(data['column_name']) < 3:
            is_valid = False
            flash ('column_name name must be greater than 3 characters')

        return is_valid