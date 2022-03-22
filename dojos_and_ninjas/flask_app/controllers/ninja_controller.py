from flask_app import app
from flask import render_template, redirect,request,session

# from flask_app.models.dojos import Dojo
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

#========================================================== 
# create Ninja
# =========================================================
@app.route('/ninjas')
def new_ninja_form():
    all_dojos= Dojo.get_all_dojos()
    return render_template("ninjas.html", all_dojos=all_dojos)


@app.route('/create_ninjas', methods=['POST'])
def create_ninja():
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : int(request.form["age"]),
        "dojo_id" : int(request.form["dojo.id"]),
    }
    new_ninja= Ninja.create_new_ninja(query_data)
    return redirect("/")