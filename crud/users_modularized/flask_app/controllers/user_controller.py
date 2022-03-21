from flask_app import app
from flask import render_template,redirect,request

#import models
from flask_app.models.users import User
#========================================================== 
# display all users <-- grab from database
# =========================================================
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def display_users():
    all_users= User.get_all()
    print(all_users)
    return render_template('index.html', all_users=all_users)
    
#========================================================== 
# display one user <-- grab from database
# =========================================================
@app.route('/one_user/<int:id>')
def display_one_user(id):
    query_data = {
        "id" : id
    }
    one_user = User.get_one_user(query_data)
    return render_template("one_user.html", one_user = one_user)


#========================================================== 
# create new user --> send to database
# =========================================================
@app.route('/user/new')
def form_for_user():
    return render_template("new_user.html")

@app.route('/process', methods = ['POST'])
def create_user():
    User.save_instance(request.form)
    print(request.form)
    return redirect('/users')



#========================================================== 
# edit existing user --> send to database
# =========================================================
@app.route('/edit_user/<int:id>')
def form_edit_user(id):
    query_data = {
        "id":id
    }
    one_user = User.get_one_user(query_data)
    return render_template("edit_user.html", one_user = one_user)

@app.route('/process_edit', methods = ['POST'])
def process_edit_user():
    data={
        "id":request.form["id"],
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    print(data)
    User.edit_instance(data)
    return redirect ("/users")


#========================================================== 
# DELETE existing user --> send to database
# =========================================================
@app.route('/delete_user/<int:id>')
def delete(id):
    query_data = {
        "id" :id
    }
    one_user = User.delete_instance(query_data)
    return redirect('/users')

