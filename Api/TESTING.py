from flask import Flask
from Views import view #get the variable 'view' from a different file name 'Views'

app = Flask("hi")# initialise the flask

#url_prefix makes it so that when you enter "/view" or anything, it shows you that only
#e.g http://127.0.0.1:5000/view/ will activate the route under here but http://127.0.0.1:5000/ will lead to error
app.register_blueprint(view, url_prefix="/view") # allows it to communicate with different files

app.run(debug=True, port=8000)