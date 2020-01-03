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
    


        # TODO: write code...
# this line of code will allow costumesr to add reviews
@app.route('/add_review')
def add_review():
    return render_template('add-reviews.html')

     
@app.route('/add_review', methods=['POST'])
def insert_reviews():
    reviews = mongo.db.opinion
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))

# code for conecting templates


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html",company=data, about=mongo.db.about.find())
    
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
   return render_template("rooms.html", page_title="Rooms",fan=mongo.db.fan.find(),ac=mongo.db.ac.find(),cabin=mongo.db.cabin.find(),camp=mongo.db.camp.find())
   
   
# to be able to update the rooms information
@app.route('/update_room')
def update_room_data():
    return render_template("admin-room.html", fan=mongo.db.fan.find())

@app.route('/update_rooms/<fan_id>', methods=["POST"])
def update_rooms(fan_id):
    fan = mongo.db.fan
    fan.update( {'_id': ObjectId(fan_id)},
    {
        'title':request.form.get('title'),
        'price':request.form.get('price'),
        'subject': request.form.get('subject'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
    
@app.route('/update_room_ac')
def update_room_ac():
    return render_template("admin-ac.html", ac=mongo.db.ac.find())

@app.route('/update_rooms_ac/<ac_id>', methods=["POST"])
def update_rooms_ac(ac_id):
    ac = mongo.db.ac
    ac.update( {'_id': ObjectId(ac_id)},
    {
        'title':request.form.get('title'),
        'price':request.form.get('price'),
        'subject':request.form.get('subject'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
    
@app.route('/update_room_cabin')
def update_room_cabin():
    return render_template("admin-cabin.html", cabin=mongo.db.cabin.find())

@app.route('/update_rooms_cabin/<cabin_id>', methods=["POST"])
def update_rooms_cabin(cabin_id):
    cabin = mongo.db.cabin
    cabin.update( {'_id': ObjectId(cabin_id)},
    {
        'title':request.form.get('title'),
        'price':request.form.get('price'),
        'subject':request.form.get('subject'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
    
@app.route('/update_room_camp')
def update_room_camp():
    return render_template("admin-camp.html", camp=mongo.db.camp.find())

@app.route('/update_rooms_camp/<camp_id>', methods=["POST"])
def update_rooms_camp(camp_id):
    camp = mongo.db.camp
    camp.update( {'_id': ObjectId(camp_id)},
    {
        'title':request.form.get('title'),
        'price':request.form.get('price'),
        'subject':request.form.get('subject'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
#  code so that the charity information can be diplayed and the the manager can update the information

@app.route('/charity')
def charity():
   return render_template("charity.html", page_title="charity",data=mongo.db.data.find(), cha=mongo.db.data_cha.find(), char=mongo.db.char.find())
   
   
   
@app.route('/update_charity')
def update_charity_info():
    return render_template("admin-charity.html", char=mongo.db.char.find())


@app.route('/update_charity_info/<char_id>', methods=["POST"])
def update_charity(char_id):
    char = mongo.db.char
    char.update( {'_id': ObjectId(char_id)},
    {
        'title':request.form.get('title'),
        'title2':request.form.get('title2'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
    
@app.route('/update_charity_1')
def update_charity_info_1():
    return render_template("admin-1.html",data=mongo.db.data.find())

    
@app.route('/update_charity_info_1/<data_id>', methods=["POST"])
def update_charity_data(data_id):
    data = mongo.db.data
    data.update( {'_id': ObjectId(data_id)},
    {
        'title':request.form.get('title'),
        'subject':request.form.get('subject'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
    
@app.route('/update_charity_2')
def update_charity_info_2():
    return render_template("admin-2.html",cha=mongo.db.data_cha.find())

    
@app.route('/update_charity_info_2/<cha_id>', methods=["POST"])
def update_charity_data_1(cha_id):
    data_cha = mongo.db.data_cha
    data_cha.update( {'_id': ObjectId(cha_id)},
    {
        'title':request.form.get('title'),
        'subject':request.form.get('subject'),
        
    })
    return redirect(url_for('Admin_update_reviews_and_more'))
   


@app.route('/admin')
def Admin_update_reviews_and_more():
   return render_template("admin.html")
   
# this line of code is for the managers to update their reviews and delete them
@app.route('/admin_reviews')
def Admin_update_reviews():
   return render_template("admin-reviews.html", opinion=mongo.db.opinion.find())
   
   
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
            
   
         
