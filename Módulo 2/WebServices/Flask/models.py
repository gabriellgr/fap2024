from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    cliente_id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(1), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    email = db.Column(db.String(40), nullable = False)

class Ficha(db.Model):
    ficha_id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date, nullable = False)
    observacao = db.Column(db.Text)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente_id'), nullable = False)
    