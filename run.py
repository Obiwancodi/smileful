import os
from flask.ext.script import Manager
from smileful import app


from werkzeug.security import generate_password_hash
from smileful.models import User

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
    

from flask.ext.migrate import Migrate, MigrateCommand
from smileful.database import Base

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
     manager.run()