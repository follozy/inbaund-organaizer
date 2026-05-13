from flask import Flask, render_template, request, jsonify, redirect, url_for
from parser import take_setings
from api import take_users
app = Flask(__name__)

@app.route('/')
def first():
  return render_template("index.html")

@app.route('/api')
def api():
  return take_users()


if __name__ == '__main__':
  app.run(debug=True)
