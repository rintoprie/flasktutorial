from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    html = '<h1>Hello, World!</h1>'
    html += '<h2>OK</h2>'
    return html

@app.route('/azka')
def azka():
    user = "Azka"
    return render_template('azka.html',name = user)

@app.route('/daftar')
def daftar():
    daftar = ['Satu','Dua','Tiga']
    return render_template('daftar.html',lst = daftar)

