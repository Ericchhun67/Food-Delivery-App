# Actual SQLite file (auto-created after running app).
# Stores all data: users, restaurants, menu items, orders, drivers, tracking.
# Connected to via database.py (db = SQLAlchemy()).
# Linked to:
#   • app.py (initializes db + migrations)
#   • models/*.py (define tables mapped into database.db)
#   • routes/*.py (query/update tables via models)
#   • utils/*.py (optional helpers that touch the database)


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy() # initialize SQLAlchemy 

# db will be linked to Flask app in app.py


# Models (tables) are defined in models/*.py and imported in app.py
# Migrations are handled via Flask-Migrate in app.py








