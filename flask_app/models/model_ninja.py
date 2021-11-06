##### Rename model_"name" to reflect project #####

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the friend table from our database
DATABASE = 'dojos_and_ninjas'
##### RENAME: class_name(cap first letter), DATABASE_SCHEMA ##### 
##### table_name, column_name, all_table_name, new_table_name_id #####

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

# C *************
# C *************
# C *************

    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)'
        new_ninjas_id = connectToMySQL(DATABASE).query_db(query, data)

        return new_ninjas_id

# R *************
# R *************
# R *************

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for ninjas in results:
            all_ninjas.append(cls(ninjas))
        return all_ninjas

    @classmethod
    def get_one(cls, **data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return results
        return cls(results[0])

# U *************
# U *************
# U *************

    @classmethod
    def update_one(cls, **data):
        query = 'UPDATE ninjas SET column_name = %(column_name)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)

# D *************
# D *************
# D *************

    @classmethod
    def delete_one(cls, **data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s'
        connectToMySQL(DATABASE).query_db(query, data)
        return id


# ************* VALIDATIONS *************

    @staticmethod
    def validate_ninjas(**data):
        is_valid = True
        
        ##### can make multiple 'if' statements #####
        if len(data['column_name']) < 3:
            is_valid = False
            flash ('column_name name must be greater than 3 characters')

        return is_valid
