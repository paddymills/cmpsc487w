from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    res = [
        { "id": 1, "reserved_by": "John Doe", "vehicle": "Sprinter Van", "return_date": "2020-01-01" },
        { "id": 2, "reserved_by": "Jane Doe", "vehicle": "Ford Focus", "return_date": "2020-01-02" },
    ]
    return render_template("admin.html", reservations=res)

@app.errorhandler(404)
def notfound():
    return "site not found", 404