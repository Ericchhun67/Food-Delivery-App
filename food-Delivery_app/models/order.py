from database import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="pending")

    # Relationship → link back to order items
    order_items = db.relationship('OrderItem', back_populates='order', cascade="all, delete-orphan")

    restaurant = db.relationship('Restaurant', back_populates='orders')

    # Tracking relationship (each order can have many tracking points over time)
    tracking = db.relationship('Tracking', back_populates='order', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order {self.id} - {len(self.order_items)} items - ${self.total}>"