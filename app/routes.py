from app import app, db
from flask import jsonify, make_response, render_template, request
from datetime import datetime, timedelta
from random import randint
from .models import Forecast

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


@app.route('/forecast', methods=['POST'])
def forecast():
    city = request.args.get('city')
    date = request.args.get('date')
    date_format = datetime.strptime(data, '%d-%m-%y')
    forecast = Forecast(
        city=city,
        date=date,
        temperature = get_weather_for_date(date),
    )
    db.session.add(forecast)
    db.session.commit()
    return jsonify({'id': forecast._id}), 201


@app.route('/forecast/<_id>', methods=['GET', 'PATCH'])
def forecast_for_id(_id):
    if request.method == 'PATCH':
        temperature = request.args.get('temperature')

        forecast = Forecast.query.get_or_404(_id)
        forecast.temperature = temperature
        db.session.commit()

    elif request.method == 'GET':
        forecast = Forecast.query.get_or_404(_id)
        return jsonify({
            'id': forecast._id,
            'city': forecast.city,
            'temperature': forecast.temperature,
            'date': forecast.date
        })


@app.route('/delete_forecast/<_id>', methods=['DELETE'])
def delete_forecast(_id):
    forecast = Forecast.query.get_or_404(_id)
    db.session.delete(forecast)
    db.session.commit()
    return jsonify({'result': True})