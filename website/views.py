from flask import Blueprint, redirect, url_for, render_template
from .model import Vote, User, Position
from . import session

views = Blueprint('views', __name__)

@views.route('/')
def home_redirect():
        return redirect(url_for('views.login'))

@views.route('/login')
def login():
        if 'user' in session:
                session.pop('user', None)
        return render_template('login.html')

@views.route('/dashboard')
def dashboard():
        if 'user' in session:
                user = session['user']
                candidates = Vote.query.all()
                return render_template('dashboard.html', user=user, candidates=candidates)
        return redirect(url_for('views.login'))