from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired


class Route(FlaskForm):
    coor_ax = IntegerField("Координата X точки A", default=0)
    coor_ay = IntegerField("Координата Y точки A", default=0)

    coor_bx = IntegerField("Координата X точки B", default=0)
    coor_by = IntegerField("Координата Y точки B", default=0)
    submit = SubmitField('куда идти, если я не хочу сдохнуть?')
