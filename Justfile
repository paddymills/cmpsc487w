install:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

run:
    flask --app app run

dev:
    watchexec --exts py,html,css --restart -- flask --app app run
