from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    users = [ 'Rafael','Marcelo','Alex' ]
    return render_template('index.html', title='Welcome', members=users)



app.run(host='0.0.0.0', port=81, debug=True)