from app import app,db,mail
from flask import render_template, flash, request, redirect, url_for
from flask_mail import Message

users = ["jeffreiher@gmail.com", "jeffreiher@bulletmail.org", "jreiher2003@yahoo.com"]
with mail.connect() as conn:
    for i in range(len(users)):
        message = 'this is test message'
        subject = "hello, %s" % user[i]
        msg = Message(recipients=[user[i]],
                      body=message,
                      subject=subject)

        conn.send(msg)