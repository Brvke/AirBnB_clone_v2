#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route handler for the root URL"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route handler for the /hbnb URL"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route handler for the /c/<text> URL"""
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """Route handler for the /python/<text> URL"""
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Route handler for the /number/<n> URL"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Route handler for the /6-number_odd_or_even.html/<n> URL"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """Route handler for the /number_odd_or_even/<n> URL"""
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
