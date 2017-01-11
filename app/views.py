from app import app
from flask import render_template, flash, request, redirect, url_for
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