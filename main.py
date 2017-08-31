from flask import Flask, redirect, url_for, render_template, request, session
from user_data import *
from user import *

app = Flask(__name__)

app.secret_key = 'fjdksalfhup3502rt/5342afdsa'


@app.route('/')
def index():
    user = session.get('username')
    admin = user == 'admin'
    return render_template('index.html', user=user, admin=admin)


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


@app.route('/delete/<string:username>', methods=['GET', 'POST'])
def delete(username):
    user = session.get('username')
    admin = user == 'admin'
    if username != 'admin' and admin:
        delete_user(username)
        return redirect(url_for('admin'))
    else:
        if user == username:
            session.pop('username')
            delete_user(username)
            return redirect(url_for('index'))
        return redirect(url_for('settings', username=user))


@app.route('/settings/<string:username>', methods=['GET', 'POST'])
def settings(username):
    user = session.get('username')
    if user != username:
        return redirect(url_for('settings', username=user))
    return render_template('settings.html', user=user)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    user = session.get('username')
    admin = user == 'admin'
    if admin:
        users = get_all_users(user)
        print(users)
        return render_template('admin.html', users=users)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
