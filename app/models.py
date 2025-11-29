from flask import current_app
from . import db


class Curso(db.Model):
    __tablename__: 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)
    desc = db.Column(db.String(64), unique=True, index=True)