from flask import render_template, session, redirect, url_for, current_app
from datetime import datetime
from . import main
from ..models import Curso
from .forms import NameForm
import os
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .. import db

@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@main.route('/professores')
def professores():
    return render_template('indisponivel.html', current_time=datetime.utcnow())

@main.route('/disciplinas')
def disciplinas():
    return render_template('indisponivel.html', current_time=datetime.utcnow())

@main.route('/alunos')
def alunos():
    return render_template('indisponivel.html', current_time=datetime.utcnow())

@main.route('/cursos', methods=['GET', 'POST'])
def cursos():
    form = NameForm()
    if form.validate_on_submit():
        curso = Curso.query.filter_by(nome=form.nome.data).first()
        if curso is None:
            curso = Curso(nome=form.nome.data, desc=form.desc.data)
            db.session.add(curso)
            db.session.commit()
    return render_template('cursos.html', form=form, current_time=datetime.utcnow(), cursos=Curso.query.all())

@main.route('/ocorrencias')
def ocorrencias():
    return render_template('indisponivel.html', current_time=datetime.utcnow())
