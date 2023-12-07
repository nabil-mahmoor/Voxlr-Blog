from flask import Flask, render_template, url_for


app = Flask(__name__)


posts = [
    {
        'author': 'Vanell Blunt',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 16, 2020'
    },
    {
        'author': 'Zack Beer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 29, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('home.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)