from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users_py = {
        "Linh":{
            "name":"Pham Khanh Linh",
            "gender":"female",
            "age": "23",
        },
        "Hanh":{
            "name":"Pham Nguyen Hanh",
            "gender":"female",
            "age":"21",
        },
        "Lam":{
            "name":"Pham Tung Lam",
            "gender":"male",
            "age":"13",
        },  
    }

    if username in users_py:
        return render_template('Serious excercise2.html', username=users_py[username], users_html=users_py)
    else:
        return "User not found!" 

if __name__ == '__main__':
  app.run(debug=True)
