from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired


class Route(FlaskForm):
    coor_ax = IntegerField("Координата X точки A", validators=[DataRequired()])
    coor_ay = IntegerField("Координата Y точки A", validators=[DataRequired()])

    coor_bx = IntegerField("Координата X точки B", validators=[DataRequired()])
    coor_by = IntegerField("Координата Y точки B", validators=[DataRequired()])
    submit = SubmitField('куда идти, если я не хочу сдохнуть?')