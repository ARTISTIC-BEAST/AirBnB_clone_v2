#!/usr/bin/python3
""" 6. Odd or even? """
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
def task8():
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


@app.route('/')
def task0():
    """ Task 0 """
    return 'Hello HBNB!'


@app.route('/hbnb')
def task1():
    """ Task 1 """
    return 'HBNB'


@app.route('/c/<var>')
def task2(var):
    """ Task 2 """
    return 'C {}'.format(var)


@app.route('/python', defaults={'var': 'is cool'})
@app.route('/python/(<var>)')
def task3(var="is cool"):
    """ Task 3 """
    return 'Python {}'.format(var).replace('_', ' ')


@app.route('/number/<int:n>')
def task4(n):
    """ Task 4 """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def task5(n):
    """ Task 5 """
    return render('5-number.html',      number=n)


@app.route('/number_odd_or_even/<int:n>')
def task6(n):
    """ Task 6 """
    if n % 2 is 0:
        return render('6-number_odd_or_even.html', num=n, num_type='even')
    return render('6-number_odd_or_even.html', num=n, num_type='odd')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
