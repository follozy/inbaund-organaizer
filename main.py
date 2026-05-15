from flask import Flask, render_template, request, jsonify, redirect, url_for
from parser import take_setings, set_users
from api import take_users, take_fild, add_sever, take_user_by_id
app = Flask(__name__)

@app.route('/')
def first():
  return render_template("index.html")

@app.route('/page')
def load():
  
  
  if request.args.get('page') == 'users_list':
    data = {'type': 'users_list'}
    return render_template("page.html", data=data)
  elif request.args.get('page') == 'add_server':
    data = {'type': 'add_server'}
    return render_template('page.html', data=data)
  elif request.args.get('page') == 'user':
    data = {'type': 'user'}
    data['id'] = request.args.get('id')
    return render_template('page.html', data=data)
  else:
    return 'заглушка'





@app.get('/api')
def get_api():
  if request.args.get('type') == 'users':
    if request.args.get('action') == 'update':
      return set_users()
    elif request.args.get('action') == 'list':
      return take_users()
    elif request.args.get('action') == 'take_one':
      return take_user_by_id(int(request.args.get('id')))
  elif request.args.get('type') == 'tables':
    return take_fild(request.args.get('name'))

@app.post('/api')
def post_api():
  if request.args.get('type') == 'servers':
    if request.args.get('action') == 'add_server':
      return add_sever(request.form.to_dict())




if __name__ == '__main__':
  app.run(debug=True)
