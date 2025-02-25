from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import pybreaker
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Circuit Breaker configuration
circuit_breaker = pybreaker.CircuitBreaker(
    fail_max=3,  # Fail after 3 failures
    reset_timeout=10  # Reset after 10 seconds
)

events = []

@app.route('/events/create', methods=['POST'])
def create_event():
    data = request.json
    event = {
        "title": data.get('title'),
        "description": data.get('description'),
        "date": data.get('date')
    }

    # Try to create an event with Circuit Breaker
    try:
        with circuit_breaker:
            # Simulating a failure for demonstration purposes
            if len(events) >= 3:  # Simulate failure after 3 attempts
                raise Exception("Simulated failure")

            events.append(event)
            print(f"Event created: {event}")
            socketio.emit('event_created', {'event': event})
            return jsonify({"message": "Event created successfully"}), 201

    except pybreaker.CircuitBreakerError:
        print("Circuit Breaker: Service is currently unavailable.")
        return jsonify({"error": "Service is currently unavailable"}), 503

    except Exception as e:
        print(f"Error creating event: {str(e)}")
        return jsonify({"error": "Failed to create event"}), 500

@app.route('/events/list', methods=['GET'])
def list_events():
    print(f"Listing events: {events}")
    return jsonify({"events": events})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Event Service is running"}), 200

@socketio.on('connect')
def handle_connect():
    print('Client connected to Event Service')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected from Event Service')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=50051)
