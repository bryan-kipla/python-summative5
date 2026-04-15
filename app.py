from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/bryan/Moringaschool/module5/python-summative5/instance/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# MODELS
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=lambda: date.today())
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

class WorkoutExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workout.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercise.id"))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)

# ROUTES
@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify([{
        "id": w.id,
        "date": str(w.date),
        "duration_minutes": w.duration_minutes,
        "notes": w.notes
    } for w in workouts])

@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()
    new_workout = Workout(
        date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
        duration_minutes=int(data["duration_minutes"]),
        notes=data.get("notes")
    )
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({
        "id": new_workout.id,
        "date": str(new_workout.date),
        "duration_minutes": new_workout.duration_minutes,
        "notes": new_workout.notes
    }), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
