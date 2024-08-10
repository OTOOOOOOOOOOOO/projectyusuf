from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/IGS')
def IGS():
    return render_template("IGS.html")
 
if __name__ == "__main__":
    app.run(debug=True)