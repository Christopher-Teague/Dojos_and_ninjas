
##### Rename controller_"name" to be in line with project #####

from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_ninja ##### Rename to match model file #####
from flask_app.models.model_dojo import Dojo

@app.route('/')
def index_dojos():
    all_dojos = Dojo.get_all()
    return render_template('dojos_main.html', all_dojos = all_dojos)

# C *************

@app.route('/dojo/new') 
def new_dojo():
    return render_template('/')

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

# R *************

@app.route('/dojo/show_all')
def get_all_dojo():
    return render_template('/dojos_show.html')

# @app.route('/dojo/<int:id>')
# def dojos_with_ninjas(id):
#     print(id)
    
#     return render_template ('/dojos_show.html')



@app.route('/dojo/<int:id>')
def get_one_dojo(id):
    # print(id)
    data = Dojo.dojos_with_ninjas({'id': id})
    
    return render_template ('/dojos_show.html', dojo = data)


# U *************

@app.route('/dojo/<int:id>/edit')
def edit_name():
    return render_template('/')

@app.route('/dojo/<int:id>/update', methods=['POST'])
def update_one_dojo():
    return redirect('/')

# D *************

@app.route('/dojo/<int:id>/delete')
def delete_one_dojo():
    return 'delete one dojo'