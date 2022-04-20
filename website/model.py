from . import db

class User(db.Model):
        _userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
        _email = db.Column(db.String(30), unique=True, nullable=False)
        _password = db.Column(db.String(150), nullable=False)
        _voted = db.Column(db.Integer, default=0)
        
        def __repr__(self) -> str:
                return f'{self._userid} {self._email} {self._voted}'

class Position(db.Model):
        _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        _position = db.Column(db.String(50), nullable=False)
        
        def __repr__(self) -> str:
                return f'{self._id} {self._position}'


class Vote(db.Model):
        _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        _fkid = db.Column(db.Integer, db.ForeignKey('position._id'))
        _name = db.Column(db.String(50), nullable=False)
        _total_votes = db.Column(db.Integer, nullable=False, default=0)

        def __repr__(self) -> str:
                return f'{self._id} {self._fkid} {self._name} {self._total_votes}'