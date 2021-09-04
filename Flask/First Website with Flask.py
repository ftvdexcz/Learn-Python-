from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello! This is first website with flask</h1>"

# dynamic route
@app.route('/<name>')
def user(name):
    return f'Hello {name}!'

# Sử dụng redirect(url_for('<tên hàm>')) để điều hướng tới trang web khác, ví dụ điều hướng tới trang home
@app.route('/admin')
def admin():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
