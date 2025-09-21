# driver.py
# Eric Chhun
# Represents delivery drivers in the Food Delivery App.

from database import db

class Driver(db.Model):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Status
    availability = db.Column(db.Boolean, default=True)   # True = available for deliveries
    vehicle_type = db.Column(db.String(50), nullable=True)  # e.g., car, bike, scooter

    # Relationships
    orders = db.relationship("Order", back_populates="driver")   # driver can handle many orders
    tracking = db.relationship("Tracking", back_populates="driver", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Driver {self.name} ({'Available' if self.availability else 'Busy'})>"