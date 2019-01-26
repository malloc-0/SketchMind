#!/usr/bin/env python

# Import flask module
from flask import Flask

# Initialize
app = Flask(__name__)

# decorate the index


@app.route('/index')
def index():
    return "This is the index page"


@app.route('/main')
def main():
    return "This is the main page"


@app.route('/request', methods=['POST'])
def request():
    if request.method == 'POST':
        return "Uhhhh, we've got a picture. Working on it."


if __name__ == '__main__':
    app.run()
