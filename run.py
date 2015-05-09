import os
from flask.ext.script import Manager
from smileful import app


from werkzeug.security import generate_password_hash
from smileful.models import User,Scores

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
from smileful.models import Content
from smileful.database import session

@manager.command
def seed():
    content = Content(link="http://en.wikipedia.org/wiki/Crass",
    genre="crass")
    session.add(content)
    session.commit()
    
    
@manager.command
def seed2():
    content = Content(link="http://bulbapedia.bulbagarden.net/wiki/Dark_%28type%29",
    genre="dark")
    session.add(content)
    session.commit()
    
@manager.command
def adduser():
    email = raw_input("Email: ")
    if session.query(User).filter_by(email=email).first():
        print "User with that email address already exists"
        return
     
    password = ""
    password_2 = ""
    while not (password and password_2) or password != password_2:
        password = getpass("Password: ")
        password_2 = getpass("Re-enter password: ")
    user = User(email=email,
                password=generate_password_hash(password))
    session.add(user)
    session.commit()

@manager.command
def seed3():
    content1 = Content(link="http://c2.com/cgi/wiki?DontRepeatYourself",
    genre="dry")
    content2 = Content(link="http://www.cc.com/stand-up",
                      genre="stand_up")
    content3 = Content(link="http://www.theonion.com/",
                      genre="satire")
    content4 = Content(link="http://goanimate.com/",
                      genre="pardoy")
    content5 = Content(link="http://alwaysfunny.com/",
                      genre="topical")
    content6 = Content(link="http://dictionary.reference.com/browse/slapstick",
                      genre="slapstick")
    content7 = Content(link="http://en.wikipedia.org/wiki/Surreal",
                      genre="surreal")
    content9 = Content(link="http://improv.com/index.cfm",
                      genre="sketch_improv")
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content9])
    session.commit()

@manager.command
def seed4():
    content = Content(link="https://www.youtube.com/watch?v=UBXbz8Kunss",
                     genre="crass")
    session.add(content)
    session.commit()
@manager.command
def stand_up_content():
    content1 = Content(link="https://www.youtube.com/watch?v=9FPv2toi5og", genre="stand_up")
    content2 = Content(link="https://www.youtube.com/watch?v=HjLr7Duq3B8", genre="stand_up")
    content3 = Content(link="https://www.youtube.com/watch?v=znn4Y3AC37c", genre="stand_up")
    content4 = Content(link="https://www.youtube.com/watch?v=GUlf1F05gTA", genre="stand_up")
    content5 = Content(link="https://www.youtube.com/watch?v=UZ4FLl-2Py0", genre="stand_up")
    content6 = Content(link="https://www.youtube.com/watch?v=c_SaTwOFcz0", genre="stand_up")
    content7 = Content(link="https://www.youtube.com/watch?v=gmlFzw5xvoE", genre="stand_up")
    content8 = Content(link="https://www.youtube.com/watch?v=aM1QhIBFBVs", genre="stand_up")
    content9 = Content(link="https://www.youtube.com/watch?v=MvgN5gCuLac", genre="stand_up")
    content10 = Content(link="https://www.youtube.com/watch?v=VSsI4dGddr8", genre="stand_up")
    content11 = Content(link="http://www.cc.com/video-clips/kepxs1/stand-up-dane-cook--uncensored---ending-relationships", genre="stand_up")
    content12 = Content(link="http://www.cc.com/video-clips/q4idyc/stand-up-amy-schumer--uncensored---giving-advice-to-the-audience", genre="stand_up")
    content13 = Content(link="http://www.cc.com/video-clips/1x9hrv/comedy-central-presents-baby-cuteness", genre="stand_up")
    content14 = Content(link="https://www.youtube.com/watch?v=J-q2-eSI4h8", genre="stand_up")
    content15 = Content(link="https://www.youtube.com/watch?v=rfLf8agsN5Y", genre="stand_up")
    content16 = Content(link="https://www.youtube.com/watch?v=SLXCfO2PEUs", genre="stand_up")
    content17 = Content(link="https://www.youtube.com/watch?v=pAaqpqDGlhQ", genre="stand_up")
    content18 = Content(link="https://www.youtube.com/watch?v=F_2_e1nwtKs", genre="stand_up")
    content19 = Content(link="http://www.cc.com/video-clips/ntqo57/russell-simmons-presents-the-ruckus-is-born", genre="stand_up")
    content20 = Content(link="https://www.youtube.com/watch?v=wUG2DvhobQE", genre="stand_up")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def sketch_improv_content():
    content1 = Content(link="https://www.youtube.com/watch?v=3qqE_WmagjY", genre="sketch_improv")
    content2 = Content(link="https://www.youtube.com/watch?v=kMwiBBCLT3o", genre="sketch_improv")
    content3 = Content(link=" https://www.youtube.com/watch?v=L3dq9dxEf2c", genre="sketch_improv")
    content4 = Content(link="https://www.youtube.com/watch?v=XCNYPwCRRYw", genre="sketch_improv")
    content5 = Content(link="https://www.youtube.com/watch?v=13wEuXLk958", genre="sketch_improv")
    content6 = Content(link="https://www.youtube.com/watch?v=7W_qrc-TkR8", genre="sketch_improv")
    content7 = Content(link="https://www.youtube.com/watch?v=V2b21yAeEpQ", genre="sketch_improv")
    content8 = Content(link="https://www.youtube.com/watch?v=fCXzEyVdFl0", genre="sketch_improv")
    content9 = Content(link="https://www.youtube.com/watch?v=NYANlrcoT_w", genre="sketch_improv")
    content10 = Content(link="https://www.youtube.com/watch?v=nY9Sxg8L8SM", genre="sketch_improv")
    content11 = Content(link="https://www.youtube.com/watch?v=GLa6dl9U6h8", genre="sketch_improv")
    content12 = Content(link="https://www.youtube.com/watch?v=rH0Tdxybvic", genre="sketch_improv")
    content13 = Content(link="https://www.youtube.com/watch?v=1BNgRpRuWGs", genre="sketch_improv")
    content14 = Content(link="https://www.youtube.com/watch?v=1UXHiPWrZxg", genre="sketch_improv")
    content15 = Content(link="https://www.youtube.com/watch?v=fhO7dMEthK4", genre="sketch_improv")
    content16 = Content(link="https://www.youtube.com/watch?v=wBij_rEXdCk", genre="sketch_improv")
    content17 = Content(link="https://www.youtube.com/watch?v=qUznIgxrkX8", genre="sketch_improv")
    content18 = Content(link="https://www.youtube.com/watch?v=VWuJHbVZBQg", genre="sketch_improv")
    content19 = Content(link="https://www.youtube.com/watch?v=Dd7FixvoKBw", genre="sketch_improv")
    content20 = Content(link="https://www.youtube.com/watch?v=xccz5qvv0AI", genre="sketch_improv")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def dark_content():
    content1 = Content(link="https://www.youtube.com/watch?v=eNMKZww0Z9A", genre="dark")
    content2 = Content(link="http://www.cc.com/video-clips/tp6kjq/comedy-central-presents-don-t-stab-me", genre="dark")
    content3 = Content(link="http://www.cc.com/video-clips/gzsuf7/comedy-central-presents-alcoholics-anonymous", genre="dark")
    content4 = Content(link="http://www.cc.com/video-clips/t3xa69/comedy-central-presents-suicide-squads", genre="dark")
    content5 = Content(link="http://www.cc.com/video-clips/9fz12y/comedy-central-presents-til-death-do-you-part", genre="dark")
    content6 = Content(link="http://www.cc.com/video-clips/r6h4zw/comedy-central-presents-hut-of-pain", genre="dark")
    content7 = Content(link="http://www.cc.com/video-clips/9y43ia/comedy-central-presents-too-graphic--too-sad", genre="dark")
    content8 = Content(link="http://www.cc.com/video-clips/i4unyh/comedy-central-presents-baby-safety", genre="dark")
    content9 = Content(link="http://tosh.cc.com/video-clips/xp6mc0/how-are-you-turkeys-doing-tonight-", genre="dark")
    content10 = Content(link="http://www.cc.com/video-clips/3shdyv/comedy-central-presents-a-level-of-self-consciousness", genre="dark")
    content11 = Content(link="http://www.cc.com/video-clips/sia1cg/new-york-comedy-festival-things-have-gotten-dark-again", genre="dark")
    content12 = Content(link="http://www.cc.com/video-clips/c78qfv/live-at-gotham-horror", genre="dark")
    content13 = Content(link="http://www.cc.com/video-clips/t0djw6/john-oliver-s-new-york-stand-up-show-progressive-city", genre="dark")
    content14 = Content(link="http://www.cc.com/video-clips/9lmleq/live-at-gotham-stranger-s-funeral", genre="dark")
    content15 = Content(link="http://www.cc.com/video-clips/wf06hp/john-oliver-s-new-york-stand-up-show-trial-separation", genre="dark")
    content16 = Content(link="http://www.cc.com/video-clips/5pgvpp/mind-of-mencia-anti-fat-bias", genre="dark")
    content17 = Content(link="http://www.cc.com/video-clips/yv2kg1/stand-up-christopher-titus--on-behalf-of-whitey", genre="dark")
    content18 = Content(link="http://www.cc.com/video-clips/340oq2/stand-up-tracy-morgan--drugs-in-sports", genre="dark")
    content19 = Content(link="http://www.cc.com/video-clips/n2wecg/comedy-central-presents-sex-in-the-dark", genre="dark")
    content20 = Content(link="http://www.cc.com/video-clips/sdx9x3/comedy-central-presents-look-of-hope", genre="dark")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def pardoy_content():
    content1 = Content(link="https://www.youtube.com/watch?v=oPpzJAzdpTU", genre="pardoy")
    content2 = Content(link="https://www.youtube.com/watch?v=Ol2DedEhOGI", genre="pardoy")
    content3 = Content(link="https://www.youtube.com/watch?v=4eY4qU80lPM", genre="pardoy")
    content4 = Content(link="https://www.youtube.com/watch?v=8Nfm-iWo3v8", genre="pardoy")
    content5 = Content(link="https://www.youtube.com/watch?v=QAY5b8AEXDc", genre="pardoy")
    content6 = Content(link="https://www.youtube.com/watch?v=ZrHmcpRAZNs", genre="pardoy")
    content7 = Content(link="http://www.cc.com/video-clips/ou2qyy/comedy-central-presents-abbott---costello", genre="pardoy")
    content8 = Content(link="http://thedailyshow.cc.com/videos/em87ho/putting-on-a-great-show", genre="pardoy")
    content9 = Content(link="http://tosh.cc.com/video-clips/kcqbmd/nba--where-amazing-happens-parody", genre="pardoy")
    content10 = Content(link="http://www.cc.com/video-clips/hzf8y5/mind-of-mencia-dateline-punk-d", genre="pardoy")
    content11 = Content(link="http://www.cc.com/video-clips/p5tk9x/nathan-for-you-dumb-starbucks", genre="pardoy")
    content12 = Content(link="http://www.cc.com/video-clips/vv5nd5/key-and-peele--the-exorcist--revisited", genre="pardoy")
    content13 = Content(link="https://www.youtube.com/watch?v=gcSVyntYuRY", genre="pardoy")
    content14 = Content(link="http://thecolbertreport.cc.com/videos/ane28t/america-strikes-back---episode-ii---return-of-the-america-strikes-back--again", genre="pardoy")
    content15 = Content(link="https://www.youtube.com/watch?v=z3eN9u5N2Q4", genre="pardoy")
    content16 = Content(link="https://www.youtube.com/watch?v=a_zCqKTS5o0", genre="pardoy")
    content17 = Content(link="https://www.youtube.com/watch?v=cnoZeGkhFGo", genre="pardoy")
    content18 = Content(link="https://www.youtube.com/watch?v=Z6xXEaWz5Iw", genre="pardoy")
    content19 = Content(link="https://www.youtube.com/watch?v=mRVvUUerOsI", genre="pardoy")
    content20 = Content(link="https://www.youtube.com/watch?v=0zVK4BpWORE", genre="pardoy")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def satire_content():
    content1 = Content(link="https://www.youtube.com/watch?v=2AAa0gd7ClM", genre="satire")
    content2 = Content(link="https://www.youtube.com/watch?v=Zugm5fGtNiA", genre="satire")
    content3 = Content(link="https://www.youtube.com/watch?v=kRCdgZC98_A", genre="satire")
    content4 = Content(link="http://www.cc.com/video-clips/grjpe1/new-york-comedy-festival-political-satire-in-2009", genre="satire")
    content5 = Content(link="https://www.youtube.com/watch?v=T-B7l-ZMcN8", genre="satire")
    content6 = Content(link="http://www.bing.com/videos/search?q=satire+comedy+examples&FORM=HDRSC3#view=detail&mid=7BD612FD157299906E257BD612FD157299906E25", genre="satire")
    content7 = Content(link="http://www.cc.com/video-clips/66u7us/the-sarah-silverman-program-brian-and-steve-in-the-bad-van", genre="satire")
    content8 = Content(link="https://www.youtube.com/watch?v=hmuF3SJhWI4", genre="satire")
    content9 = Content(link="http://www.bing.com/videos/search?q=satire%20comedy&qs=VI&form=QBVR&pq=satire&sc=8-6&sp=5&sk=VI4#view=detail&mid=B8B99B2315D9982A858BB8B99B2315D9982A858B", genre="satire")
    content10 = Content(link="http://www.bing.com/videos/search?q=satire%20comedy&qs=VI&form=QBVR&pq=satire&sc=8-6&sp=5&sk=VI4#view=detail&mid=88C1B6DEFE3586B12C3B88C1B6DEFE3586B12C3B", genre="satire")
    content11 = Content(link="https://www.youtube.com/watch?v=Zugm5fGtNiA", genre="satire")
    content12 = Content(link="https://www.youtube.com/watch?v=qOS2cFagZSE", genre="satire")
    content13 = Content(link="http://www.cc.com/video-clips/lg9i2t/comedy-central-presents-detailed-cheering", genre="satire")
    content14 = Content(link="http://www.cc.com/video-clips/odbdlm/comedy-central-presents-laugh-the-tears-away", genre="satire")
    content15 = Content(link="http://thecolbertreport.cc.com/videos/g12gwt/the-eruption-of-mt--stephen", genre="satire")
    content16 = Content(link="http://thedailyshow.cc.com/videos/6mibvz/parliament-slight", genre="satire")
    content17 = Content(link="https://www.youtube.com/watch?v=vnQe2DosQnc", genre="satire")
    content18 = Content(link="https://www.youtube.com/watch?v=i5ZM0-f5_CU", genre="satire")
    content19 = Content(link="https://www.youtube.com/watch?v=pS5YG--PwDU", genre="satire")
    content20 = Content(link="https://www.youtube.com/watch?v=9uxIe7W0yWs", genre="satire")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def dry_content():
    content1 = Content(link="https://www.youtube.com/watch?v=WxuhISNpZFk", genre="dry")
    content2 = Content(link="http://www.cc.com/video-clips/fb5nqp/comedy-central-presents-southern-accents", genre="dry")
    content3 = Content(link="http://www.cc.com/video-clips/s801oy/comedy-central-presents-dry-spell", genre="dry")
    content4 = Content(link="http://www.cc.com/video-clips/0obkxa/live-at-gotham-iraqachusetts", genre="dry")
    content5 = Content(link="https://www.youtube.com/watch?v=EzS0wfehYbI", genre="dry")
    content6 = Content(link="https://www.youtube.com/watch?v=s7AXskSxxMk", genre="dry")
    content7 = Content(link="https://www.youtube.com/watch?v=T1vqaRkqTQs", genre="dry")
    content8 = Content(link="http://www.cc.com/video-clips/dmuhxg/comedy-central-presents-staten-island-zoo", genre="dry")
    content9 = Content(link="http://www.cc.com/video-clips/10swv3/live-at-gotham-fourth-trimester", genre="dry")
    content10 = Content(link="https://www.youtube.com/watch?v=Ej8EaLF382c", genre="dry")
    content11 = Content(link="https://www.youtube.com/watch?v=Fg_XskS1Rmk", genre="dry")
    content12 = Content(link="https://www.youtube.com/watch?v=qfh6tf8AF4s", genre="dry")
    content13 = Content(link="http://www.cc.com/video-clips/zlctk7/comedy-central-presents-bob-the-builder", genre="dry")
    content14 = Content(link="http://www.cc.com/video-clips/z5n7in/john-oliver-s-new-york-stand-up-show-save-your-sandals", genre="dry")
    content15 = Content(link="https://www.youtube.com/watch?v=XxNMuHWOASg", genre="dry")
    content16 = Content(link="https://www.youtube.com/watch?v=-4a0VC7aXZM", genre="dry")
    content17 = Content(link="http://www.cc.com/video-clips/sd1boa/comedy-central-presents-half-asser", genre="dry")
    content18 = Content(link="http://www.cc.com/video-clips/pw1vym/stand-up-patton-oswalt--50th-street-grime-tunnel", genre="dry")
    content19 = Content(link="http://www.cc.com/video-clips/j0e6ct/comedy-central-presents-old-soul", genre="dry")
    content20 = Content(link="http://www.cc.com/video-clips/sd1boa/comedy-central-presents-half-asser", genre="dry")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def topical_content():
    content1 = Content(link="https://www.youtube.com/watch?v=fUEd2dyItuE", genre="topical")
    content2 = Content(link="http://thecolbertreport.cc.com/videos/ilh2wg/on-topic---the-environment---awww--animals-", genre="topical")
    content3 = Content(link="http://www.cc.com/video-clips/d9ddhn/comedy-central-presents-jackie-robinson", genre="topical")
    content4 = Content(link="https://www.youtube.com/watch?v=oMCKaBku83U", genre="topical")
    content5 = Content(link="https://www.youtube.com/watch?v=gqfJ51e1i8g", genre="topical")
    content6 = Content(link="https://www.youtube.com/watch?v=ewpZ_fTc0pU", genre="topical")
    content7 = Content(link="http://www.cc.com/video-clips/psosrl/live-at-gotham-new-yorkers", genre="topical")
    content8 = Content(link="http://www.cc.com/video-clips/83dmi2/important-things-with-demetri-martin-strategy---property-court", genre="topical")
    content9 = Content(link="http://www.cc.com/video-clips/bz3t0q/comedy-central-presents-rules-committee", genre="topical")
    content10 = Content(link="https://www.youtube.com/watch?v=I0ocSZsFqMk", genre="topical")
    content11 = Content(link="https://www.youtube.com/watch?v=W-EhlYeIiK4", genre="topical")
    content12 = Content(link="https://www.youtube.com/watch?v=KFLensufk4Y", genre="topical")
    content13 = Content(link="https://www.youtube.com/watch?v=zVUjNKCxT8M", genre="topical")
    content14 = Content(link="https://www.youtube.com/watch?v=6gsYBjAscns", genre="topical")
    content15 = Content(link="http://thedailyshow.cc.com/videos/9q977p/democalypse-2012---welcome--twilight--fans--this-is-a-topical-comedy-show-edition", genre="topical")
    content16 = Content(link="https://www.youtube.com/watch?v=z6dfOds64to", genre="topical")
    content17 = Content(link="https://www.youtube.com/watch?v=SqtultQ_BAU", genre="topical")
    content18 = Content(link="https://www.youtube.com/watch?v=naKTsnRdHx8", genre="topical")
    content19 = Content(link="http://thedailyshow.cc.com/videos/qdkcji/bill-o-reilly--president-obama--and-the-super-bowl-pre-show", genre="topical")
    content20 = Content(link="http://www.cc.com/video-clips/nyk52p/comedy-central-presents-getting-online", genre="topical")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def slapstick_content():
    content1 = Content(link="https://www.youtube.com/watch?v=FIGL4eaks20", genre="slapstick")
    content2 = Content(link="https://www.youtube.com/watch?v=sRaF4gk1yhY", genre="slapstick")
    content3 = Content(link="https://www.youtube.com/watch?v=jhaqJXHIXiA", genre="slapstick")
    content4 = Content(link="https://www.youtube.com/watch?v=iRlZaSWocQk", genre="slapstick")
    content5 = Content(link="https://www.youtube.com/watch?v=yxPrxl2K-jY", genre="slapstick")
    content6 = Content(link="https://www.youtube.com/watch?v=OgSNpbVDlCE", genre="slapstick")
    content7 = Content(link="https://www.youtube.com/watch?v=T3qrs5jNT00", genre="slapstick")
    content8 = Content(link="https://www.youtube.com/watch?v=khXJqedYRpw", genre="slapstick")
    content9 = Content(link="https://www.youtube.com/watch?v=xlDXQdgx_QU", genre="slapstick")
    content10 = Content(link="http://www.bing.com/videos/search?q=slapstick+comedy&qpvt=slapstick+comedy&FORM=VDRE#view=detail&mid=AE399D8EF5993BDB0BDBAE399D8EF5993BDB0BDB", genre="slapstick")
    content11 = Content(link="https://www.youtube.com/watch?v=7P9EEB9Mr18", genre="slapstick")
    content12 = Content(link="https://www.youtube.com/watch?v=Vp4uwCEUM0E", genre="slapstick")
    content13 = Content(link="http://www.bing.com/videos/search?q=slapstick+comedy+examples&qpvt=Slapstick+Comedy+Examples&FORM=VDRE#view=detail&mid=4375B9BF2D2658F09B284375B9BF2D2658F09B28", genre="slapstick")
    content14 = Content(link="http://www.bing.com/videos/search?q=slapstick+comedy+examples&qpvt=Slapstick+Comedy+Examples&FORM=VDRE#view=detail&mid=4375B9BF2D2658F09B284375B9BF2D2658F09B28", genre="slapstick")
    content15 = Content(link="https://www.youtube.com/watch?v=j5lU52aWTJo", genre="slapstick")
    content16 = Content(link="https://www.youtube.com/watch?v=dAE7uOO_4v4", genre="slapstick")
    content17 = Content(link="https://www.youtube.com/watch?v=mpjEyBKSfJQ", genre="slapstick")
    content18 = Content(link="http://www.bing.com/videos/search?q=slapstick+comedy&qpvt=Slapstick+Comedy&FORM=VDRE#view=detail&mid=644DD44F89271E636F3D644DD44F89271E636F3D", genre="slapstick")
    content19 = Content(link="http://www.bing.com/videos/search?q=Female+Slapstick&Form=VQFRVP#view=detail&mid=91415E35BABC08977C8791415E35BABC08977C87", genre="slapstick")
    content20 = Content(link="http://www.bing.com/videos/search?q=slapstick+comedy&qpvt=Slapstick+Comedy&FORM=VDRE#view=detail&mid=2C570C3E5EEA4E8E7BC32C570C3E5EEA4E8E7BC3", genre="slapstick")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def crass_content():
    content1 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy&qs=n&form=QBVR&pq=crass%20comedy&sc=6-12&sp=-1&sk=#view=detail&mid=D915FA68B2A400920E30D915FA68B2A400920E30", genre="crass")
    content2 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy&qs=n&form=QBVR&pq=crass%20comedy&sc=6-12&sp=-1&sk=#view=detail&mid=6A5CB6E166D57FCDD5836A5CB6E166D57FCDD583", genre="crass")
    content3 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy&qs=n&form=QBVR&pq=crass%20comedy&sc=6-12&sp=-1&sk=#view=detail&mid=B08D2974301A7BB8A19BB08D2974301A7BB8A19B", genre="crass")
    content4 = Content(link="https://www.youtube.com/watch?v=rBRVjFrvlqE", genre="crass")
    content5 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy&qs=n&form=QBVR&pq=crass%20comedy&sc=6-12&sp=-1&sk=#view=detail&mid=5DED3DE614EC1A6AC5225DED3DE614EC1A6AC522", genre="crass")
    content6 = Content(link="http://thedailyshow.cc.com/videos/90t6yy/bernard-goldberg-pt--1", genre="crass")
    content7 = Content(link="https://www.youtube.com/watch?v=VV4TdzfoERo", genre="crass")
    content8 = Content(link="http://www.bing.com/videos/search?q=crass+comedy&FORM=HDRSC3#view=detail&mid=28D56D586C2EE2F5DCCD28D56D586C2EE2F5DCCD", genre="crass")
    content9 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy%20&qs=n&form=QBVR&pq=crass%20comedy%20&sc=2-13&sp=-1&sk=#view=detail&mid=B5FFF0003BF69C1BA214B5FFF0003BF69C1BA214", genre="crass")
    content10 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy%20&qs=n&form=QBVR&pq=crass%20comedy%20&sc=2-13&sp=-1&sk=#view=detail&mid=691299343138C6754C9B691299343138C6754C9B", genre="crass")
    content11 = Content(link="http://www.bing.com/videos/search?q=crass%20comedy%20&qs=n&form=QBVR&pq=crass%20comedy%20&sc=2-13&sp=-1&sk=#view=detail&mid=9717AEA61B311691EB0F9717AEA61B311691EB0F", genre="crass")
    content12 = Content(link="https://www.youtube.com/watch?v=fPZxw-9WH7s", genre="crass")
    content13 = Content(link="https://www.youtube.com/watch?v=3Pf5DIkd0xo", genre="crass")
    content14 = Content(link="https://www.youtube.com/watch?v=b3RYrQSir7k", genre="crass")
    content15 = Content(link="https://www.youtube.com/watch?v=I-SFA5Xs0s8", genre="crass")
    content16 = Content(link="http://www.bing.com/videos/search?q=crass+comedians&qs=SC&sk=&FORM=QBVR&pq=crass%20comedy&sc=5-12&sp=2&qs=SC&sk=#view=detail&mid=3AA0E89708E608A07AB43AA0E89708E608A07AB4", genre="crass")
    content17 = Content(link="http://www.bing.com/videos/search?q=crass+comedians&qs=SC&sk=&FORM=QBVR&pq=crass%20comedy&sc=5-12&sp=2&qs=SC&sk=#view=detail&mid=361F57898566848F6B82361F57898566848F6B82", genre="crass")
    content18 = Content(link="http://www.bing.com/videos/search?q=crass+comedians&qs=SC&sk=&FORM=QBVR&pq=crass%20comedy&sc=5-12&sp=2&qs=SC&sk=#view=detail&mid=A5506151A64B58CC029FA5506151A64B58CC029F", genre="crass")
    content19 = Content(link="https://www.youtube.com/watch?v=GgZYCj39M38", genre="crass")
    content20 = Content(link="https://www.youtube.com/watch?v=sG5Kjsz_Y2E", genre="crass")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def surreal_content():
    content1 = Content(link="http://www.bing.com/videos/search?q=surreal%20comedians&qs=n&form=QBVR&pq=surreal%20comedians&sc=2-17&sp=-1&sk=#view=detail&mid=8E38C278DEA4752CC1E38E38C278DEA4752CC1E3", genre="surreal")
    content2 = Content(link="http://www.cc.com/video-clips/9gz49q/premium-blend-brutally-honest", genre="surreal")
    content3 = Content(link="https://www.youtube.com/watch?v=NbUSjexRJm4", genre="surreal")
    content4 = Content(link="http://www.bing.com/videos/search?q=surreal%20comedians&qs=n&form=QBVR&pq=surreal%20comedians&sc=2-17&sp=-1&sk=#view=detail&mid=CF6711A51779F44665B1CF6711A51779F44665B1", genre="surreal")
    content5 = Content(link="http://www.cc.com/video-clips/hbzpxo/john-oliver-s-new-york-stand-up-show-favorite-movie", genre="surreal")
    content6 = Content(link="http://www.cc.com/episodes/mn10si/mind-of-mencia-the-rich-sheik---ogps-season-2-ep-209", genre="surreal")
    content7 = Content(link="http://www.bing.com/videos/search?q=surreal%20comedians&qs=n&form=QBVR&pq=surreal%20comedians&sc=2-17&sp=-1&sk=#view=detail&mid=E6555E6B074BB875EBE6E6555E6B074BB875EBE6", genre="surreal")
    content8 = Content(link="https://www.youtube.com/watch?v=qGn7xxhhmo8", genre="surreal")
    content9 = Content(link="https://www.youtube.com/watch?v=eoI2jO7MabQ", genre="surreal")
    content10 = Content(link="http://www.bing.com/videos/search?q=surreal%20comedians&qs=n&form=QBVR&pq=surreal%20comedians&sc=2-17&sp=-1&sk=#view=detail&mid=29E188B9D19BF9ACC5E529E188B9D19BF9ACC5E5", genre="surreal")
    content11 = Content(link="http://www.bing.com/videos/search?q=surreal+comedy&FORM=HDRSC3#view=detail&mid=51185F3877D47C75B5C251185F3877D47C75B5C2", genre="surreal")
    content12 = Content(link="https://www.youtube.com/watch?v=wk0Bcp3X0rY", genre="surreal")
    content13 = Content(link="http://www.cc.com/video-clips/5hdkyi/comedy-central-presents-irish-soap", genre="surreal")
    content14 = Content(link="http://www.cc.com/video-clips/xwo5aw/comedy-central-presents-laundromat-submarine", genre="surreal")
    content15 = Content(link="http://www.cc.com/video-clips/v8meld/stand-up-bo-burnham--beauty-in-the-world", genre="surreal")
    content16 = Content(link="https://www.youtube.com/watch?v=hN4Kv5lHmMc", genre="surreal")
    content17 = Content(link="https://www.youtube.com/watch?v=eEwPkCQTIFY", genre="surreal")
    content18 = Content(link="https://www.youtube.com/watch?v=-bMdTmRae6c", genre="surreal")
    content19 = Content(link="https://www.youtube.com/watch?v=dQfyT4H_NPw", genre="surreal")
    content20 = Content(link="https://www.youtube.com/watch?v=tmy0iD3x6Gs", genre="surreal")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,
    content15,content16,content17,content18,content19,content20])
    session.commit()
    
@manager.command
def remove_stuff():
    content1 = session.query(Content).get(95)
    content2 = session.query(Content).get(99)
    content3 = session.query(Content).get(96)
    session.delete(content1)
    session.delete(content2)
    session.delete(content3)
    session.commit()
@manager.command
def change_stuff_dark():
    content1 = session.query(Content).get(68)
    content2 = session.query(Content).get(67)
    content3 = session.query(Content).get(58)
    content4 = session.query(Content).get(59)
    
    content1.genre = "crass"
    content2.genre = "stand_up"
    content3.genre = "crass"
    content4.genre = "stand_up"
    
    session.commit()
@manager.command
def change_stuff():
    content1 = session.query(Content).get(185)
    content2 = session.query(Content).get(173)
    content3 = session.query(Content).get(184)
    content4 = session.query(Content).get(183)
    content5 = session.query(Content).get(90)
    content6 = session.query(Content).get(103)
    content7 = session.query(Content).get(107)
    
    content9 = session.query(Content).get(127)
    content10 = session.query(Content).get(120)
    content11 = session.query(Content).get(157)
    
    content1.genre = "sketch_improv"
    content2.genre = "stand_up"
    content3.genre = "stand_up"
    content4.genre = "stand_up"
    content5.genre = "pardoy"
    content6.genre = "stand_up"
    content7.genre = "sketch_improv"
    
    content9.genre = "crass"
    content10.genre = "dark"
    content11.genre = "crass"
    
    session.commit()

@manager.command
def remove_crap():
    content1 = session.query(Content).get(60)
    content2 = session.query(Content).get(50)
    content3 = session.query(Content).get(178)
    content4 = session.query(Content).get(170)
    content5 = session.query(Content).get(182)
    content6 = session.query(Content).get(172)
    content7 = session.query(Content).get(181)
    content8 = session.query(Content).get(187)
    content9 = session.query(Content).get(174)
    content10 = session.query(Content).get(186)
    content11 = session.query(Content).get(176)
    content12 = session.query(Content).get(175)
    content13 = session.query(Content).get(171)
    content14 = session.query(Content).get(11)
    content15 = session.query(Content).get(12)
    content16 = session.query(Content).get(23)
    content17 = session.query(Content).get(2)
    content18 = session.query(Content).get(92)
    content19 = session.query(Content).get(93)
    
    content21 = session.query(Content).get(106)
    content22 = session.query(Content).get(97)
    content23 = session.query(Content).get(91)
    content24 = session.query(Content).get(108)
    content25 = session.query(Content).get(3)
    content26 = session.query(Content).get(100)
    content27 = session.query(Content).get(124)
    content28 = session.query(Content).get(1)
    content29 = session.query(Content).get(116)
    content30 = session.query(Content).get(114)
    content31 = session.query(Content).get(125)
    content32 = session.query(Content).get(121)
    content33 = session.query(Content).get(112)
    content34= session.query(Content).get(118)
    content35= session.query(Content).get(122)
    content36= session.query(Content).get(8)
    content37= session.query(Content).get(42)
    content38= session.query(Content).get(46)
    content39= session.query(Content).get(159)
    content40 = session.query(Content).get(164)
    content41 = session.query(Content).get(155)
    content42= session.query(Content).get(169)
    content43 = session.query(Content).get(150)
    content44 = session.query(Content).get(6)
    content45= session.query(Content).get(152)
    content46= session.query(Content).get(158)
    content47= session.query(Content).get(167)
    content48= session.query(Content).get(163)
    content49 = session.query(Content).get(153)
    content50= session.query(Content).get(4)
    content51 = session.query(Content).get(89)
    content52 = session.query(Content).get(74)
    content53= session.query(Content).get(82)
    content54 = session.query(Content).get(76)
    content55 = session.query(Content).get(88)
    
    session.delete(content1)
    session.delete(content2)
    session.delete(content3)
    session.delete(content4)
    session.delete(content5)
    session.delete(content6)
    session.delete(content7)
    session.delete(content8)
    session.delete(content9)
    session.delete(content10)
    session.delete(content11)
    session.delete(content12)
    session.delete(content13)
    session.delete(content14)
    session.delete(content15)
    session.delete(content16)
    session.delete(content17)
    session.delete(content18)
    session.delete(content19)
    
    session.delete(content21)
    session.delete(content22)
    session.delete(content23)
    session.delete(content24)
    session.delete(content25)
    session.delete(content26)
    session.delete(content27)
    session.delete(content28)
    session.delete(content29)
    session.delete(content30)
    session.delete(content31)
    session.delete(content32)
    session.delete(content33)
    session.delete(content34)
    session.delete(content35)
    session.delete(content36)
    session.delete(content37)
    session.delete(content38)
    session.delete(content39)
    session.delete(content40)
    session.delete(content41)
    session.delete(content42)
    session.delete(content43)
    session.delete(content44)
    session.delete(content45)
    session.delete(content46)
    session.delete(content47)
    session.delete(content48)
    session.delete(content49)
    session.delete(content50)
    session.delete(content51)
    session.delete(content52)
    session.delete(content53)
    session.delete(content54)
    session.delete(content55)
    
    session.commit()
    
@manager.command
def remove_top_sur():
    
    content1 = session.query(Content).get(5)
    content2 = session.query(Content).get(7)
    content3 = session.query(Content).get(130)
    content4 = session.query(Content).get(131)
    content5 = session.query(Content).get(132)
    content6 = session.query(Content).get(133)
    content7 = session.query(Content).get(134)
    content8 = session.query(Content).get(135)
    content9 = session.query(Content).get(136)
    content10 = session.query(Content).get(137)
    content11 = session.query(Content).get(138)
    content12 = session.query(Content).get(139)
    content13 = session.query(Content).get(140)
    content14 = session.query(Content).get(141)
    content15 = session.query(Content).get(142)
    content16 = session.query(Content).get(143)
    content17 = session.query(Content).get(144)
    content18 = session.query(Content).get(145)
    content19 = session.query(Content).get(146)
    content20 = session.query(Content).get(147)
    content21 = session.query(Content).get(148)
    content22 = session.query(Content).get(149)
    content23 = session.query(Content).get(190)
    content24 = session.query(Content).get(191)
    content25 = session.query(Content).get(192)
    content26 = session.query(Content).get(193)
    content27 = session.query(Content).get(194)
    content28 = session.query(Content).get(195)
    content29 = session.query(Content).get(196)
    content30 = session.query(Content).get(197)
    content31 = session.query(Content).get(198)
    content32 = session.query(Content).get(199)
    content33 = session.query(Content).get(200)
    content34= session.query(Content).get(201)
    content35= session.query(Content).get(202)
    content36= session.query(Content).get(203)
    content37= session.query(Content).get(204)
    content38= session.query(Content).get(205)
    content39= session.query(Content).get(206)
    content40 = session.query(Content).get(207)
    content41 = session.query(Content).get(208)
    content42= session.query(Content).get(209)

    session.delete(content1)
    session.delete(content2)
    session.delete(content3)
    session.delete(content4)
    session.delete(content5)
    session.delete(content6)
    session.delete(content7)
    session.delete(content8)
    session.delete(content9)
    session.delete(content10)
    session.delete(content11)
    session.delete(content12)
    session.delete(content13)
    session.delete(content14)
    session.delete(content15)
    session.delete(content16)
    session.delete(content17)
    session.delete(content18)
    session.delete(content19)
    session.delete(content20)
    session.delete(content21)
    session.delete(content22)
    session.delete(content23)
    session.delete(content24)
    session.delete(content25)
    session.delete(content26)
    session.delete(content27)
    session.delete(content28)
    session.delete(content29)
    session.delete(content30)
    session.delete(content31)
    session.delete(content32)
    session.delete(content33)
    session.delete(content34)
    session.delete(content35)
    session.delete(content36)
    session.delete(content37)
    session.delete(content38)
    session.delete(content39)
    session.delete(content40)
    session.delete(content41)
    
    
    session.commit()
    
    
@manager.command
def add_new_stuff():
    content1 = Content(link="https://www.youtube.com/watch?v=WOIBBE3ObRY", genre="dark",vulgar=1)
    content2 = Content(link="http://www.reddit.com/r/AskReddit/comments/wz4nf/im_feeling_dark_whats_the_most_morbid_joke_you/", genre="dark",vulgar=1)
    content3 = Content(link="http://thoughtcatalog.com/christine-stockton/2013/11/23-funny-but-depressing-jokes/", genre="dark",vulgar=1)
    content4 = Content(link="http://www.reddit.com/r/MeanJokes/comments/1olbs6/best_dead_baby_jokes/", genre="dark",vulgar=1)
    content5 = Content(link="https://www.youtube.com/watch?v=Q2daFOY9e4Q", genre="crass",vulgar=1)
    content6 = Content(link="https://www.youtube.com/watch?v=srtES-HebG0", genre="crass",vulgar=1)
    content7 = Content(link="https://www.youtube.com/watch?v=Q7FtYv7-aTk", genre="crass",vulgar=1)
    content8 = Content(link="https://www.youtube.com/watch?v=48XreePDi8k", genre="crass",vulgar=1)
    content9 = Content(link="https://www.youtube.com/watch?v=0WQw9hO9Qlg", genre="crass",vulgar=1)
    content10 = Content(link="https://www.youtube.com/watch?v=-XMGP43_cZw", genre="crass",vulgar=1)
    content11 = Content(link="https://www.youtube.com/watch?v=eSfoF6MhgLA", genre="crass",vulgar=1)
    content12 = Content(link="https://www.youtube.com/watch?v=f3PJF0YE-x4", genre="crass",vulgar=1)
    content13 = Content(link="https://www.youtube.com/watch?v=4I7kpCJ_ScU", genre="crass",vulgar=1)
    content14 = Content(link="https://www.youtube.com/watch?v=pcnFbCCgTo4", genre="crass",vulgar=1)
    content15 = Content(link="https://www.youtube.com/watch?v=0jiR_uUw2p8", genre="crass",vulgar=1)
    content16 = Content(link="https://www.youtube.com/watch?v=2sKJ8K-vLgU", genre="crass",vulgar=1)
    content17 = Content(link="https://www.youtube.com/watch?v=YRWen6392yA", genre="crass",vulgar=1)
    content18 = Content(link="http://www.theonion.com/articles/fraternity-members-to-undergo-racial-sensitivity-h,38196/", genre="satire")
    content19 = Content(link="http://www.clickhole.com/video/breathtaking-footage-people-googling-great-family--2097", genre="satire")
    content20 = Content(link="http://southpark.cc.com/clips/44wh2k/seeing-through-the-charade#source=473fef35-48a7-434c-afc6-207874c7f1a3:795ff1e1-03ad-4e07-a5cf-284a02d45aa5&position=2&sort=playlist", genre="satire", vulgar=1)
    content21 = Content(link="https://www.youtube.com/watch?v=9JKvJaJKPPk", genre="satire")
    content22 = Content(link="https://www.youtube.com/watch?v=jOjfxEejS2Y", genre="satire")
    content23 = Content(link="https://www.youtube.com/watch?v=U0kJHQpvgB8", genre="satire", vulgar=1)
    content24= Content(link="https://www.youtube.com/watch?v=XPpsI8mWKmg", genre="satire", vulgar=1)
    content25 = Content(link="https://www.youtube.com/watch?v=2X93u3anTco", genre="satire")
    content26 = Content(link="https://www.youtube.com/watch?v=SluBPO4SCBw", genre="satire")
    content27 = Content(link="https://www.youtube.com/watch?v=63UNmod8zf0", genre="satire")
    content28 = Content(link="https://www.youtube.com/watch?v=ZUnAbwaDYr0", genre="satire",vulgar=1)
    content29 = Content(link="http://www.theonion.com/article/museum-repressed-american-history-conceals-new-exh-50367", genre="satire")
    content30 = Content(link="https://www.youtube.com/watch?v=vLfghLQE3F4", genre="satire")
    content31 = Content(link="https://www.youtube.com/watch?v=CyCj9dmi5n8", genre="dry")
    content32 = Content(link="https://www.youtube.com/watch?v=AZ3v7V2CZu8", genre="dry")
    content33 = Content(link="https://www.youtube.com/watch?v=SrLZgP-OR6s", genre="dry")
    content34 = Content(link="https://www.youtube.com/watch?v=t6WKWsUBkaw", genre="dry")
    content35 = Content(link="https://www.youtube.com/watch?v=AAuDFU2IZlA", genre="dry")
    content36 = Content(link="https://www.youtube.com/watch?v=UKuS1BxVaSk", genre="dry")
    content37 = Content(link="https://www.youtube.com/watch?v=2hBRJ3sfGv4", genre="dry", vulgar=1)
    content38 = Content(link="https://www.youtube.com/watch?v=kAG39jKi0lI", genre="dry")
    content39 = Content(link="https://www.youtube.com/watch?v=_1HYUyhujl4", genre="dry")
    content40 = Content(link="https://www.youtube.com/watch?v=NObe6bMN9AM", genre="dry")
    content41 = Content(link="https://www.youtube.com/watch?v=6cN-FNzTbLY", genre="dry")
    content42 = Content(link="https://www.youtube.com/watch?v=i6HvS0pOoJc", genre="dry")
    content43 = Content(link="https://www.youtube.com/watch?v=35YHvoNXxAA", genre="sketch_improv", vulgar=1)
    content44 = Content(link="https://www.youtube.com/watch?v=3_3VrHLuqG4", genre="slapstick", vulgar=1)
    content45 = Content(link="https://www.youtube.com/watch?v=0XOzPjsD_ec", genre="slapstick", vulgar=1)
    content46 = Content(link="https://www.youtube.com/watch?v=cWn9INKTiq8", genre="slapstick", vulgar=1)
    content47 = Content(link="https://www.youtube.com/watch?v=etLE3ALWZaM", genre="slapstick")
    content48 = Content(link="https://www.youtube.com/watch?v=6hs_m46toTc", genre="slapstick")
    content49 = Content(link="https://www.youtube.com/watch?v=dKmN2e9UXOY", genre="slapstick")
    content50 = Content(link="https://www.youtube.com/watch?v=J7L9THry9QM", genre="slapstick",vulgar=1)
    content51 = Content(link="https://www.youtube.com/watch?v=uMn9gvTgMFg", genre="slapstick")
    content52 = Content(link="https://www.youtube.com/watch?v=S2XvxDaIwCw", genre="slapstick")
    content53 = Content(link="https://www.youtube.com/watch?v=bSdm_eA1Css", genre="slapstick")
    content54 = Content(link="https://www.youtube.com/watch?v=7BwxSHs9elk", genre="slapstick")
    content55 = Content(link="https://www.youtube.com/watch?v=u7tXpBrpecA", genre="slapstick", vulgar=1)
    content56 = Content(link="https://www.youtube.com/watch?v=p2MMGKc-HJo", genre="pardoy")
    content57 = Content(link="https://www.youtube.com/watch?v=0gugBiEkLwU", genre="pardoy", vulgar=1)
    content58 = Content(link="https://www.youtube.com/watch?v=z3eN9u5N2Q4", genre="pardoy",vulgar=1)
    content59 = Content(link="https://www.youtube.com/watch?v=aQ27iS1mkuo", genre="pardoy")
    
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9,content10,content11,content12,content13,content14,  content15,content16,content17,content18,content19,content20,content21,content22,content23,content24,content25,content26,content27,content28,content29,content30,content31,content32,content33,content34, content35,content36,content37,content38,content39,content40,content41,content42,content43,content44,content45,content46,content47,content48,content49,content50,content51,content52,content53,content54,content55,content56,content57,content58,content59])
    session.commit()

@manager.command
def un_bing():
    content1 = session.query(Content).get(179)
    content2 = session.query(Content).get(180)
    
    content4 = session.query(Content).get(98)
    content5 = session.query(Content).get(162)
    content6 = session.query(Content).get(168)
    
    session.delete(content1)
    session.delete(content2)
    
    session.delete(content4)
    session.delete(content5)
    session.delete(content6)
    
    
    session.commit()
@manager.command
def delete_users():
    scores1 = session.query(Scores).get(1)
    scores2 = session.query(Scores).get(2)
    scores3 = session.query(Scores).get(4)
    user1 = session.query(User).get(1)
    user2 = session.query(User).get(2)
    user3 = session.query(User).get(3)
    user4 = session.query(User).get(4)
    session.delete(scores1)
    session.delete(scores2)
    session.delete(scores3)
    session.delete(user1)
    session.delete(user2)
    session.delete(user3)
    session.delete(user4)
    
    session.commit()
    
@manager.command
def delete_last():
    content1 = session.query(Content).get(213)
    content2 = session.query(Content).get(211)
    content3 = session.query(Content).get(177)
    content4 = session.query(Content).get(99)
    content5 = session.query(Content).get(95)
    content6 = session.query(Content).get(111)
    content7 = session.query(Content).get(102)
    content8 = session.query(Content).get(188)
    content9 = session.query(Content).get(244)
    content10 = session.query(Content).get(117)
    content11 = session.query(Content).get(129)
    content12 = session.query(Content).get(128)
    content13 = session.query(Content).get(185)
    content14 = session.query(Content).get(253)
    content15 = session.query(Content).get(156)
    content16 = session.query(Content).get(77)
    content17 = session.query(Content).get(84)
    
    session.delete(content1)
    session.delete(content2)
    session.delete(content3)
    session.delete(content4)
    session.delete(content5)
    session.delete(content6)
    session.delete(content7)
    session.delete(content8)
    session.delete(content9)
    session.delete(content10)
    session.delete(content11)
    session.delete(content12)
    session.delete(content13)
    session.delete(content14)
    session.delete(content15)
    session.delete(content16)
    session.delete(content17)
    
    session.commit()
@manager.command
def add_last():
    content1 = Content(link="http://www.skrause.org/humor/deadbaby.shtml", genre="dark",vulgar=1)
    content2 = Content(link="http://imgur.com/gallery/WnyFQ", genre="dark", vulgar=1)
    content3 = Content(link="https://www.youtube.com/watch?v=zVDKYBNceeQ", genre="dark",vulgar=1)
    content4 = Content(link="https://www.youtube.com/watch?v=xhNneU5shTs", genre="crass", vulgar=1)
    content5 = Content(link="https://www.youtube.com/watch?v=kIQbTJRKDpc", genre="slapstick", vulgar=1)
    content6 = Content(link="https://www.youtube.com/watch?v=oRKbez1LpWU", genre="slapstick", vulgar=1)
    content7 = Content(link="https://www.youtube.com/watch?v=6Dye05tvSoo", genre="slapstick", vulgar=1)
    content8 = Content(link="https://www.youtube.com/watch?v=bOR38552MJA", genre="satire")
    content9 = Content(link="http://www.nbc.com/saturday-night-live/video/couric--palin-open/n12311", genre="pardoy")
    content10 = Content(link="https://screen.yahoo.com/nprs-delicious-dish-schweddy-balls-000000088.html", genre="pardoy", vulgar=1)
    content11 = Content(link="https://www.youtube.com/watch?v=rxUm-2x-2dM", genre="dry")
    content12 = Content(link="https://www.youtube.com/watch?v=TIIAQME1Uhg", genre="dry")
    content13 = Content(link="https://www.youtube.com/watch?v=faMh6OYfuNE", genre="dry")
    
    
    session.add_all([content1, content2, content3, content4, content5, content6, content7, content8, content9, content10, content11, content12, content13])
    session.commit()
@manager.command
def yes():    
    content1 = session.query(Content).get(278)
    session.delete(content1)
    session.commit()
from flask.ext.migrate import Migrate, MigrateCommand
from smileful.database import Base

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
     manager.run()