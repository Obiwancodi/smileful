from flask import render_template

from smileful import app
from database import session
from models import Content
from models import User
from models import Scores

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
from random import randrange
from random import shuffle


def calulate_score(scores,values_dict):
    
        values_dict = {str(k):int(v) for k,v in values_dict.iteritems()}
    
        scores_list = []
        
        total_score = 0
        for scoress in values_dict.values():
            total_score +=  scoress
        
        
        scores_dict = {}
        for genre,score in values_dict.iteritems():
            scores_dict[genre] = int(float(score)/(total_score) * 100)
            scores_list.append(score)
        
        
        scores.dark = scores_dict["dark"]
        scores.crass = scores_dict["crass"]
        scores.stand_up = scores_dict["stand_up"]
        scores.satire = scores_dict["satire"]
        scores.dry = scores_dict["dry"]
        scores.sketch_improv= scores_dict["sketch_improv"]
        scores.topical = scores_dict["topical"]
        scores.slapstick = scores_dict["slapstick"]
        scores.surreal = scores_dict["surreal"]
        scores.pardoy = scores_dict["pardoy"]
        
        return scores_dict
        

@app.route("/")
@app.route("/home")
def frontpage():

    return render_template("home.html")

@app.route("/content/", methods=['GET'])
@login_required
def get_content():
    
    user = current_user
    scores = user.scores
    disliked = user.dislike_content
    disliked = [content.id for content in disliked]
    print disliked
    dict_score = scores.make_scores_dict()
    print dict_score
    num = randrange(1,101)
    print num
    for score in dict_score:
        if num - int(dict_score[score]) >= 0:
            num = num - int(dict_score[score])
            continue
        else:
            content_type = score
            print content_type
            content = session.query(Content).filter(Content.genre==content_type,~Content.id.in_(disliked)).all()
            print content
            shuffle(content)
            content = content[0]
            print content.id
            
            if "https://www.youtube" in content.link:
                    url = content.link
                    v_id = url.split('=',1)
                    print v_id[1]
                    return render_template("youtube.html", id=id, content=content, v_id=v_id)
            else:
                    return render_template("content.html", id=id, content=content)
            
@app.route("/content/", methods=["POST"])
@login_required
def dislike_like():
    user= current_user
    content =session.query(Content).get(request.form["content.id"])
    print content.id
    like_dislike = request.form["dislike_like"]
    if like_dislike == "dislike":
        print content.link
        print "dislike"
        user.dislike_content.append(content)
        session.commit()
        return redirect(url_for("get_content"))
    elif like_dislike == "like":
        print "like"
        genre = content.genre
        print genre
        scores = user.scores
        dict_score = scores.make_scores_dict()
        print dict_score
        dict_score[genre] += 1
        print dict_score
        calulate_score(scores,dict_score)
        session.commit()
                
        return redirect(url_for("get_content"))
               
                
@app.route("/preferences1", methods=["GET"])
@login_required
def prefereences_get1():
    return render_template("perferences.html")

@app.route("/preferences1", methods=["POST"])
@login_required
def preferences_post():
    user = current_user
    scores = session.query(Scores).filter(Scores.user_id == user.id).first()
    if not scores:
        scores = Scores(user_id = user.id)
    
    v = calulate_score(scores, request.form)
    print v
    session.add(scores)
    session.commit()
    
    return redirect(url_for("frontpage"))    

@app.route("/editpreferences", methods=["GET"])
@login_required
def prefereences_get2():
    return render_template("editperferences.html")

@app.route("/editpreferences", methods=["POST"])
@login_required
def preferences_edit():
    
    user = current_user
    scores = session.query(Scores).filter(Scores.user_id == user.id).first()
    ve = calulate_score(scores,request.form)
    print ve
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




    
    
