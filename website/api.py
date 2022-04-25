from flask import Blueprint, redirect, url_for, request
from .model import Vote, User, Position
import hashlib
from . import session
from . import db

api = Blueprint('api', __name__)

@api.route('/login.do', methods=['POST'])
def login():
        if 'user' in session:
                session.pop('user', None)
        if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                print(email, password)
                password = hashlib.md5(password.encode()).hexdigest()
                user = User.query.filter_by(_email=email).first()
                if user and password == user._password:
                        user = {'email': user._email, 'voted': user._voted, 'userid': user._userid}
                        session['user'] = user
                        print(email, password)
                        # return {'success' : True}
                        return redirect(url_for('views.dashboard'))
        # return {'success' : False}
        return redirect(url_for('views.login'))

@api.route('/logout.do', methods=['POST'])
def logout():
        if 'user' in session:
                session.pop('user', None)
        # return {'success': False}
        return redirect(url_for('views.login'))

@api.route('/vote.do', methods=['POST'])
def vote():

        user = session['user']

        if user['voted'] == 1:
                # return {'vote' : False};
                return redirect(url_for('views.dashboard'))

        session['user'] = {'email': user['email'], 'voted': 1, 'userid': user['userid']}

        user = User.query.filter_by(_email=user['email']).first()
        user._voted = 1
        
        db.session.commit()

        p = request.form['p-candidate']
        president = Vote.query.filter_by(_name=p).first()
        president._total_votes += 1

        vp = request.form['vp-candidate']
        vice_president = Vote.query.filter_by(_name=vp).first()
        vice_president._total_votes += 1

        db.session.commit()

        # return {'vote': True}
        return redirect(url_for('views.dashboard'))