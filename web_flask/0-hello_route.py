#!/usr/bin/python3
""" 0. Hello Flask! """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Hello world function"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(port=5000)
