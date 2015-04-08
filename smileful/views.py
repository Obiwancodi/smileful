from flask import render_template

from smileful import app
from database import session
from models import Content
from models import User
from models import Scores

from flask.ext.login import login_required, fresh_login_required
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



def calculate_score(scores,values_dict):
    
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
    if not scores:
        return render_template("No_scores.html")
    disliked = user.dislike_content
    disliked = [content.id for content in disliked]
    seen_content = user.user_seen_content
    seen_content = [content.id for content in seen_content]
    print seen_content
    print disliked
    dict_score = scores.make_scores_dict()
    total_score = 0
    for values in dict_score:
        total_score += dict_score[values]
    print total_score
    print dict_score
    num = randrange(1,total_score+1)
    print num
    for score in dict_score:
        if num - int(dict_score[score]) > 0:
            num = num - int(dict_score[score])
            continue
        else:
            content_type = score
            print content_type
            if user.want_vulgar == 1:
                content = session.query(Content).filter(Content.genre==content_type,~Content.id.in_(disliked),~Content.id.in_(seen_content),Content.vulgar==0).all()
            elif user.want_vulgar == 0:
                content = session.query(Content).filter(Content.genre==content_type,~Content.id.in_(disliked),~Content.id.in_(seen_content)).all()
            if not content:
                return render_template("No_content.html", id=id, content=content)
            print content
            print user.want_vulgar
            shuffle(content)
            content = content[0]
            user.user_seen_content.append(content)
            session.commit()
            print content.id
            print content.vulgar 
            if "https://www.youtube" in content.link:
                    url = content.link
                    v_id = url.split('=',1)
                    print v_id[1]
                    return render_template("youtube.html", id=id, content=content, v_id=v_id)
            else:
                    return render_template("content.html", id=id, content=content)
            
@app.route("/content/", methods=["POST"])
@login_required
def dislike_like_vulgar():
    user= current_user
    content = session.query(Content).get(request.form["content.id"])
    print content.id
    like_dislike_vulgar = request.form["dislike_like_vulgar"]
    print like_dislike_vulgar
    if like_dislike_vulgar == "dislike":
        print content.link
        print "dislike"
        user.dislike_content.append(content)
        session.commit()
        return redirect(url_for("get_content"))
    elif like_dislike_vulgar == "like":
        print "like"
        genre = content.genre
        print genre
        scores = user.scores
        dict_score = scores.make_scores_dict()
        print dict_score
        dict_score[genre] += 1
        print dict_score
        calculate_score(scores,dict_score)
        session.commit()       
        return redirect(url_for("get_content"))
    elif like_dislike_vulgar =="vulgar":
        content.vulgar = 1
        session.commit()
        return redirect(url_for("get_content"))
    

                
@app.route("/preferences", methods=["GET"])
@login_required
def preferences_get():
    return render_template("preferences.html")

@app.route("/preferences", methods=["POST"])
@login_required
def preferences_post():
    user = current_user
    scores = session.query(Scores).filter(Scores.user_id == user.id).first()
    if not scores:
        scores = Scores(user_id = user.id)
    try:
        v = calculate_score(scores, request.form)
    except ZeroDivisionError:
        return render_template("All_zeros.html")
    print v
    session.add(scores)
    session.commit()
    flash("Preferences Saved","danger")
    return redirect(url_for("frontpage"))    

@app.route("/editpreferences", methods=["GET"])
@login_required
def editpreferences_get():
    return render_template("editpreferences.html")

@app.route("/editpreferences", methods=["POST"])
@login_required
def preferences_edit():
    
    user = current_user
    scores = session.query(Scores).filter(Scores.user_id == user.id).first()
    try:
        ve = calculate_score(scores, request.form)
    except ZeroDivisionError:
        return render_template("All_zeros.html")
    
    print ve
    session.commit()
    flash("Preferences Saved","danger")
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
    
    user.user_seen_content = []
    session.commit()
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



@app.route("/vulgar")
@login_required
def vulgar():
    user = current_user
    if user.want_vulgar == 0:
        user.want_vulgar = 1
        session.commit()
        flash("Vulgar Content Turned Off","danger")
        return redirect(url_for('frontpage'))
    
    elif user.want_vulgar == 1:
        user.want_vulgar = 0
        session.commit()
        flash("Vulgar Content Turned On", "danger")
        return redirect(url_for('frontpage'))
        
    
    
    
