import os
import json
import click
from flask import Flask, render_template, request,redirect, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'reviews'
app.config["MONGO_URI"] = "mongodb+srv://root:Johann@myfirstcluster-ugp0n.mongodb.net/reviews?retryWrites=true&w=majority"

mongo = PyMongo(app)
app.secret_key = "cachimiro"
@app.route('/')
def index():
    return render_template("index.html")


# code to be ble to see reviews
@app.route('/view_reviews')
def get_reviews():
    return render_template("reviews.html", opinion=mongo.db.opinion.find())
    

    
 # code to shorten reviews so they are not to overwelming 

        # TODO: write code...
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
    
    


@app.route('/contact')
def contact():  
 return render_template("contact.html", page_title="Contact",)


@app.route('/rooms')
def rooms():
   return render_template("rooms.html", page_title="Rooms")

@app.route('/charity')
def charity():
   return render_template("charity.html", page_title="charity")
   
@app.route('/administration')
def Admin_update_reviews_and_more():
   return render_template("admin.html", opinion=mongo.db.opinion.find())
   
# this line of code is for the managers to update their reviews and delete them
@app.route('/edit_review/<opinion_id>')
def edit_review(opinion_id):
    the_opinion =  mongo.db.opinion.find_one({"_id": ObjectId(opinion_id)})
    return render_template('update.html', opinion=the_opinion)
                           
                           
@app.route('/update_opinion/<opinion_id>', methods=["POST"])
def update_opinion(opinion_id):
    opinion = mongo.db.opinion
    opinion.update( {'_id': ObjectId(opinion_id)},
    {
        'name':request.form.get('name'),
        'surname':request.form.get('surname'),
        'Title': request.form.get('Title'),
        'Opinion': request.form.get('Opinion'),
        'how_would_you_improve_it':request.form.get('how_would_you_improve_it')
    })
    return redirect(url_for('Admin_update_reviews_and_more'))


@app.route('/delete_opinion/<opinion_id>')
def delete_opinion(opinion_id):
    mongo.db.opinion.remove({'_id': ObjectId(opinion_id)})
    return redirect(url_for('Admin_update_reviews_and_more'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
   
         
