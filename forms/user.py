from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField, \
    SelectMultipleField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    email = EmailField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=5)])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired(), Length(min=5)])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    speciality = StringField('Специальность')
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')