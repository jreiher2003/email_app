from app import app,db,mail
from flask import render_template, flash, request, redirect, url_for
from flask_mail import Message
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

@app.route("/send")
def send_email():
    msg = Message("Hello",
                  sender="email@asciichan-tripplannr.com",
                  recipients=["jeffreiher@gmail.com"])
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
            subject = "hello, %s" % user[i]
            msg = Message(recipients=[user[i]],
                          body=message,
                          subject=subject)

            conn.send(msg)
        return "sent"

