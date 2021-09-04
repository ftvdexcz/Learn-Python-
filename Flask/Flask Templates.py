from flask import Flask, redirect, url_for, render_template

app =  Flask(__name__)

@app.route('/')
def index():
    return 'Hello! This is tutorial flask python'

@app.route('/welcome/<name>')
def welcome_user(name):
    return render_template('welcome_user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)