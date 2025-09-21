# tracking.py
# Eric Chhun
# Tracks real-time driver location and updates the customer dashboard.

from database import db
from datetime import datetime

class Tracking(db.Model):
    __tablename__ = 'tracking'

    id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)

    # Live location
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    order = db.relationship('Order', back_populates='tracking')
    driver = db.relationship('Driver', back_populates='tracking')

    def __repr__(self):
        return f"<Tracking Order {self.order_id} Driver {self.driver_id} @ ({self.latitude}, {self.longitude})>"