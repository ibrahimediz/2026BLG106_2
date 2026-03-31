from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'İbrahim'}
    posts = [
        {
            'author': {'username': 'Ahmet'},
            'body': 'İstanbul bugün harika bir havaya sahip!'
        },
        {
            'author': {'username': 'Ayşe'},
            'body': 'Flask ile web geliştirmek çok eğlenceli!'
        }
    ]
    return render_template('index.html', title='Ana Sayfa', user=user, posts=posts)
