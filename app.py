from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class userdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(50), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    """time = db.Column(db.DateTime, default=datetime.utcnow)"""

    def __repr__(self):
        return f"Exercise: {self.exercise}, Sets: {self.sets}, Reps: {self.reps}, Weight: {self.weight}"

    

@app.route('/add', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        exercise = request.form['exercise']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']
        workout = userdata(exercise=exercise, sets=sets, reps=reps, weight=weight)
        db.session.add(workout)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route("/")
@app.route("/home") 
def home():
    workouts = userdata.query.all()
    return render_template("index.html", workouts=workouts)


@app.route("/about") 
def about():
    return "<h1>About Page<h1>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)