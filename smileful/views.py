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


def calulate_score(scores,genres):
        scores_list = []
        
        total_score = 0
        for genre in genres:
            total_score +=  genre
        print total_score   
        for genre in genres:
            score = float(genre)/(total_score) * 100
            scores_list.append(score)
            
        scores.dark = scores_list[0]
        scores.crass = scores_list[1]
        scores.stand_up = scores_list[2]
        scores.satire = scores_list[3]
        scores.dry = scores_list[4]
        scores.sketch_improv= scores_list[5]
        scores.topical = scores_list[6]
        scores.slapstick = scores_list[7]
        scores.surreal = scores_list[8]
        scores.pardoy = scores_list[9]
        
        print scores_list
        print scores.dark
        return scores_list

@app.route("/")
@app.route("/home")
def frontpage():

    return render_template("base.html")

@app.route("/content/", methods=['GET'])
@login_required
def get_content():
    
    user = current_user
    scores = user.scores
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
            content = session.query(Content).filter(Content.genre==content_type).all()
            shuffle(content)
            content = content[0]
            
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
        for score in dict_score:
            if not score == genre:
                continue
            else:
                print score
                dict_score[score] = dict_score[score] + 1
                print dict_score
                calulate_score(scores,[dict_score[score] for score in dict_score])
                print dict_score
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
      
    dark = int(request.form["dark"])
    crass = int(request.form["crass"])
    stand_up = int(request.form["stand_up"])
    satire = int(request.form["satire"])
    dry = int(request.form["dry"])
    sketch_improv = int(request.form["sketch_improv"])
    topical = int(request.form["topical"])
    slapstick = int(request.form["slapstick"])
    surreal = int(request.form["surreal"])
    pardoy = int(request.form ["pardoy"])
    genres = [dark,crass,stand_up,satire,dry,sketch_improv,topical,slapstick,surreal,pardoy]
    
    calulate_score(scores,genres)
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
    
    dark = int(request.form["dark"])
    crass = int(request.form["crass"])
    stand_up = int(request.form["stand_up"])
    satire = int(request.form["satire"])
    dry = int(request.form["dry"])
    sketch_improv = int(request.form["sketch_improv"])
    topical = int(request.form["topical"])
    slapstick = int(request.form["slapstick"])
    surreal = int(request.form["surreal"])
    pardoy = int(request.form ["pardoy"])
    calulate_score(scores,request.form)
    session.commit()
    
    return redirect(url_for("frontpage"))




@app.route("/like/<id>",methods=["POST"])
@login_required
def like_content(id):
    user = current_user
    content = query.session(Content).get(id)
    user.like_content = content
    content.genre = like_genre
    
    session.commit()
    
    
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




    
    
