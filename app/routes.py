from flask import Blueprint, request, jsonify, render_template
from app.models import db, Destination

main = Blueprint('main', __name__)

@main.route('/')
def index():
    destinations = Destination.query.all()
    return render_template('index.html', destinations=destinations)

@main.route('/destination', methods=['POST'])
def add_destination():
    data = request.form
    destination = Destination(name=data.get("name"), description=data.get("description"))
    db.session.add(destination)
    db.session.commit()
    return jsonify({"message": "Destination added", "destination": {"name": destination.name, "description": destination.description}}), 201

@main.route('/destination/<int:id>', methods=['PUT'])
def edit_destination(id):
    destination = Destination.query.get(id)
    if destination:
        data = request.form
        destination.name = data.get("name")
        destination.description = data.get("description")
        db.session.commit()
        return jsonify({"message": "Destination updated", "destination": {"name": destination.name, "description": destination.description}}), 200
    return jsonify({"message": "Destination not found"}), 404

@main.route('/destination/<int:id>', methods=['DELETE'])
def delete_destination(id):
    destination = Destination.query.get(id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({"message": "Destination deleted", "destination": {"name": destination.name, "description": destination.description}}), 200
    return jsonify({"message": "Destination not found"}), 404


