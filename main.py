from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



#create Routes
@app.route("/")
def home():
    return "Hello!"



if __name__ == "__main__":
    app.run(debug=True)