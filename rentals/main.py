
from datetime import date
from flask import Blueprint, render_template, request
from .models import Vehicle, Reservation
from . import db

main = Blueprint('main', __name__)

@main.route("/")
def index():
    vehicles = Vehicle.query.all()

    return render_template("index.html", vehicles=vehicles)

@main.post("/")
def rent():
    name = request.form.get("name")
    vehicle_id = int(request.form.get("vehicle"))
    start = date.fromisoformat(request.form.get("start"))
    end = date.fromisoformat(request.form.get("end"))

    rental = Reservation(reserved_by=name, vehicle_id=vehicle_id, pickup_date=start, return_date=end)
    db.session.add(rental)
    db.session.commit()

    return render_template("index.html", msg="Rented!")

@main.errorhandler(404)
def notfound():
    return "site not found", 404
