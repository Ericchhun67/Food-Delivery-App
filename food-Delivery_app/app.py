#
# Food Delivery.py
# Eric Chhun
# 09/16/2025
# food delivery app
# •	Starts the Flask app → it’s the entry point (python app.py).
# •	Configures the app → sets secret keys, debug mode, database connection.
# •	Registers Blueprints → links all the route files (auth.py, account.py, dashboard.py).
# •	Initializes database models → tells Flask/SQLAlchemy about your user.py, account.py, etc.
# •	Serves templates + static files → lets index.html, dashboard.html, and JS/CSS load correctly.

from flask import Flask # core Flask framework
from flask_sqlalchemy import SQLAlchemy # for database integration
from flask import render_template, request, redirect, url_for, session # for serving HTML templates
from routes import auth, customers, driver as driver_routes, resturant, admin
from routes import tracking as tracking_routes 
from database import db # import the db instance from database.py

app = Flask(__name__) # create Flask app instance

app.config['SECRET_KEY'] = 'your_secret_key' # Replace with a secure key in production
# Using SQLite for simplicity; switch to PostgreSQL/MySQL in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_delivery.db'

db.init_app(app) # initialize SQLAlchemy with the app

# import models to create tables
from models import driver, menu_item, order_item, order, restaurant, tracking, user

# # import and register blueprints

app.register_blueprint(auth.bp)
# app.register_blueprint(customers.bp)
# app.register_blueprint(driver.bp)
# app.register_blueprint(resturant.bp)
# Register tracking blueprint at its declared url_prefix ("/tracking")
app.register_blueprint(tracking_routes.bp)
# app.register_blueprint(admin.bp)

# (Removed incorrect /api/tracking redirects; tracking UI lives at /tracking/<order_id>)

# simple route to test
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/dashboard')
def dashboard():
    # Placeholder username, replace with actual user session data
    return render_template('dashboard.html', username=session.get('username', 'Guest'))
    
# route for registration page
@app.route('/register', methods=['GET', 'POST'])
# A function to handle user registration by redirecting to the auth blueprint
def register():
    return render_template('register.html')
    

# route for traking page
@app.route('/track-order')
def track_order():
    return render_template('tracking.html', username=session.get('username', 'Guest'))

# route for logout
@app.route('/logout')
# A function to handle user logout by clearing the session and redirecting to login
def logout():
    # Clear user session data to log out the user and redirect to login page
    session.clear()
    return redirect(url_for('auth.login'))
    
# @app.route('/customers/dashboard')
# def customer_dashboard():
#     return render_template('dashboard.html', username=session.get('username', 'Guest'))


@app.route('/profile')
def profile():
    return render_template('profile.html', username=session.get('username', 'Guest'))
    
# Tracking page is served by the tracking blueprint at /tracking/<int:order_id>


# create Db tables on the first run
with app.app_context():
    db.create_all()

# run the app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) # enable debug mode for development
    
    
    

# Note: work on dashboard.html next - need to debug more
# Note: work on register.html next
# note: fix the routes to register file
