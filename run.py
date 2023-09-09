# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
import os
from flask import Flask, render_template
# capital F of Flask as its a class name

# instace of class is app
#  This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# In Python, a decorator starts with the @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.

@app.route("/")
# below function is also know as view
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug=True
    )