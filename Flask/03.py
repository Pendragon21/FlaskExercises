from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/dashboard/<name>')
def dashboard(name):
   return f"<h1>Welcome {name}!</h1>"

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=81, debug=True)