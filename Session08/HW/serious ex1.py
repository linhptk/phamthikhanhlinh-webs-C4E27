from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight, height):
    heightNumber = float(height) / 100
    BMI_py =  float(weight / (heightNumber * heightNumber))
    if BMI_py < 16:
        BMI = ("BMI=" + str(BMI) + ".BMI < 16 : Severely underweight")
    elif 16 <= BMI_py < 18.5:
        BMI = ("BMI="+ str(BMI) + "16 <= BMI < 18.5: Underweight")
    elif 18.5 <= BMI_py <25:
        BMI = ("BMI=" + str(BMI) + "18.5 <= BMI < 25: Normal")
    elif 25 <= BMI_py < 30:
        BMI = ("BMI=" + str(BMI) + "25 <= BMI < 30: Overweight")
    else:
        BMI = ("BMI=" + str(BMI) + "BMI > 30: Obese")
    return render_template("Serious excercise1.html", BMI_html=BMI_py)

if __name__ == '__main__':
  app.run(debug=True)
 