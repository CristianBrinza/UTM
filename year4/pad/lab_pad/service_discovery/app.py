from flask import Flask, request, jsonify

app = Flask(__name__)

services = {}

@app.route('/register', methods=['GET'])
def register_service():
    name = request.args.get('name')
    address = request.args.get('address')
    services[name] = address
    print(f"Service {name} registered at {address}")
    return jsonify({"message": f"Service {name} registered at {address}"}), 200

@app.route('/get', methods=['GET'])
def get_service():
    name = request.args.get('name')
    if name in services:
        print(f"Service found: {name} at {services[name]}")
        return jsonify({"address": services[name]})
    print(f"Service {name} not found")
    return jsonify({"error": "Service not found"}), 404

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Service Discovery is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
