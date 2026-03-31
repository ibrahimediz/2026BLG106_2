from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'İbrahim'}
    posts = [
        {'author': {'username': 'Ahmet'}, 'body': 'İstanbul bugün harika bir havaya sahip!'},
        {'author': {'username': 'Ayşe'}, 'body': 'Flask ile web geliştirmek çok eğlenceli!'}
    ]
    return render_template('index.html', title='Ana Sayfa', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} için giriş isteği gönderildi, beni hatırla={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Giriş Yap', form=form)
