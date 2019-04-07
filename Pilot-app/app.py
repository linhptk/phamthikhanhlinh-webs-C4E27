from flask import Flask, render_template, redirect, request, session
# from flask import *
from services import Services
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["SECRET_KEY"] = "phamkhanhlinh"

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/all-service')
def all_service():
  if "logged" in session:
    if session["logged"] == True:
      persons = Services.find()
      # print(persons)
      return render_template("all_service.html",all_persons=persons)
    else:
      return redirect("/login")
  else:
    return redirect("/login")

@app.route('/all-service/detail/<id>')
def detail(id):
    detail_person = Services.find_one({"_id": ObjectId(id)})
    # print(detail_person)
    return render_template("service-detail.html", detail_person=detail_person)

@app.route('/all-service/<g>')
def gender(g):
  services = Services.find({"gender":g})
  return render_template("all_service.html", all_persons=services)
@app.route('/all-service/delete/<id>')
def delete(id):
  delete_person = Services.find_one({"_id":ObjectId(id)})
  Services.delete_one(delete_person)
  return redirect ('/all-service')

@app.route('/all-service/update/<id>', methods=["GET", "POST"])
def update(id):
  update_service = Services.find_one({"_id": ObjectId(id)})
  if request.method == "GET":
    # print(update_service)
    return render_template("update-service.html", update_service= update_service)
  elif request.method == "POST":
    form = request.form
    service_name = form["input_name"]
    service_age = form["input_age"]
    service_gender = form["input_gender"]
    service_height = form["input_height"]
    service_address = form["input_address"]
    service_available = form["input_available"]
    # print(form["input_name"])
    new_value = {
      "$set":{
        "name":service_name,
        "age":service_age,
        "address":service_address,
        "gender":service_gender,
        "height":service_height,
        "available":service_available,
      }
    }
    Services.update_one(update_service, new_value)
    return redirect("/all-service/detail/{0}".format(id))

@app.route('/login', methods = ["GET", "POST"])
def login():
  if session["logged"] == True:
    return redirect("/all-service")
  else:
    if request.method == "GET":
      return render_template("login.html")
    elif request.method == "POST":
      username_admin = "admin" 
      password_admin = "admin"
      form= request.form
      input_username = form["input_username"]
      input_password = form["input_password"]
      if input_username == username_admin and input_password == password_admin:
        session["logged"] = True
        
        return "logged in"
      else:
        return redirect("/login")
@app.route('/logout', methods = ["GET", "POST"])
def logout():
  if "logged" in session:
    session["logged"] = False
    return redirect("/login")
  else:
    return redirect("/login")

if __name__ == '__main__':
  app.run(debug=True)
 