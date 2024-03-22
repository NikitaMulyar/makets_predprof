import csv
import datetime

from flask import Flask, render_template, redirect, abort, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
# login_manager = LoginManager()
# login_manager.init_app(app)
host = '127.0.0.1'
port = '5000'
path = f'http://{host}:{port}'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(port=int(port), host=host)
