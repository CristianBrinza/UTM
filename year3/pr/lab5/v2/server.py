import socket  # Import the socket module for network communication
import threading  # Import the threading module for concurrent execution
import json  # Import the json module for JSON serialization and deserialization
import os  # Import the os module for file and directory operations
import base64  # Import the base64 module for encoding binary data

# Define server address and port
HOST = '127.0.0.1'
PORT = 6666

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the server's address and port
server_socket.bind((HOST, PORT))
# Listen for incoming connections
server_socket.listen()

# List to keep track of connected clients
server_clients = []

# Function to handle a client's messages
def client_handler(client_socket, client_address):
    print(f"\nAccepted connection from {client_address}")
    while True:
        # Receive message from the client
        client_message = client_socket.recv(1024).decode('utf-8')
        # If message is empty, break the loop
        if not client_message:
            break
        # Deserialize the JSON message
        message = json.loads(client_message)
        # Check the type of message and handle accordingly
        if message['type'] == 'file_upload':
            # Save the received file and get the file path
            file_path = save_file(message['payload']['file_name'], message['payload']['file_data'])
            # Create a notification message
            notification = {
                "type": "notification",
                "payload": {
                    "message": f"A file has been uploaded: {file_path}"
                }
            }
            print(f"\nFile uploaded by {client_address}: {file_path}")
        elif message['type'] == 'file_download':
            # Create the full file path
            file_path = os.path.join("SERVER_MEDIA", message['payload']['file_name'])
            # Check if the file exists
            if os.path.exists(file_path):
                # Open and read the file
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    # Encode the file data in base64
                    encoded_file_data = base64.b64encode(file_data).decode('utf-8')
                    # Create a JSON message to send the file
                    file_message = {
                        "type": "file",
                        "payload": {
                            "file_name": message['payload']['file_name'],
                            "file_data": encoded_file_data
                        }
                    }
                    # Send the JSON message to the client
                    client_socket.send(json.dumps(file_message).encode('utf-8'))
                print(f"\nFile downloaded by {client_address}: {file_path}")
            else:
                # Create a notification message for file not found
                notification = {
                    "type": "notification",
                    "payload": {
                        "message": f"The file {message['payload']['file_name']} does not exist on the server."
                    }
                }
                # Send the JSON message to the client
                client_socket.send(json.dumps(notification).encode('utf-8'))
                print(f"\nFile download failed for {client_address}: File does not exist.")
        elif message['type'] == 'message':
            # Create a message to broadcast to all clients
            notification = {
                "type": "message",
                "payload": message['payload']
            }
            print(f"\nMessage from {client_address}: {message['payload']['text']}")
        else:
            # Ignore other message types
            continue
        # Broadcast the message/notification to all connected clients
        for client in server_clients:
            client.send(json.dumps(notification).encode('utf-8'))
    print(f"\nConnection from {client_address} closed")
    # Remove the client from the list and close the socket
    server_clients.remove(client_socket)
    client_socket.close()

# Function to save a file received from a client
def save_file(file_name, file_data):
    # Define the path where files will be saved
    save_path = "SERVER_MEDIA"
    # Create the directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # Create the full file path
    file_path = os.path.join(save_path, file_name)
    # Decode the base64 encoded file data
    decoded_file_data = base64.b64decode(file_data.encode('utf-8'))
    # Write the decoded data to a file
    with open(file_path, "wb") as file:
        file.write(decoded_file_data)
    return file_path

# Main loop to accept new clients
print("Server is running...")
while True:
    # Accept a new client connection
    client_socket, client_address = server_socket.accept()
    # Add the client to the list
    server_clients.append(client_socket)
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
    client_thread.start()
