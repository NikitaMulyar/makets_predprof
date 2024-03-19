import csv
import datetime

from flask import Flask, render_template, redirect, abort, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data import db_session, csv_api
from data.users import User
from data.companies import Company
from data.lands import Land
from data.user_to_company import UserCompany
from form.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
host = '127.0.0.1'
port = '5000'
path = f'http://{host}:{port}'
@app.route('/')
def index():
    return render_template('index.html')