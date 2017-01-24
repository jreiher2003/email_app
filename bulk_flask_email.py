
from app import app,db,mail
from flask import render_template, flash, request, redirect, url_for
from app.models import Export 
from flask_mail import Message

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

users = ["jeffreiher@gmail.com", "jeffreiher@bulletmail.org", "jreiher2003@yahoo.com"]
def send_bulk():
    email_list = db.session.query(Export).limit(50000)
    email_list_50k = db.session.query(Export).offset(50001).limit(50000)
    email_list_50_100k = db.session.query(Export).offset(100001).limit(50000)
    email_list_100_150k = db.session.query(Export).offset(150001)
    with app.app_context():
        with mail.connect() as conn:
            for i in email_list:
                dropbox_url = "https://db.tt/wW7clVpS"
                html = render_template("dropbox/dropbox_signup.html", dropbox_url=dropbox_url)
                subject = "Free cloud storage"
                send_email(i.email, subject, html)

def test_query():
    email_list = db.session.query(Export).limit(50000)
    email_list_50k = db.session.query(Export).offset(50001).limit(50000)
    email_list_50_100k = db.session.query(Export).offset(100001).limit(50000)
    email_list_100_150k = db.session.query(Export).offset(150001)
    for i in email_list_50k:
        print i.email
        

if __name__ == "__main__":
    print "###########################################"
    import time
    start = time.time()
    time.sleep(60)
    send_bulk()
    end = time.time()
    time = (end-start)
    print "it took ", time, " in seconds " , time/60, "in minutes"
    print "all sent"
    print "###########################################"

    # test_query()