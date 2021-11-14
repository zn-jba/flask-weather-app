from flask import Blueprint

bp = Blueprint(name="weather_app",
               import_name=__name__)

from app import routes
