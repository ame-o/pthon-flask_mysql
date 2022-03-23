from flask import render_template, redirect, request,flash, session
from flask_app import app

from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app) #use wherever you need it in there

#IMPORTANT table 1 should be the table that has the info for the connection
# of one to many
@app.route('/')
def index():
    return render_template('index.html')
#base page/dashboard/etc

#========================================================== 
# Show All Table1s  / One Table1 with connected table2s
# =========================================================
@app.route('/register', methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data_query = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "password" : pw_hash
        
        }
    user_id = User.create_instance(data_query)
    session['user_id'] = user_id
    return redirect('/dashboard')

# @app.route('/login',method=['POST'])
# def login():
#     data = {
#         "email" : request.form["email"],
#         "password" : request.form["password"]
#     }
#     user = User.get_one_email(data)

#     if not user:
#         flash("Invalid Email","login")
#         return redirect('/')
#     if not bcrypt.check_password_hash(user.password,request.form['password']):
#         flash ("Invalid Password!", "login")
#         return redirect('/')
#     session['user_id'] = user.id
#     return redirect('dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data_query= {
        'id' : session['user_id']
    }
    user_id=User.get_one_id(data_query)
    return render_template("dashboard.html", user_id=user_id)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

