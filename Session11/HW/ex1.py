from flask import Flask, render_template, request, redirect
from bike_data import bike_collection
app = Flask(__name__)


@app.route('/new-bike', methods= ["GET", "POST"])
def new_bike():
  if request.method == "GET":
    return render_template('ex1.html')
  elif request.method == "POST":
    form=request.form
    input_model_py = form["input_model_html"]
    input_dailyfee_py = form["input_dailyfee_html"]
    input_image_py = form["input_image_html"]
    input_year_py = form["input_year_html"]
    bikes = {
      "model":"input_model_py",
      "daily fee":"input_dailyfee_py",
      "image": "input_image_py",
      "year": "input_year_py", 
      }
    bike_collection.insert_one(bikes)
    return redirect("/new-bike")

if __name__ == '__main__':
  app.run( debug=True)
 