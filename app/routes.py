from app import app
from flask import jsonify, make_response, render_template
from datetime import datetime, timedelta
from random import randint

CITY = 'Amsterdam'
CITIES = ['amsterdam', 'moscow']


class Week:
    def __init__(self, start):
        self.start = start.strftime('%d-%m-%y')
        self.end = (start + timedelta(days=7)).strftime('%d-%m-%y')
        self.week_days = self.get_weekdays(start)

    def get_weekdays(self, start):
        weekdays = []
        for i in range(8):
            weekdays.append((start + timedelta(days=i)).strftime('%d-%m-%y'))
        return weekdays


def get_weather_for_date():
    return randint(5, 15)


@app.route('/hello')
def index():
    return "<h2>Hi, fellow Flask developer!<h2>"


@app.route('/time')
def current_time():
    return make_response(jsonify(time=datetime.now()), 201)


@app.route('/')
@app.route('/week')
def weather_week():
    week = Week(datetime.today())
    week_weather = {day: get_weather_for_date() for day in week.week_days}
    return render_template('week_overview.html', week=week, city=CITY, week_weather=week_weather)


@app.route('/week/<city>')
def weather_in_city(city):
    city = city.lower()
    if city in CITIES:
        week = Week(datetime.today())
        week_weather = {day: get_weather_for_date() for day in week.week_days}
        return render_template('week_overview.html', week=week, city=city, week_weather=week_weather)
    return render_template('404.html'), 404

@app.route('/your_city')
def weather_your_city():
    week = Week(datetime.today())
    return render_template('week_overview.html', week=week)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
