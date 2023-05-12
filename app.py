from flask import Flask, render_template, url_for
"""from flask_sqlalchemy import SQLAlchemy
from datetime import datetime """

app = Flask(__name__)
"""db = SQLAlchemy()
db_name = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite=:///{db_name.db}'
db.init_app(app)

class Tracker(db.model):
    date = db.column(db.String, primary_key= True)
    content = db.column(db.string(200), nullable = False)
    date_made = db.column(db.Datetime, default=datetime.utcnow)

    def __repr__(self):
        return "<workout %r> " % self.id"""
@app.route("/")
@app.route("/home") 
def home():
    return render_template("index.html", data = data)

data =[
    {
        "Exercise": "bench press",
        "Sets": "3",
        "Reps": "10",
        "Weight": "185",
    },  
    {
        "Exercise": "Squat",
        "Sets": "3",
        "Reps": "10",
        "Weight": "245",
    }
]

@app.route("/about") 
def about():
    return "<h1>About Page<h1>"

if __name__ == "__main__":
    app.run(debug=True)