from flask import Flask, render_template, url_for

app = Flask(__name__)

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