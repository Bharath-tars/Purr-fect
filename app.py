from flask import Flask, flash, redirect, render_template, request
from helpers import apology, login_required, lookup, usd
from apisuma import request_text

app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
        return render_template("about.html")


@app.route("/textsummarize",methods=["GET","POST"])
def textsummarize():
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        text = request.form.get("text")
        message, summary, full_data = request_text(name,email,text)
        return render_template("result.html",message=message,summary=summary,full_data=full_data,name=name,email=email)
    else:
        return render_template("textsummarize.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
    else:
        return render_template("contact.html")




