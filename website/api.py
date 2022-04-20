from flask import Blueprint, redirect, url_for, render_template, request
from .model import Vote, User, Position
from . import db

api = Blueprint('api', __name__)

@api.route('/login.do', methods=['POST'])
def login():
        email = request.form['email']
        password = request.form['password']
        print(email, password)
        return redirect(url_for('views.dashboard'))

@api.route('/logout.do', methods=['POST'])
def logout():
        print('LOGOUT')
        
        p = request.form['p-cand']
        president = Vote.query.filter_by(_name=p).first()
        president._total_votes += 1

        vp = request.form['vp-cand']
        vice_president = Vote.query.filter_by(_name=vp).first()
        vice_president._total_votes += 1

        db.session.commit()

        # user = session['user']
        # session['user'] = {'email': user['email'], 'voted': 1, 'uid': user['uid']}
        # user = User.query.filter_by(_email=user['email']).first()
        # user._voted = 1
        # db.session.commit()

        return redirect(url_for('authentication.login'))

@api.route('/vote.do', methods=['POST'])
def vote():
        return render_template('dashboard.html')