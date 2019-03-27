from flask import Flask, render_template
app = Flask(__name__)

poems = [
        {
            "title":"Thơ con cóc",
            "content":"Hôm nay trăng lên cao quá",
            "author":"Huệ",
            "gender":"female"
        },
        {
            "title":"Thơ con ếch",
            "content":"Để thằng bán đồ giữ mất tuổi thanh xuân",
            "author":"Trường",
            "gender":"male"
        }
    ]

@app.route('/')
def index():
    return "Hello C4E27"

@app.route('/say-hi/<name>/<Tuoi>')
def sayhi(name, Tuoi):
    x = int(name) + int(Tuoi)
    return  str(x)

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return str(a + b)


@app.route('/poem')
def poem():
    
    # poem_title = "Thơ con cóc"
    # poem_content = "Hôm nay trăng lên cao quá"
    # poem_author = "Quân"


    # app_poem = {
    #     "title":"Thơ con cóc",
    #     "content":"Hôm nay trăng lên cao quá",
    #     "author":"Quân"
    # }
    return render_template("poem.html", poems = poems)
                                # title=poem_title,
                                # content = poem_content,
                                # author = poem_author)

@app.route('/poem/<int:index>')
def detail(index):
    poem = poems[index]
    return render_template("poem-detail.html", poem=poem, index=index)

if __name__ == '__main__':
  app.run(debug=True)
 




