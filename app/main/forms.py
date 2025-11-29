from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Length
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    nome = StringField('Qual é o nome do curso?', validators=[DataRequired(), Length(max=250)])
    desc = TextAreaField('Descrição (250 caracteres)', validators=[Length(max=250)])
    submit = SubmitField('Submit')
