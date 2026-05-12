from flask import Flask
from parser import take_setings
app = Flask(__name__)

@app.route('/')
def hello_world():
  return take_setings()

if __name__ == '__main__':
  app.run(debug=True)
