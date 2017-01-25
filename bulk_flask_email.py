
from app import app,db,mail
from flask import render_template, flash, request, redirect, url_for
from app.models import Export 
from flask_mail import Message

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='"Cloud Storage" <email@asciichan-tripplannr.com>'
    )
    mail.send(msg)

# users = ["jeffreiher@gmail.com", "jeffreiher@bulletmail.org", "jreiher2003@yahoo.com"]
def send_bulk(offset):
    email_list = db.session.query(Export).offset(offset).limit(1000)
    # email_list_50k = db.session.query(Export).offset(50001).limit(50000)
    # email_list_50_100k = db.session.query(Export).offset(100001).limit(50000)
    # email_list_100_150k = db.session.query(Export).offset(150001)
    # email_list_180_188k = db.session.query(Export).offset(180501).limit(5000)
    with app.app_context():
        with mail.connect() as conn:
            for i in email_list:
                dropbox_url = "https://db.tt/wW7clVpS"
                html = render_template("dropbox/dropbox_signup.html", dropbox_url=dropbox_url)
                subject = "Free cloud storage"
                send_email(i.email, subject, html)
        

if __name__ == "__main__":
    print "###########################################"
    import time
    start = time.time()
    send_bulk(0)
    end = time.time()
    time = (end-start)
    print "it took ", time, " in seconds " , time/60, "in minutes"
    print "all sent"
    print "###########################################"

    # test_query()