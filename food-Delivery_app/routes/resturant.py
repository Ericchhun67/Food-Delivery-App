# restaurant.py
# Eric Chhun
# Defines the Restaurant model for the food delivery app.

from database import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each restaurant
    name = db.Column(db.String(120), nullable=False)  # Restaurant name
    address = db.Column(db.String(255), nullable=False)  # Address
    phone = db.Column(db.String(20))  # Optional contact number
    email = db.Column(db.String(120), unique=True)  # Contact email

    # Relationships
    menu_items = db.relationship('MenuItem', back_populates='restaurant', cascade="all, delete-orphan")
    orders = db.relationship('Order', back_populates='restaurant', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Restaurant {self.name}>"