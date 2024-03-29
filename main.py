from flask import Flask, render_template, redirect, abort, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.user import RegisterForm, LoginForm
from forms.add_point import Point
from forms.add_route import Route
from data import db_session
from data.users import User
from map_parser import create_map
from edit_detector import edit_detector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
host = '127.0.0.1'
port = '5000'
path = f'http://{host}:{port}'
res = (None, None)


# ГЛАВНАЯ СТРАНИЦА
@app.route('/', methods=['GET', 'POST'])
def index():
    global res
    form = Route()
    t = (res[0], res[1])
    res = (None, None)
    if form.validate_on_submit():
        coor_a = form.coor_ax.data, form.coor_ay.data
        coor_b = form.coor_bx.data, form.coor_by.data
        create_map(coor_a, coor_b)
        return render_template('index.html', form=form, res=t[1])
    return render_template('index.html', form=form, res=t[1])


# ТУТ БУДЕТ ЛИЧНАЯ СТРАНИЧКА ПОЛЬЗОВАТЕЛЯ
@app.route('/user')
def user():
    return render_template('user.html')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# ЛОГИНИМСЯ
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


# РЕГИСТРАЦИЯ
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            login=form.login.data,
            surname=form.surname.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# ВЫХОДИМ ИЗ АККА
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add', methods=['GET', 'POST'])
def add():
    global res
    form = Point()
    if form.validate_on_submit():
        id_point = form.id_point.data
        coors = form.coor_x.data, form.coor_y.data
        anomalia_1 = form.anomalia_id_1.data, form.anomali_rate_1.data
        anomalia_2 = form.anomalia_id_2.data, form.anomali_rate_2.data
        anomalia_3 = form.anomalia_id_3.data, form.anomali_rate_3.data
        anomalia_4 = form.anomalia_id_4.data, form.anomali_rate_4.data
        anomalia_5 = form.anomalia_id_5.data, form.anomali_rate_5.data
        anomalia_6 = form.anomalia_id_6.data, form.anomali_rate_6.data
        res = edit_detector(id_point, coors, anomalia_1, anomalia_2, anomalia_3, anomalia_4, anomalia_5, anomalia_6)
        return redirect('/')
    return render_template('add.html', title='Изменить данные', form=form)


@app.route('/graph')
def graph():
    return render_template('datta.html')


@app.route('/sidorovich')
def sidorovich():
    return render_template('sidorovich.html')


if __name__ == '__main__':
    db_session.global_init("db/database.db")
    app.run(port=int(port), host=host)
