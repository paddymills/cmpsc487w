
from . import lm
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, logout_user, login_user
from .models import User

auth = Blueprint('auth', __name__)

@lm.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()

@auth.get('/login')
def login_page():
    return render_template("login.html")

@auth.post('/login')
def login_post():
    name = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()
    if not user or user.password != password:
        return render_template("login.html", msg="Invalid login")

    login_user(user)

    return redirect(request.args.get('next') or url_for('main.index'))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
