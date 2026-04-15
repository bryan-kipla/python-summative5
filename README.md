
# Python_summative5

## Project Description
A backend API built with Flask, SQLAlchemy, and Marshmallow for tracking workouts and exercises. Trainers can create workouts, add exercises, and record sets, reps, or duration.

## Installation
```bash
pipenv install Flask==2.2.2 Flask-Migrate==3.1.0 flask-sqlalchemy==3.0.3 Werkzeug==2.2.2 importlib-metadata==6.0.0 importlib-resources==5.10.0 ipdb==0.13.9 marshmallow==3.20.1
pipenv shell
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

## Run Instructions
```bash
flask run
```

## Endpoints
- **GET /workouts** – List all workouts  
- **GET /workouts/<id>** – Show a single workout with exercises  
- **POST /workouts** – Create a workout  
- **DELETE /workouts/<id>** – Delete a workout  
- **GET /exercises** – List all exercises  
- **GET /exercises/<id>** – Show a single exercise with workouts  
- **POST /exercises** – Create an exercise  
- **DELETE /exercises/<id>** – Delete an exercise  
- **POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises** – Add exercise to a workout with reps/sets/duration  