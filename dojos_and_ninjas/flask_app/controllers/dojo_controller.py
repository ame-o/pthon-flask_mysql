from flask_app import app
from flask import render_template, redirect,request,session

from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
# from flask_app.models.ninjas import Ninjas

@app.route('/')
def index():
    return redirect('/dojos')

#========================================================== 
# Show All  / One Dojo
# =========================================================

@app.route('/dojos')
def show_dojos():
    all_dojos= Dojo.get_all_dojos()
    all_ninjas= Ninja.get_all_ninjas()
    return render_template("dojos.html", all_dojos=all_dojos, all_ninjas=all_ninjas)

@app.route('/dojos/<int:id>')
def show_one_dojo(dojo_id):
    dojo_id = {
        "id" : id
    }
    one_dojo_ninjas = Dojo.get_one_dojo_with_ninjas(dojo_id)
    return render_template("dojo_show_one.html", one_dojo_ninjas=one_dojo_ninjas)


#========================================================== 
# create new instance of Dojo --> send to database
# =========================================================

@app.route('/create_dojo', methods = ['POST'])
def create_dojo():
    Dojo.create_new_dojo(request.form)
    return redirect("/dojos")


