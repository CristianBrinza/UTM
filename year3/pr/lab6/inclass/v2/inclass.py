# Importing necessary modules and packages
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

# Initializing the Flask application
app = Flask(__name__)
# Configuring the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initializing SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Defining a model for 'Scooter' in the database
class Scooter(db.Model):
    # Defining columns for the 'Scooters' table
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each scooter
    name = db.Column(db.String(80), nullable=False)  # Name of the scooter
    battery_level = db.Column(db.Float, nullable=False)  # Battery level of the scooter

# API endpoint to retrieve all scooters
@app.route('/scooters/', methods=['GET'])
def retrieve_scooters():
    """Endpoint to retrieve all scooters from the database."""
    # Querying all scooters from the database
    scooters = Scooter.query.all()
    # Logging the operation in the console
    print(f"Retrieved {len(scooters)} scooters from the database.")
    # Returning the scooters data as JSON
    return jsonify([{'id': s.id, 'name': s.name, 'battery_level': s.battery_level} for s in scooters])

# API endpoint to add a new scooter
@app.route('/scooters/', methods=['POST'])
def add_scooter():
    """Endpoint to add a new scooter to the database."""
    # Validating the request data
    if not request.json or 'name' not in request.json or 'battery_level' not in request.json:
        # Aborting the request with a 400 status code and error message
        abort(400, description="Missing required fields: name, battery_level")
    # Creating a new scooter instance and adding it to the database
    new_scooter = Scooter(name=request.json['name'], battery_level=request.json['battery_level'])
    db.session.add(new_scooter)
    db.session.commit()
    # Logging the operation in the console
    print(f"Added new scooter: {new_scooter.name}, Battery Level: {new_scooter.battery_level}")
    # Returning the new scooter data as JSON
    return jsonify({'id': new_scooter.id, 'name': new_scooter.name, 'battery_level': new_scooter.battery_level}), 201

# API endpoint to retrieve a specific scooter by ID
@app.route('/scooters/<int:scooter_id>', methods=['GET'])
def retrieve_scooter(scooter_id):
    """Endpoint to retrieve a specific scooter using its ID."""
    # Querying the scooter from the database using the provided ID
    scooter = Scooter.query.get(scooter_id)
    # Handling case where scooter is not found
    if scooter is None:
        # Aborting the request with a 404 status code and error message
        abort(404, description="Scooter not found")
    # Logging the operation in the console
    print(f"Retrieved scooter: {scooter.name}, Battery Level: {scooter.battery_level}")
    # Returning the scooter data as JSON
    return jsonify({'id': scooter.id, 'name': scooter.name, 'battery_level': scooter.battery_level})

# API endpoint to update a specific scooter by ID
@app.route('/scooters/<int:scooter_id>', methods=['PUT'])
def modify_scooter(scooter_id):
    """Endpoint to update the details of a specific scooter using its ID."""
    # Querying the scooter from the database using the provided ID
    scooter = Scooter.query.get(scooter_id)
    # Handling case where scooter is not found
    if scooter is None:
        # Aborting the request with a 404 status code and error message
        abort(404, description="Scooter not found")
    # Validating the request data
    if not request.json:
        # Aborting the request with a 400 status code and error message
        abort(400, description="Request body must be JSON")
    # Updating the scooter details and committing to the database
    scooter.name = request.json.get('name', scooter.name)
    scooter.battery_level = request.json.get('battery_level', scooter.battery_level)
    db.session.commit()
    # Logging the operation in the console
    print(f"Updated scooter {scooter.id}: Name: {scooter.name}, Battery Level: {scooter.battery_level}")
    # Returning the updated scooter data as JSON
    return jsonify({'id': scooter.id, 'name': scooter.name, 'battery_level': scooter.battery_level})

# API endpoint to delete a specific scooter by ID
@app.route('/scooters/<int:scooter_id>', methods=['DELETE'])
def remove_scooter(scooter_id):
    """Endpoint to delete a specific scooter using its ID."""
    # Querying the scooter from the database using the provided ID
    scooter = Scooter.query.get(scooter_id)
    # Handling case where scooter is not found
    if scooter is None:
        # Aborting the request with a 404 status code and error message
        abort(404, description="Scooter not found")
    # Deleting the scooter from the database and committing the changes
    db.session.delete(scooter)
    db.session.commit()
    # Logging the operation in the console
    print(f"Deleted scooter {scooter.id}: {scooter.name}")
    # Returning a success message as JSON
    return jsonify({'result': True})

# Configuring Swagger UI for API documentation
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "lab6_inclass"}
)

# Registering the Swagger UI blueprint with the Flask app
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Main execution block
if __name__ == '__main__':
    with app.app_context():
        # Creating the database tables
        db.create_all()
    # Running the Flask app
    app.run(debug=True)
