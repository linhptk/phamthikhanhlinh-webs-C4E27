# flask --> Xay dung wweb, nen tang, build web nhanh hon
# flask snippet --> code nhanh hon
# 127.0.0.1: local host
# 5000: port(cong)
# @app.route('/') --> / la homepage

# poem.html: html:5


# Chuyển dữ liệu từ app.py sang poem.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
# </head>
# <body>
#     <h3>{{ title }}</h3>
#     <p>
#         {{ content }}
#     </p>
#     <h5>By: {{ author}}</h5>
#     <hr>

# {{poem}}
    <h3>{{poem.title}}</h3>
    <p>{{poem.content}}</p>
    <h5>{{poem.author}}</h5>
    <hr>

# {{poem}}
#     <h3>{{poem["title"]}}</h3>
#     <p>{{poem["content"]}}</p>
#     <h5>{{poem["author"]}}</h5>
#     <hr>

# http://jinja.pocoo.org/docs/2.10/