# Importing necessary modules from Flask
from flask import Flask, request, jsonify, abort
# Importing Swagger UI blueprint function for API documentation
from flask_swagger_ui import get_swaggerui_blueprint

# Initializing Flask app
application = Flask(__name__)

# Configuring Swagger UI
# Setting the URL path where Swagger UI will be served
DOCS_URL = '/api/documentation'
# Setting the URL where API definition (swagger.json) is located
API_DEFINITION_URL = '/static/api_definition.json'

# Creating Swagger UI blueprint
# This blueprint serves the Swagger UI at the specified URL and loads the API definition
api_docs_blueprint = get_swaggerui_blueprint(
    DOCS_URL,
    API_DEFINITION_URL,
    # Overriding Swagger UI configuration to update the app name
    config={
        'app_name': "Electric Scooter API"
    }
)

# Registering the Swagger UI blueprint with the Flask app
application.register_blueprint(api_docs_blueprint, url_prefix=DOCS_URL)

# Creating an in-memory database (dictionary) to store scooter data
SCOOTER_DATABASE = {}

# Defining API route to fetch all scooters
@application.route('/electricscooters/', methods=['GET'])
def retrieve_scooters():
    """Retrieve and display all scooters"""
    # Logging to console
    print("Fetching all scooters from the database...")
    # Returning all scooters in JSON format
    return jsonify(list(SCOOTER_DATABASE.values()))

# Defining API route to add a new scooter
@application.route('/electricscooters/', methods=['POST'])
def add_scooter():
    """Add a new scooter to the database"""
    # Validating input data
    if not request.json or 'name' not in request.json or 'battery_level' not in request.json:
        # Logging to console
        print("Invalid input. Name and battery level are required.")
        # Aborting request with HTTP 400 status code
        abort(400)
    # Generating a new scooter ID
    scooter_id = len(SCOOTER_DATABASE) + 1
    # Creating a new scooter object
    new_scooter = {
        'id': scooter_id,
        'name': request.json['name'],
        'battery_level': request.json['battery_level']
    }
    # Adding the new scooter to the database
    SCOOTER_DATABASE[scooter_id] = new_scooter
    # Logging to console
    print(f"New scooter added: {new_scooter}")
    # Returning the new scooter data in JSON format with HTTP 201 status code
    return jsonify(new_scooter), 201

# Defining API route to fetch a specific scooter by ID
@application.route('/electricscooters/<int:scooter_id>', methods=['GET'])
def retrieve_scooter(scooter_id):
    """Retrieve a specific scooter using its ID"""
    # Checking if the scooter exists in the database
    if scooter_id not in SCOOTER_DATABASE:
        # Logging to console
        print(f"Scooter with ID {scooter_id} not found.")
        # Aborting request with HTTP 404 status code
        abort(404)
    # Returning the requested scooter data in JSON format
    return jsonify(SCOOTER_DATABASE[scooter_id])

# Defining API route to delete a specific scooter by ID
@application.route('/electricscooters/<int:scooter_id>', methods=['DELETE'])
def remove_scooter(scooter_id):
    """Remove a specific scooter using its ID"""
    # Checking if the scooter exists in the database
    if scooter_id not in SCOOTER_DATABASE:
        # Logging to console
        print(f"Scooter with ID {scooter_id} not found.")
        # Aborting request with HTTP 404 status code
        abort(404)
    # Deleting the scooter from the database
    del SCOOTER_DATABASE[scooter_id]
    # Logging to console
    print(f"Scooter with ID {scooter_id} deleted.")
    # Returning a success response in JSON format
    return jsonify({'result': True})

# Defining API route to update a specific scooter by ID
@application.route('/electricscooters/<int:scooter_id>', methods=['PUT'])
def modify_scooter(scooter_id):
    """Modify details of a specific scooter using its ID"""
    # Checking if the scooter exists in the database
    if scooter_id not in SCOOTER_DATABASE:
        # Logging to console
        print(f"Scooter with ID {scooter_id} not found.")
        # Aborting request with HTTP 404 status code
        abort(404)
    # Validating input data
    if not request.json:
        # Logging to console
        print("Invalid input. JSON data expected.")
        # Aborting request with HTTP 400 status code
        abort(400)
    # Updating scooter details
    SCOOTER_DATABASE[scooter_id]['name'] = request.json.get('name', SCOOTER_DATABASE[scooter_id]['name'])
    SCOOTER_DATABASE[scooter_id]['battery_level'] = request.json.get('battery_level', SCOOTER_DATABASE[scooter_id]['battery_level'])
    # Logging to console
    print(f"Scooter with ID {scooter_id} updated: {SCOOTER_DATABASE[scooter_id]}")
    # Returning the updated scooter data in JSON format
    return jsonify(SCOOTER_DATABASE[scooter_id])

# Running the Flask app
if __name__ == '__main__':
    # Enabling debug mode for development
    application.run(debug=True)
