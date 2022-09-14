from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserSignUp


from app.models import User 

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
            db.session.commit
            return redirect(url_for('auth.login'))
        else:
            print('validation failed')
    else:
        print('GET request made')
    return render_template('signup.html', form=form)

@auth.route('/login')
def login():
    return render_template('login.html')