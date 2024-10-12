
from flask import Blueprint, render_template
from flask_login import login_required
from .models import Reservation

admin = Blueprint('admin', __name__)

@admin.route("/admin")
@login_required
def index():
    return render_template("admin.html", reservations=Reservation.query.all())