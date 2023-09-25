#!/usr/bin/python3
""" 2. C route """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Task 0 """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Task 1 """
    return 'HBNB'


@app.route('/c/<var>')
def c(var):
    """ Task 2 """
    return 'C {}'.format(var).replace('_', ' ')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
