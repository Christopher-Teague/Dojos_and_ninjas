##### Rename controller_"name" to be in line with project #####

from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_dojo, model_ninja ##### Rename to match model file #####

# @app.route('/')
# def index_ninjas():
#     return render_template('dojos_main.html')

# C *************

@app.route('/ninja/new') 
def new_ninja():
    context = {
        'all_dojos' : model_dojo.Dojo.get_all()
    }
    return render_template('/ninja_new.html', **context)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    model_ninja.Ninja.create_ninja(request.form)
    id = request.form["dojo_id"]
    return redirect(f'/dojo/{id}')

# R *************

@app.route('/ninja/show_all')
def get_all_ninja():
    return 'show all ninja' 

@app.route('/ninja/<int:id>')
def get_one_ninja():
    return 'show all ninja'


# U *************

@app.route('/ninja/<int:id>/edit')
def edit_name_ninja():
    return render_template('/')

@app.route('/ninja/<int:id>/update', methods=['POST'])
def update_one_ninja():
    return redirect('/')

# D *************

@app.route('/ninja/<int:id>/delete')
def delete_one_ninja():
    return 'show all ninja'