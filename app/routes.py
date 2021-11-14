from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.blueprint import bp
from app.models.city import City

from app.utils import get_weather_at


@bp.route("/")
def index():
    # Get all cities data from the database
    cities = City.find_all()
    return render_template("index.html", cities=cities if cities else None)


@bp.route("/add", methods=["POST"])
def add_city():
    if request.method == "POST":
        # get name of city from POST request and capitalize the first letter of each word
        name = request.form["name"].title()

        # Check if city has already been added to the database
        if City.find_by_name(name):
            flash("The city has already been added to the list!")
        else:
            data = get_weather_at(name)

            if data:
                weather_data = data.json()

                # Create an instance of City with weather data and commit to the database
                city = City(name=name,
                            current_temp=int(weather_data["main"]["temp"]),
                            current_state=weather_data["weather"][0]["main"])
                city.save_to_db()
            else:
                flash("The city doesn't exist!")

    return redirect(url_for("weather_app.index"))


@bp.route("/delete/<city_id>", methods=["GET", "POST"])
def delete_city(city_id: int):
    if city := City.find_by_id(city_id):
        city.delete_from_db()
    return redirect(url_for("weather_app.index"))
