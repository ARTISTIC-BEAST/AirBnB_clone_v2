#!/usr/bin/python3
""" 9. Cities by states """
from flask import Flask, render_template as render
from models import storage
from models.state import State
from models.city import City
from bisect import insort

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception=None):
    """ Teardown """
    storage.close()


@app.route('/states_list')
def states_list():
    states = ""
    state_list = []
    all_states = storage.all(State)
    for state in all_states.values():
        insort(state_list, "{},{}".format(state.name, state.id))
    for i in state_list:
        _id = i.split(',')[1]
        _name = i.split(',')[0]
        states += '\n\t<li>{}: <b>{}</b></li>\n'.format(_id, _name)
    return render('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """ Cities by state """
    cities = ""
    city_list = []
    all_states = storage.all(State)
    # Create a sorted list of states
    for state in all_states.values():
        if len(state.cities) is 0:
            insort(city_list, "{},{},{},{}".format(
                state.name, "", "", state.id))
        else:
            for city in state.cities:
                insort(city_list, "{},{},{},{}".format(
                    state.name, city.name, city.id, state.id))

    state_id = ""
    for i in city_list:
        if state_id != i.split(',')[3]:
            state_id = i.split(',')[3]
            state_name = i.split(',')[0]
            city_id = i.split(',')[2]
            city_name = i.split(',')[1]
            if city_list.index(i) is not 0:
                cities += "\n\t\t</ul>\n\t</li>"
            cities += '\n\t<li>{}: <b>{}</b>\n\t\t<ul>'.format(
                state_id, state_name)
            if city_id != "":
                cities += '\n\t\t\t<li>{}: <b>{}</b></li>\n'.format(
                    city_id, city_name)
        else:
            city_id = i.split(',')[2]
            city_name = i.split(',')[1]
            if city_id != "":
                cities += '\n\t\t\t<li>{}: <b>{}</b></li>\n'.format(
                    city_id, city_name)
    cities += "\n\t\t</ul>\n\t</li>"
    return render('8-cities_by_states.html', cities=cities)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
