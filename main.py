from flask import Flask, render_template, request, jsonify, redirect, url_for
from parser import take_setings
from api import take_users
app = Flask(__name__)

@app.route('/')
def first():
  return render_template("index.html")

@app.route('/page')
def load():
  data = {'a': 0}
  return render_template("page.html", data=data)

@app.get('/api')
def get_api():
  return take_users()

@app.post('/api')
def post_api():
  return{'a': 0}

if __name__ == '__main__':
  app.run(debug=True)
