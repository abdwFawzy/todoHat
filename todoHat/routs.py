from flask import redirect, render_template, request,url_for
from todoHat.forms import registerform, loginform
from todoHat.models import User, Task, doin_task
from todoHat import app
from werkzeug.security import check_password_hash, generate_password_hash
from .helpers import apology
import os

# starting
@app.route('/', methods=['GET', 'POST'])
def home():
    return apology("TODO: Home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginform()
    return render_template("login.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "Post":
        return redirect(url_for('home'))
    form = registerform()
    return render_template("register.html", form=form)        
