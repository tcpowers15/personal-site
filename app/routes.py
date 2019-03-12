from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Trevor'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautifiul day'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'what!?'
        }
    ]

    return render_template('home.html', title='Home',
                           user=user, posts=posts)
