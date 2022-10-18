from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
import calendar
import datetime

months_amount = 3
users = ["Bartek", "Kasia", "Karolina", "Madzia", "Pawel"]
meetings = {}
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# class Choices(db.Model):
#     __tablename__ = "boardgame"
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(100), unique=True)
#     dates = db.Column(db.String(1000))
# db.create_all()


@app.route('/')
def index():
    date = []

    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    date.append([[current_year, months[current_month]]] + calendar.monthcalendar(current_year, current_month))

    for _ in range(1, months_amount):
        current_month = current_month + 1
        if current_month > 12:
            current_year = current_year + 1
            current_month = 1
        date.append([[current_year, months[current_month]]] + calendar.monthcalendar(current_year, current_month))

    return render_template("index.html", data=meetings, dates=date, users=users)


@app.route('/add', methods=["POST"])
def add_availability():
    if request.method == "POST":
        user_data = request.json
        user_name = user_data["name"]
        user_meetings = user_data["data"]
        if user_meetings:
            for meeting in user_meetings:
                if meeting in meetings:
                    meetings[meeting].append(user_name)
                else:
                    meetings[meeting] = [user_name]

                meetings[meeting] = list(set(meetings[meeting]))

    response = make_response("Successfully added.")
    response.status_code = 200
    return response


@app.route('/clear', methods=["POST"])
def clear_availability():
    if request.method == "POST":
        data = request.json
        user_name = data["name"]
        for event in meetings.copy().items():
            user_name in event[1] and event[1].remove(user_name)
            if not event[1]:
                del meetings[event[0]]

    response = make_response("Successfully cleared.")
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
    app.run()
