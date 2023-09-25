#!/usr/bin/python3
""" Task 11 """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template as render
from bisect import insort

app = Flask(__name__)
app.url_map.strict_slashes = False


all_states = storage.all(State)
all_amenities = storage.all(Amenity)


@app.teardown_appcontext
def teardown(exception=None):
    """ Teardown """
    storage.close()


@app.route('/hbnb_filters')
def hbnb():
    """Task 11 """
    return render('10-hbnb_filters.html', all_states=all_states,
                  all_amenities=all_amenities)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
