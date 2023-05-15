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
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Exercise: {self.exercise}, Sets: {self.sets}, Reps: {self.reps}, Weight: {self.weight}, Time: {self.date_created}"

    

@app.route('/add', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        exercise = request.form['exercise']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']
        new_workout = userdata(exercise=exercise, sets=sets, reps=reps, weight=weight)
        try:
            db.session.add(new_workout)
            db.session.commit()
            return redirect(url_for('home'))
        except:
            return "Issue adding data"
    else:
        entries = userdata.query.order_by(userdata.date_created).all()
        return render_template('add.html', entries = entries)

@app.route("/")
@app.route("/home") 
def home():
    entries = userdata.query.order_by(userdata.date_created).all()
    return render_template("homepage.html",entries = entries)

@app.route('/view', methods=['GET'])
def view_workout():
    if request.method == 'GET':
        entries = userdata.query.order_by(userdata.date_created).all()
        return render_template("view.html",entries = entries)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

"""TODO: Have created entries add on top of each other on homepage lists, fix table when there are no entries"""