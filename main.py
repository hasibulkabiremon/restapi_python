from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy #ORM(object relational mapper)

app = Flask(__name__)

#create database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50),nullable=False)
    country = db.Column(db.String(50),nullable=False)
    rating = db.Column(db.Float,nullable=False)

    def to_dict(self):
        return{
            "id":self.id,
            "destination":self.destination,
            "country":self.country,
            "rating":self.rating
        }

with app.app_context():
    db.create_all()


#create Routes
@app.route("/")
def home():
    return jsonify({"message":"This is Flask json response!"})

@app.route("/destinations", methods =["GET"])
def get_destinations():
    destinations = Destination.query.all()
    if destinations:
        return jsonify([destination.to_dict()] for destination in destinations)
    else:
        return jsonify({"error":"Destinations not found!"}), 404

@app.route("/destinations/<int:destination_id>", methods =["GET"])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error":"Destination not found!"}), 404
    

#POST
@app.route("/destinations", methods=["POST"])
def add_destination():
    data = request.get_json()
    new_destination = Destination()
    new_destination.destination= data["destination"]
    new_destination.country= data["country"]
    new_destination.rating=data["rating"]

    db.session.add(new_destination)
    db.session.commit()

    return jsonify(new_destination.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)