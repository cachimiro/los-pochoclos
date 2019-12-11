import os
import json
from flask import Flask, render_template, request,redirect, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'reviews'
app.config["MONGO_URI"] = "mongodb+srv://root:Johann@myfirstcluster-ugp0n.mongodb.net/reviews?retryWrites=true&w=majority"

mongo = PyMongo(app)
app.secret_key = "cachimiro"

# code to be ble to see reviews
@app.route('/view_reviews')
def get_reviews():
    return render_template("reviews.html", opinion=mongo.db.opinion.find())
    
# this line of code will allow costumesr to add reviews
@app.route('/add_review')
def add_review():
    return render_template('add-reviews.html')

     
@app.route('/add_review', methods=['POST'])
def insert_task():
    tasks = mongo.db.opinion
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))

# code for conecting templates
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", member=member)
    
    


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
   return render_template("careers.html", page_title="careers")

@app.route('/charity')
def charity():
   return render_template("charity.html", page_title="charity")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            
# chat function will go here all the code thats going to be provided from here is for that chat area
#pesonal note i will coment out this section for a moment need to work on other html 
"""
import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = os.getenv("SECRET","randomstring123")
messages = []


def add_message(username, message):
    #Add messages to the `messages` list
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


@app.route("/", methods=["GET", "POST"])
def chat_room():
    #Main page with instructions
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    #Add and display chat messages
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username=username,
                           chat_messages=messages)


app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=False)
       
 """
 
 