
from rentals import create_app, db
from rentals.models import *

app = create_app()
app.app_context().push()
db.create_all()

db.session.add_all([
    User(name='admin', password='password'),
    Vehicle(description='Sedan'),
    Vehicle(description='Van'),
    Vehicle(description='SUV'),
    Vehicle(description='Pick-up Truck'),
])
db.session.commit()
