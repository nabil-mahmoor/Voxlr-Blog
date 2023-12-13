from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '26a76a089b9266365155fa79cf124b38bb614058e80fb13e07668234ba770e43'


posts = [
    {
        'author': 'Zack Lenon',
        'title': 'Blog Post 01',
        'content': 'First post',
        'date_created': 'April 20, 2018'
    },
    {
        'author': 'Kate Jeene',
        'title': 'Blog Post 02',
        'content': 'Second post',
        'date_created': 'May 17, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ffff@blog.com' and form.password.data == 'ffff': 
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)