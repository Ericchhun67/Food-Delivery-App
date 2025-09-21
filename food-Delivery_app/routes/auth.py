# 
# auth.py
# Eric Chhun
# 09/16/2025
# This is a Flask Blueprint inside your routes/ folder. 
# It takes care of authentication (login, register, logout).
# Login route: renders index.html (login form), checks credentials, 
# starts a session, redirects to dashboard.
# 	•	Register route: renders register.html, accepts POST requests, 
# validates input, creates a new user in the database, then redirects to login.
# 	•	Logout route: clears the session and redirects back to login page.


from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User 
from database import db




bp = Blueprint('auth', __name__)

# register route
@bp.route('/register', methods=['GET', 'POST'])
def register():
    # if GET, show the registration form
    # Make sure templates/register.html exists.
    # In register.html, set form action to {{ url_for('auth.register') }}.
    if request.method == 'GET':
        return render_template('register.html')
    
    # create new user if POST
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return "Username and password are required.", 400
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "Username already taken. Please choose another.", 400
    
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))
    
    
# login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
    # if GET, Show the login form
    if request.method == 'GET':
        return render_template('index.html')
    # if POST, verify credentials and log in the user
    username = request.form.get('username')
    # get the password from the form data
    password = request.form.get('password')
    # check if username and password are provided
    if not username or not password:
        # display error for missing fields
        return "Missing username or password.", 400
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for('auth.dashboard'))
    else:
        # display error for invalid credentials
        return "Invalid credentials. please try again.", 401
    
# logout route
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


    
        
    
        
        