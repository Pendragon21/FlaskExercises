from flask import Flask, make_response, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index02.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'

app.run(host='0.0.0.0', port=81, debug=True)