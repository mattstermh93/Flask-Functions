from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user=user, title='Home Page')

@app.route('/posts')
def posts():
    posts = [
        'This is post #1.',
        'This is post #2.',
        'We\'re looping through these posts.',
        'This is Flask!!!!'
    ]
    return render_template('posts.html', title='Posts', posts=posts)

@app.route('/redirect')
def goaway():
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Thank you for logging in {}!'.format(login_form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        flash('Thank you for registering! {}!'.format(register_form.username.data))
        return redirect(url_for('index'))
    return render_template('register.html', form=register_form)


# app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm(request.form)
#     if request.method == 'POST' and form.validate():
#         user = User(form.username.data, form.email.data,
#                     form.password.data)
#         flash('Thank you for logging in {}!'.format(login_form.username.data))
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     register_form = LoginForm()
#     if register_form.validate_on_submit():
#         flash('Thank you for registering! {}!'.format(register_form.username.data))
#         return redirect(url_for('index'))
#     return render_template('register.html', form=register_form)
