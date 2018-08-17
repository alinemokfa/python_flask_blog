from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Aline M',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '16 Aug 2018'
    },
    {
        'author': 'Patrick C',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '17 Aug 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
