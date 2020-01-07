 
 Los pochocolos


UX
This is a hotel in north colombia south america website. the website offers all the esentials for you to read about the hotel see pictures
and the charity they work along. the website offers a administration pages whrere the owner of the website can update the writing as of when she wants,
delete inappropriate reviews that may be left.


 it has a boyt section that allows for the costumest to meet the teams an know a bit more about the CEO
Features
the website is very easy to use, with rich information

Existing Features
in the administration section the Manager can update delete or add information as they wish to so.
liked to email js to have emails sent to the owner if any questions are needed.
json file to host images but it will be removed in te future to use another data bese to host the images 

.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features Left to Implement
left to implement so that the user can update images,
Another feature idea
to crete a chat room for the charity so that the people that are sposoring the charity coud see live updates of whats going on and be able to commet,
publish ideas.
Technologies Used
JQuery
javaScript
thy both are used to make the website interactive.
python
flask
to make sure the back end is works.
CSS
HTML
BootStrap
to make the website look good and make it mobile responsive.
Testing
Responsiveness Testing
W3
I made the automatically testing using the W3 HTML checker:

W3C Validator - For HTML
JIGSAW W3C Validator - For CSS
Chrome Dev Tools
I used Dev Tools to check if there was an error on my page. Then, I changed what was wrong in the dev tools and I would be able to see the changes in a live update into my browser.Once I've found the issue I went back to Cloud9 at AWS and make the changes there.

Manual Testing
I have tested the website on:

Google Chrome
Apple Safari
Internet Explorer
Mozilla Firefox
and mobile devises 
Contact form:
Go to the "Contact" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.

LOGIN
 if you click on the left top of the page there is a id card icon.
 try loging in with any password and you will get a error messge.
 try using the loging Username= tiggy-curry password= Antigone1 the see that you succesfully log in.
 
REVIEWS
click in the show more and you will se that one one expands



Deployment
My website was created using Cloud9 on AWS and I created an external repository on GitHub and linked it to heroku.

I created a new environment in Cloud9.
Created all my folders and files.
Inside the bash terminal, entered 'git init'.
Entered 'git add .' into the terminal.
Entered 'git commit' into the terminal and created my initial commit.
Followed the below steps to deploy the site to GitHub pages.
This Project was deployed also with Heroku in the following way:

Create Heroku account
Login into Heroku from console heroku login
Create a new empty App on Heroku as none was created before heroku create
Rename App heroku apps: rename my-recipe-cookbook Run this command from App's Root. The empty Heroku Git repository is automatically set as a remote for your local repository. Check git remote -v
Create a Procfile (instruction to Heroku as which file should be used as an entry point for our App) The Procfile must be in your app’s root directory echo web python run.py > Procfile
Create a requirements.txt file sudo pip3 freeze --local > requirements.txt
To deploy git push heroku master
Set the IP,PORT, SECRET_KEY and any other environment variables in Heroku Account Settings



Credits
W3Schools - I used this to ensure I was entering all the information required correctly on my HTML and CSS and even for helping me with the functions on JavaScript.
Stack overflow - Very good and useful website for implement what you need to use one your backend related with Python and Flask.
BootStrap - for giving me a template to work on an make the page mobile responsive
Code institute- for giving me the code to work with 
Content
The text for section Y was copied from the Wikipedia article Z
Media
some photos are the photos that the owner of the hotel as given me the rest of the pictures are from google images to to fill is space they will eventually be removed to add some hotel iamges 