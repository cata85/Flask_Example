from flask import Flask, redirect, url_for, render_template, request, session

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
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


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
    app.run(debug=True)
