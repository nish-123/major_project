from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # This is used to keep the session secure

# Dummy user credentials (replace with your actual user database)
users = {'username': 'password', 'john': 'doe', 'jane': 'doe'}

@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]}<br><a href="/logout">Logout</a>'
    return 'You are not logged in<br><a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Invalid username/password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
