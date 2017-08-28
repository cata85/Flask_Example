from flask import Flask, redirect, url_for, render_template, request, session
from user_data import *
from user import *

app = Flask(__name__)

app.secret_key = 'fjdksalfhup3502rt/5342afdsa'


@app.route('/')
def index():
    return render_template('index.html', user=session.get('username'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username_text']
        password = request.form['password_text']
        if check_login(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Incorrect username or password')
    else:
        return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username_text']
        password_one = request.form['password_one']
        password_two = request.form['password_two']
        if check_username_aval(username) and compare_pass(password_one, password_two):
            create_user(username, password_one)
            session['username'] = username
            return redirect(url_for('index'))
        elif not check_username_aval(username):
            return render_template('signup.html', error='Username not available')
        else:
            return render_template('signup.html', error='Passwords do not match')
    else:
        return render_template('signup.html')


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username')
    return redirect(url_for('index'))


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
