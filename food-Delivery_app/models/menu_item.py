


# The menu_item.py file defines the Menu Item model for your food-delivery app. Each menu item belongs to a specific restaurant (restaurant_id) and contains details such as the item’s name, description, price, and availability. This model makes it possible for customers to browse a restaurant’s menu, add items to their cart, and place orders.

# It links directly to:
# 	•	restaurant.py → Each MenuItem is tied to a restaurant by a foreign key (restaurant_id).
# 	•	order_item.py → When a customer places an order, the chosen MenuItem entries are stored in this table.
# 	•	customer.py (routes) → Allows customers to view menus and select menu items.
# 	•	menu.js (frontend) → Dynamically loads the menu items for display in dashboard.html or restaurant.html.
# 	•	Database (database.db) → Stores all menu item records permanently.




from database import db





class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each menu item
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # FK → restaurant table
    name = db.Column(db.String(120), nullable=False)  # Item name (e.g., "Cheeseburger")
    description = db.Column(db.String(255))  # Short description of the item
    price = db.Column(db.Float, nullable=False)  # Price of the item
    available = db.Column(db.Boolean, default=True)  # True if available, False if sold out

    # Relationships
    restaurant = db.relationship('Restaurant', back_populates='menu_items')
    order_items = db.relationship('OrderItem', back_populates='menu_item')

    def __repr__(self):
        return f"<MenuItem {self.name} (${self.price})>"