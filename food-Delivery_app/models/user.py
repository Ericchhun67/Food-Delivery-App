
from database import db

class User(db.Model):
    __tablename__ = 'users' 
    
    id = db.Column(db.Integer, primary_key=True) # unique user ID
    name = db.Column(db.String(100), nullable=False) # user's full name
    username = db.Column(db.String(80), unique=True, nullable=False) # username for login
    password = db.Column(db.String(200), nullable=False) # hashed password
    role = db.Column(db.String(20), nullable=False) # role: customer, driver, admin, restaurant_owner
    
    
    def __repr__(self):
        return f'<User {self.username}>'
        
    