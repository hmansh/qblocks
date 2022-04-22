from flask import Blueprint, redirect, url_for, render_template
from .model import Vote, User, Position
from . import session

views = Blueprint('views', __name__)

@views.route('/')
def home_redirect():
        return redirect(url_for('login'))

@views.route('/login')
def login():
        return render_template('login.html')

@views.route('/dashboard')
def dashboard():
        user = session['user']
        candidates = Vote.query.all()
        return render_template('dashboard.html', user=user, candidates=candidates)