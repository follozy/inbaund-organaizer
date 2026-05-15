from flask import Flask, render_template, request, jsonify, redirect, url_for
from parser import take_setings
from api import take_users, take_fild
app = Flask(__name__)

@app.route('/')
def first():
  return render_template("index.html")

@app.route('/page')
def load():
  
  
  if request.args.get('page') == 'main':
    data = {'type': 'main'}
    return render_template("page.html", data=data)
  elif request.args.get('page') == 'add_server':
    data = {'type': 'add_server'}
    return render_template('page.html', data=data)
  else:
    return 'заглушка'

@app.get('/api')
def get_api():
  if request.args.get('type') == 'users':
    return take_users()
  elif request.args.get('type') == 'tables':
    return take_fild(request.args.get('name'))

    


@app.post('/api')
def post_api():
  return{'a': 0}

if __name__ == '__main__':
  app.run(debug=True)
