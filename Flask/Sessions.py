from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key= 'mykey'
# Lưu lại phiên người dùng (set thời gian có thể theo ngày, tháng)
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def index():
    return render_template('index.html')

# POST Method: Phương pháp truyền thông tin an toàn (không hiển thị trên URL)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Cho phép lưu lại phiên 
        session.permanent = True
        user = request.form['nm']
        session["user"] = user
        return redirect(url_for('user')) 
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

# GET Method: Truyền thông tin không an toàn (khi đến trang web, các thông tin hiển thị trên URL)
@app.route('/get')
def get_name():
    return render_template('1 Example of get method.html')

@app.route('/report')
def report():
    name = request.args.get('nm')
    return f'<h1>{name}</h1>'

@app.route('/user')
def user():
    # Kiểm tra xem có thông tin trong phiên không, vì người dùng có thể nhập '/usr' để truy cập 
    # Kiểm tra tên của khóa phiên (name) có trong phiên không
    if 'user' in session:
        user = session['user']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)