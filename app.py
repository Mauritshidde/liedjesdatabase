from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3, json, collections, sys, os
from forms import ToevoegenForm
#from main import
liedje = "https://www.youtube.com/watch?v=cPJUBQd-PNM"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1ccabe4c9d3d5813ba8881bd1082fef'

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


app.run(host='localhost', port=8080, debug=True)
