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
    with app.app_context():
        with mail.connect() as conn:
            for i in email_list:
                dropbox_url = "https://db.tt/wW7clVpS"
                html = render_template("dropbox/dropbox_signup.html", dropbox_url=dropbox_url)
                subject = "Free cloud storage"
                send_email(i.email, subject, html)

def gen_list():
    return list(range(5000,50000,1000))
        

if __name__ == "__main__":
    print "###########################################"
    offset_list = gen_list()
    for i in offset_list:
        print "number in list ", i
        import time
        start = time.time()
        send_bulk(i)
        end = time.time()
        tt = (end-start)
        print "it took ", tt, " in seconds " , tt/60, "in minutes"
        print "all sent"
        time.sleep(2)
        print "###########################################"
