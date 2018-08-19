from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

posts = [
    {
        'author': 'Aline',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '19 Aug 2018'
    },
    {
        'author': 'Patrick',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '19 Aug 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #TODO Seeding to be deleted once db is up
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You are now logged in!', 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
