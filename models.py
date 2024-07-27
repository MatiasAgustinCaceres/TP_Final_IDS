from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vala(db.Model):
    __tablename__ = 'Valar'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

class Troop(db.Model):
    __tablename__ = 'Troops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    combatPower = db.Column(db.Integer, nullable=False)
    consumption = db.Column(db.Integer, nullable=False)

class Campaign(db.Model):
    __tablename__ = 'Campaigns'
    id = db.Column(db.Integer, primary_key=True)
    vala = db.Column(db.Integer, db.ForeignKey('Valar.id'))
    generalName = db.Column(db.String(255), nullable=False)
    troopOne = db.Column(db.Integer, db.ForeignKey('Troops.id'))
    troopTwo = db.Column(db.Integer, db.ForeignKey('Troops.id'))
    troopThree = db.Column(db.Integer, db.ForeignKey('Troops.id'))
    troopFour = db.Column(db.Integer, db.ForeignKey('Troops.id'))
    status = db.Column(db.String(255), nullable=False)
    totalCombatPower = db.Column(db.Integer, nullable=False)