from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import Users


@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    user = Users.get_all()
    
    return render_template("read.html", users=user)

@app.route('/new_user')
def new_user():
    user = Users.get_all()

    return render_template("create.html",users=user)

@app.route('/users/show/<int:id>')
def show(id):
    data ={
        'id':id
    }
    
    return render_template("read_one.html", user =  Users.show_user(data))

@app.route('/users/show/updated/<int:id>', methods = ['POST'])
def updated(id):

    Users.edit_user(request.form)
    
    return redirect("/users")

@app.route('/users/show/update/<int:id>')
def edit(id):
    data ={'id':id}

    return render_template("update.html", user = Users.show_user(data))

@app.route('/users/show/delete/<int:id>')
def delete_user(id):
    data ={'id':id}
    Users.delete_user(data)
    return redirect('/users')

@app.route('/add_user', methods = ["POST"])
def add_users():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    print(request.form)
    Users.save(data)

    return redirect('/users')