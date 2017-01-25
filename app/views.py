from app import app,db,mail
from flask import render_template, flash, request, redirect, url_for
from flask_mail import Message
from models import Export
from forms import EmailForm

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        print email 
        flash("Unsubscribe Successfull >> %s" % email, "success")
        return redirect(url_for("success"))
    return render_template("index.html", form=form, error=error)

@app.route("/success")
def success():
    form = EmailForm()
    return render_template("success.html", form=form)

######################################################################
######################################################################

@app.route("/send")
def send_email():
    msg = Message("Hello", recipients=["jeffreiher@gmail.com"])
                  # sender="email@asciichan-tripplannr.com",
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
    return "sent"

@app.route("/send_bulk")
def send_bulk():
    users = ["jeffreiher@gmail.com", "jeffreiher@bulletmail.org", "jreiher2003@yahoo.com"]
    with mail.connect() as conn:
        for i in range(len(users)):
            message = 'this is test message'
            subject = "hello, %s" % users[i]
            sender='"Cloud Storage" <email@asciichan-tripplannr.com>'
            msg = Message(recipients=[users[i]],
                          body=message,
                          subject=subject,
                          sender=sender)
            conn.send(msg)
        return "sent"

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='"Cloud Storage" <email@asciichan-tripplannr.com>'
    )
    mail.send(msg)

def dropbox_example():
    # user = db.query()
    users = ["jeffreiher@gmail.com", "jeffreiher@bulletmail.org", "jreiher2003@yahoo.com"]
    with mail.connect() as conn:
        for i in range(len(users)):
            dropbox_url = "https://db.tt/wW7clVpS"
            html = render_template("dropbox/dropbox_signup.html", dropbox_url=dropbox_url)
            subject = "Free cloud storage"
            send_email(users[i], subject, html)

@app.route("/test_tem")
def test_tem():
    dropbox_example()
    return "send"

@app.route("/email_temp")
def email_temp():
    return render_template("dropbox/dropbox_signup.html")

###############################################################
###############################################################

# def dropbox_send():
#     email_list1 = Export.query.all()
#     email_list = list(email_list1)
#     with mail.connect() as conn:
#         for e in email_list:
#             # print e.email
#             dropbox_url = "https://db.tt/wW7clVpS"
#             html = render_template("dropbox/dropbox_signup.html", dropbox_url=dropbox_url)
#             subject = "Free cloud storage"
#             send_email(e.email, subject, html)

# @app.route("/ascii-send")
# def drobox_sending_live():
#     dropbox_send()
#     return "send"



