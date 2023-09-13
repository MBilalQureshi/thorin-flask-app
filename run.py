# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application

# The first thing we need to do, is import the 'request' library from Flask.
# Request is going to handle things like finding out what method we used, and it will also
# contain our form object when we've posted it.

# What we want to do next, is display some feedback to the user.
# To do that, we are going to import a function from Flask called 'flash'.
# Sometimes we want to display a non-permanent message to the user, something that only stays
# on screen until we refresh the page, or go to a different one.
# These are called 'flashed messages' in Flask.
import json
import os
from flask import Flask, render_template, request, flash
# capital F of Flask as its a class name

# import only if system finds env.py file
if os.path.exists("env.py"):
    import env

# instace of class is app
#  This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# In Python, a decorator starts with the @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.

@app.route("/")
# below function is also know as view
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company= data)


@app.route("/about/<member_name>")
# member_name is taken from above as an argument and the value that's inside it comes from about.html -> href link member.url ->json file
def about_member(member_name):
    # return "<h1>" + member_name + "</h1>"
    member = {}
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return "<h1>" + member["name"] + "</h1>"
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # print(request.form)
        # print(request.form.get("name")) better option tha below
        # print(request.form["email"])
        # The name will be injected in {} below
        flash("Thanks {}, we have recived your message".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Career")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug=True
    )