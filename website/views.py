from flask import Blueprint, redirect, url_for, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home_redirect():
        return redirect(url_for('authentication.login'))

@views.route('/dashboard')
def dashboard():
        return render_template('dashboard.html')