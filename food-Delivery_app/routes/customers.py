#
# customers.py
# Eric Chhun
# 09/16/2025
# This file is a Flask Blueprint dedicated to 
# customer-facing features of your food delivery app. 
# It handles routes like browsing restaurants, viewing menus, 
# adding items to the cart, and placing orders. Customers 
# interact with this blueprint through the frontend 
# templates (dashboard.html, cart.html, orders.html) 
# and it connects with the database models 
# (user.py, restaurant.py, menu_item.py, order.py, order_item.py) 
# to store and fetch customer actions. It also links with utils/validators.py 
# for input validation and can call utils/payments.py when simulating checkout. 
# Finally, it ties into app.py via app.register_blueprint(customers.bp), 
# making these customer features accessible in the overall app.


from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User
# # from models.restaurant import Restaurant
# from models.menu_item import MenuItem
# from models.order import Order
# from models.order_item import OrderItem
# from database import db
# from utils import validators, payments, notifications, tracking_utils
# import datetime
import random


bp = Blueprint('customers', __name__, url_prefix='/customers')

    





