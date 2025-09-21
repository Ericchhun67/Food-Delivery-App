
# order_item.py
# Eric Chhun
# Defines the OrderItem model for the food delivery app.
# Each order can have multiple items, each linked to a MenuItem.

from database import db

class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)  # number of items

    # Foreign Key → Link to order
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)

    # Foreign Key → Link to menu item
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)

    # Relationships
    order = db.relationship('Order', back_populates='order_items')
    menu_item = db.relationship('MenuItem', back_populates='order_items')

    def __repr__(self):
        return f"<OrderItem {self.quantity}x {self.menu_item.name}>"