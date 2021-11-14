# Weather App

## About

My solution for the [**Weather App**][project] project on the learning platform [**JetBrains Academy**][platform].

[platform]: https://hyperskill.org/

[project]: https://hyperskill.org/projects/164

## Functionality

A web application that retrieves the current weather from any city all over the world. It stores the city, weather
temperature and state at the time of the retrieval on a local SQLite database. It's powered by the Flask web framework
with the Flask-SQLAlchemy package and the OpenWeather API.

## Setup

To create the required table start a flask shell session in the projects root directory and run these commands:

```py
from app import db

db.create_all()
quit()
```

To run the application, open a terminal in the projects root directory and run this command:

```bash
flask run
```