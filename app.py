from flask import Flask, render_template, request, redirect, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3 as sql
import os
from flask_cors import CORS


app = Flask(__name__, static_folder='static')

# Ensure templates are auto-reloaded
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure session to use filesystem (instead of signed cookies)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Protect Security
CORS(app)

@app.route('/', methods=['GET'])
def index():
    '''Displays Homepage and create posts'''
    return render_template('index.html')


@app.route('/education', methods=['GET'])
def education():
    '''Display education page'''
    return render_template('education.html')


@app.route('/hobbies', methods=['GET'])
def hobbies():
    '''Display hobbies page'''
    return render_template('hobbies.html')


@app.route('/contact', methods=['GET'])
def contact():
    '''Display contact info page'''
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
