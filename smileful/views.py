from flask import render_template

from smileful import app
from database import session
from models import Content
from models import User

from flask.ext.login import login_required
from flask.ext.login import current_user
from flask import flash
from flask.ext.login import login_user
from werkzeug.security import check_password_hash
from .models import User
from flask import request, redirect, url_for
from login import load_user
from flask.ext.login import logout_user
from werkzeug.security import generate_password_hash


@app.route("/")
@app.route("/home")
def frontpage():

    return render_template("base.html")

@app.route("/content/<id>", methods=["GET"])
def get_content(id):
    content= session.query(Content).get(id)
    if "https://www.youtube" in content.link:
        url = content.link
        v_id = url.split('=',1)
        print v_id[1]
        return render_template("youtube.html", id=id, content=content, v_id=v_id)
         
    else:
        return render_template("content.html", id=id, content=content)
    
@app.route("/preferences1", methods=["GET"])
@login_required
def prefereences_get1():
    return render_template("perferences.html")

@app.route("/preferences1", methods=["POST"])
@login_required
def preferences_post():
    user = current_user
    user.dark = request.form["dark"]
    user.crass = request.form["crass"]
    user.stand_up = request.form["stand_up"]
    user.satire = request.form["satire"]
    user.dry = request.form["dry"]
    user.animated = request.form["animated"]
    user.topical = request.form["topical"]
    user.slapstick = request.form["slapstick"]
    user.surreal = request.form["surreal"]
    user.situational = request.form["situational"]
    user.improv = request.form ["improv"]
    session.commit()
    
    return redirect(url_for("frontpage"))    
        
@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login_get"))

    login_user(user)
    return redirect(request.args.get('next') or url_for("frontpage"))

@app.route("/newlogin", methods=["GET"])
def new_login():
    return render_template("new_login.html")

@app.route("/newlogin",  methods=["POST"])
def new_user():
    user = User(
           email = request.form["email"],
           password = request.form["password"]
    )
    email = user.email
    if session.query(User).filter_by(email=email).first():
            flash("Email already used by another account", "danger")
            return redirect(url_for("new_login"))
    
    password2 = request.form["password2"]
        
    if not user.password == password2:
        flash("Passwords do not match","danger")
        return redirect(url_for("new_login"))
    
    
    user.password = generate_password_hash(user.password)
    session.add(user)
    session.commit()
    login_user(user)
    return redirect(request.args.get('next') or url_for("frontpage"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('frontpage'))




    
    
