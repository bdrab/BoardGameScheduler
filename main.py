from flask import Flask, redirect, request, render_template, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import calendar


meetings = {}
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# class Choices(db.Model):
#     __tablename__ = "boardgame"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     website_address = db.Column(db.String(100))
#     user_name = db.Column(db.Integer)
# db.create_all()


@app.route('/')
def index():
    date = calendar.monthcalendar(2022, 10)
    return render_template("index.html", data=meetings, date=date)


@app.route('/register', methods=["GET", "POST"])
def register_func():
    if request.method == "POST":
        pass

    return redirect(url_for("index"))


@app.route('/test', methods=["GET", "POST"])
def test_func():
    if request.method == "POST":
        print(request.json)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
    app.run()
