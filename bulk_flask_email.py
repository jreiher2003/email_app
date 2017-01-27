from app import app,db,mail
from flask import render_template, flash, request, redirect, url_for
from app.models import Export 
from flask_mail import Message

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='"Dreams Casino" <email@asciichan-tripplannr.com>'
    )
    mail.send(msg)

# emails = ["jeffreiher@gmail.com", "jeffreiher@bulletmail.org", "jreiher2003@yahoo.com"]
def send_bulk(offset):
    email_list = db.session.query(Export).offset(offset).limit(100)
    emails = [e.email for e in email_list]
    print emails 
    print len(emails)
    with app.app_context():
        with mail.connect() as conn:
            for i in emails:
                
                html = render_template("gwages/dreams/dreams_catch_star.html", email=i)
                subject = "Play Casino Games Free Play $25"
                send_email(i, subject, html)

def gen_list():
    """ this will give you the offset variable in send bulk and step by 1000 
    email_list = db.session.query(Export).offset(46000).limit(1000)

    """
    return list(range(10700,320300,100))
        

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
