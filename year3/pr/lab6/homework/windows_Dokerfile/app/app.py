# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab6 homework


print('')
print('▒█▀▄▒█▀▄  lab. PR | FAF | FCIM | UTM | Fall 2023')
print('░█▀▒░█▀▄  FAF-212 Cristian Brinza lab5 homework  ')
print('')




# Import necessary modules from the Flask library to create a web application
from flask import Flask, request, jsonify, abort

# Import the psycopg2 module to interact with the PostgreSQL database
import psycopg2

# Import the get_swaggerui_blueprint function to set up Swagger UI for API documentation
from flask_swagger_ui import get_swaggerui_blueprint

# Create a Flask web application instance
app = Flask(__name__)

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database and return the connection object.
    """
    # Connect to the PostgreSQL database using the provided credentials and database details
    conn = psycopg2.connect(database="scooters",
                            user="admin",
                            password="adminpass",
                            host="db", port="5432")
    return conn

@app.route('/scooters/', methods=['GET'])
def list_scooters():
    """
    List all scooters in the database.
    """
    # Get a connection to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Execute a SQL query to fetch all scooters from the database
    cur.execute("SELECT id, name, battery_level FROM scooter")
    scooters = cur.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Convert the fetched data into a JSON format and return it
    return jsonify([{'id': s[0], 'name': s[1], 'battery_level': s[2]} for s in scooters])

@app.route('/scooters/', methods=['POST'])
def create_scooter():
    """
    Create a new scooter entry in the database.
    """
    # Check if the request contains valid JSON data with required fields
    if not request.json or 'name' not in request.json or 'battery_level' not in request.json:
        abort(400)  # Return a 400 Bad Request error if the data is invalid
    
    # Extract the name and battery_level from the request data
    name = request.json['name']
    battery_level = request.json['battery_level']
    
    # Get a connection to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Insert the new scooter data into the database and fetch the generated ID
    cur.execute("INSERT INTO scooter (name, battery_level) VALUES (%s, %s) RETURNING id", (name, battery_level))
    new_id = cur.fetchone()[0]
    
    # Commit the transaction to save the changes
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    # Return the created scooter data with a 201 Created status code
    return jsonify({'id': new_id, 'name': name, 'battery_level': battery_level}), 201

@app.route('/scooters/<int:id>', methods=['GET'])
def get_scooter(id):
    """
    Fetch a specific scooter by its ID from the database.
    """
    # Get a connection to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Execute a SQL query to fetch the scooter with the specified ID
    cur.execute("SELECT id, name, battery_level FROM scooter WHERE id = %s", (id,))
    scooter = cur.fetchone()
    
    # Close the database connection
    conn.close()
    
    # If the scooter is not found, return a 404 Not Found error
    if scooter is None:
        abort(404)
    
    # Return the fetched scooter data in JSON format
    return jsonify({'id': scooter[0], 'name': scooter[1], 'battery_level': scooter[2]})

@app.route('/scooters/<int:id>', methods=['PUT'])
def update_scooter(id):
    """
    Update the details of a specific scooter by its ID.
    """
    # Check if the request contains valid JSON data
    if not request.json:
        abort(400)  # Return a 400 Bad Request error if the data is invalid
    
    # Extract the name and battery_level from the request data, if they exist
    name = request.json.get('name')
    battery_level = request.json.get('battery_level')
    
    # Get a connection to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Update the scooter details in the database
    cur.execute("UPDATE scooter SET name = %s, battery_level = %s WHERE id = %s", (name, battery_level, id))
    
    # Commit the transaction to save the changes
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    # Return the updated scooter data in JSON format
    return jsonify({'id': id, 'name': name, 'battery_level': battery_level})

@app.route('/scooters/<int:id>', methods=['DELETE'])
def delete_scooter(id):
    """
    Delete a specific scooter by its ID from the database.
    """
    # Check for a custom header in the request to authenticate the delete operation
    password = request.headers.get('X-Delete-Password')
    if password != 'your_secret_password':  # Replace with your actual password
        return jsonify({"error": "Incorrect password"}), 401  # Return a 401 Unauthorized error if the password is incorrect
    
    # Get a connection to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Delete the scooter with the specified ID from the database
    cur.execute("DELETE FROM scooter WHERE id = %s", (id,))
    
    # Check if any rows were deleted
    if cur.rowcount == 0:  # No rows were deleted, implying scooter was not found
        conn.close()
        return jsonify({"error": "Electro Scooter not found"}), 404
    
    # Commit the transaction to save the changes
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    # Return a success message in JSON format
    return jsonify({"message": "Electro Scooter deleted successfully"}), 200

# Set up the Swagger UI for API documentation
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Electro Scooter API"
    }
)

# Register the Swagger UI blueprint with the Flask app
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def create_scooter_table_if_not_exists():
    """
    Create the scooter table in the database if it does not already exist.
    """
    # Get a connection to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Check if the scooter table exists in the database
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = 'scooter'
        );
    """)
    table_exists = cur.fetchone()[0]
    
    # If the table doesn't exist, create it
    if not table_exists:
        cur.execute("""
            CREATE TABLE scooter (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                battery_level INT NOT NULL
            );
        """)
        conn.commit()
    
    # Close the database connection
    conn.close()

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Create the scooter table if it doesn't exist
    create_scooter_table_if_not_exists()
    
    # Start the Flask web application
    app.run(host='0.0.0.0', debug=True)


