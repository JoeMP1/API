from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import datetime as dt
import requests
view = Blueprint(__name__,"Views")

@view.route("/")
def home():
    return render_template("index.html", name = "Tim") #passing a variable(name) to html file

    #https://www.youtube.com/watch?v=kng-mJJby8g or Make A Python Website As Fast As Possible!

@view.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@view.route("/json")
def get_json():
    
    return jsonify({'name': 'Josh', 'swag': 10000})

@view.route("/data")
def get_Data():
    data = request.json
    return jsonify(data)

@view.route("/go-to-home")
def go_to_home():
    return redirect(url_for("Views.home"))

@view.route("/err")
def test():
    return f"<h1> Error </h1>\
             <h2> {city} not found </h2>\
            <form action = '/view' >\
                <input type = 'submit' value = 'back'>\
            </form>\
            "

@view.route("/<place>") # must be the same name as the parameters of the method given below i.e 'place'
def user(place):
    try:
        global city
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        api_keys = "5079eec651a15151708ba799d0792826"
        city = place
        url = base_url + "appid=" + api_keys + "&q=" + city
        response = requests.get(url).json()
        kelvin = response['main']['temp']
        country = response['sys']['country']
        sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
        celsius = kelvin - 273
        return f"<h1> Name of the place </h1>\
                 <h2> {city}</h2>\
                 <h1> Temperature(c): </h1>\
                 <h2> {int(celsius)}c </h2><h1> country: </h1>\
                 <h2>  {country} </h2>\
                 <h1> Sunrisetime: </h1>\
                 <h2> {sunrise_time} </h2>\
                 <img src='pic_trulli.jpg' alt='Trulli' width='500' height='333'>\
                 <form action = '/view' >\
                    <input type = 'submit' value = 'back'>\
                 </form>                                  "
    except:
        return redirect(url_for("Views.test"))

@view.route("/place", methods=['POST', 'GET'])#get and GET did not work
def submit():
    print("This is working")
    Place = request.form.get('Place') #gets the name of the input in html
    if request.method == "POST": # checks if the method type is post
        
        print(f"The name of the place is: {Place}")
        return redirect(url_for("Views.user", place = Place))# calls a method name 'user' in this file
    else:
        return render_template("index.html", username=Place)
    

