
export FLASK_APP := "rentals"
export FLASK_DEBUG := "1"
export FLASK_ENV := "development"

install:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 deploy.py

run:
    flask run

dev:
    watchexec --exts py,html,css --restart -- flask run
