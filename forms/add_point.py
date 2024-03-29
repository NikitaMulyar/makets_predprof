from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired


class Point(FlaskForm):
    id_point = IntegerField("Id детектора", validators=[DataRequired()])
    coor_x = IntegerField("Координаты X", default=0)
    coor_y = IntegerField("Координаты Y", default=0)

    anomalia_id_1 = StringField("Id аномалии 1", default='')
    anomali_rate_1 = FloatField("Радиация аномалии 1", default=1)

    anomalia_id_2 = StringField("Id аномалии 2", default='')
    anomali_rate_2 = FloatField("Радиация аномалии 2", default=1)

    anomalia_id_3 = StringField("Id аномалии 3", default='')
    anomali_rate_3 = FloatField("Радиация аномалии 3", default=1)

    anomalia_id_4 = StringField("Id аномалии 4", default='')
    anomali_rate_4 = FloatField("Радиация аномалии 4", default=1)

    anomalia_id_5 = StringField("Id аномалии 5", default='')
    anomali_rate_5 = FloatField("Радиация аномалии 5", default=1)

    anomalia_id_6 = StringField("Id аномалии 6", default='')
    anomali_rate_6 = FloatField("Радиация аномалии 6", default=1)

    submit = SubmitField('Продолжить')
