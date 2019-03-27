from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    about_me_pys = {"name":"Pham Khanh Linh",
    "work":"office worker",
    "school": "UTT",
    "crush":"Cún",
    }
    return render_template("ex1.html", about_me_html = about_me_pys)
@app.route('/school')
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run(debug=True)
 