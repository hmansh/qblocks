from flask import Blueprint, render_template, request

authentication = Blueprint('authentication', __name__)

@authentication.route('/login')
def login():
        return render_template('login.html')

@authentication.route('/logout')
def logout():
        return "<p>logout</p>"
