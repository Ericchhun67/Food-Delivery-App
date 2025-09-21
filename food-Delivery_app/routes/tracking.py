
# routes/tracking.py
from flask import Blueprint, render_template, request, jsonify
from models.tracking import Tracking
from database import db

bp = Blueprint("tracking", __name__, url_prefix="/tracking")

# Renders the tracking page
@bp.route("/<int:order_id>")
def tracking_page(order_id):
    return render_template("tracking.html", order_id=order_id)

# API to update driver location
@bp.route("/update", methods=["POST"])
def update_location():
    data = request.json
    order_id = data.get("order_id")
    driver_id = data.get("driver_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if not all([order_id, driver_id, latitude, longitude]):
        return jsonify({"error": "Missing fields"}), 400

    tracking = Tracking(order_id=order_id, driver_id=driver_id,
                        latitude=latitude, longitude=longitude)
    db.session.add(tracking)
    db.session.commit()
    return jsonify({"message": "Location updated"}), 201

# API to fetch driver location for an order
@bp.route("/get/<int:order_id>")
def get_location(order_id):
    tracking = Tracking.query.filter_by(order_id=order_id).order_by(Tracking.timestamp.desc()).first()
    if not tracking:
        return jsonify({"error": "No tracking data"}), 404
    return jsonify({
        "driver_id": tracking.driver_id,
        "latitude": tracking.latitude,
        "longitude": tracking.longitude,
        "timestamp": tracking.timestamp.isoformat()
    })