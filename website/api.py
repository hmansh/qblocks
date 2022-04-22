from flask import Blueprint, redirect, url_for, render_template, request
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
                        return redirect(url_for('views.dashboard'))
        return redirect(url_for('views.login'))

@api.route('/logout.do', methods=['POST'])
def logout():
        if 'user' in session:
                session.pop('user', None)
        return redirect(url_for('views.login'))

@api.route('/vote.do', methods=['POST'])
def vote():
        p = request.form['p-candidate']
        president = Vote.query.filter_by(_name=p).first()
        president._total_votes += 1

        vp = request.form['vp-candidate']
        vice_president = Vote.query.filter_by(_name=vp).first()
        vice_president._total_votes += 1

        db.session.commit()

        user = session['user']
        session['user'] = {'email': user['email'], 'voted': 1, 'userid': user['userid']}
        user = User.query.filter_by(_email=user['email']).first()
        user._voted = 1
        db.session.commit()

        return redirect(url_for('views.dashboard'))