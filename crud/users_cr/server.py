from flask import Flask, render_template, request, redirect
# importing the user class from the user py
from users import User

app = Flask(__name__)



@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def display_user():
    all_users= User.get_all()
    print(all_users)
    return render_template('index.html', all_users=all_users)

@app.route('/user/new')
def form_for_user():
    return render_template("new_user.html")

@app.route("/process", methods = ['POST'])
def create_user():
    User.save_instance(request.form)
    print(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug = True)
