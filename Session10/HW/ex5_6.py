# MÌNH TÌM MÃI MÀ KHÔNG HIỂU VÌ SAO MÌNH CHẠY 2 FILE HTML: EX5.HTML VÀ EX6.HTML NÓ KHÔNG RA KẾT QUẢ 

from flask import Flask, render_template
from mlab import river_collection
app = Flask(__name__)


@app.route('/river-africa')
def river_africa():
    all_river_py = list(river_collection.find())
    return render_template('ex5.html', all_river_html= all_river_py)

@app.route('/river-samerica')
def river_samerica():
    all_river_py2 = list(river_collection.find())
    return render_template("ex6.html", all_river_html2= all_river_py2)
if __name__ == '__main__':
  app.run(debug=True)
 