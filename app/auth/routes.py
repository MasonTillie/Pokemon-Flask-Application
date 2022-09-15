from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserSignUp, UserLogin


from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__, template_folder='authtemplates')
from app.models import db

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = UserSignUp()
    if request.method == 'POST':
        print('Post request has been made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data     
            print(username, email, password)

            user = User(username, email, password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print('validation failed')
    else:
        print('GET request made')
    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLogin()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        print(user.username, user.password)
        if user:
            if user.password == password:
                login_user(user)
            else:
                print('Incorrect Password! Try Again')
        else:
            pass
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))