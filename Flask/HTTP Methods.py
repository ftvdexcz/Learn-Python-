from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# POST Method: Phương pháp truyền thông tin an toàn (không hiển thị trên URL)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['nm']
        return redirect(url_for('user', usr=name)) 
    else:
        return render_template('login.html')

# GET Method: Truyền thông tin không an toàn (khi đến trang web, các thông tin hiển thị trên URL)
@app.route('/get')
def get_name():
    return render_template('1 Example of get method.html')

@app.route('/report')
def report():
    name = request.args.get('nm')
    return f'<h1>{name}</h1>'

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'

if __name__ == '__main__':
    app.run(debug=True)