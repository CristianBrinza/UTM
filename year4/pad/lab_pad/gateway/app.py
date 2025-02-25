from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    print("Gateway Service Status Check: Running")
    return jsonify({"status": "Gateway is running"}), 200

@app.route('/register', methods=['POST'])
def register_service():
    service_data = request.get_json()
    print(f"Service Registered: {service_data['name']} at {service_data['address']}")
    return jsonify({"message": "Service registered successfully"}), 200

@app.route('/notification', methods=['POST'])
def notification():
    notification_data = request.get_json()
    print(f"Notification Sent: {notification_data['message']} to {notification_data['user_id']}")
    return jsonify({"message": "Notification sent"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
