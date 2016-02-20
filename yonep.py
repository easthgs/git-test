#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def yo(name=None):
    return render_template('yo.html', name=name)


@app.route('/add', methods=['POST'])
def add():
    return redirect(url_for('yo', name=request.form['name']))


if __name__ == '__main__':
    app.run(debug=True)
