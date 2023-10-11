import socket  # Import the socket module to enable TCP/IP socket connections.
import threading  # Import the threading module to manage threads for handling multiple processes concurrently.
import json  # Import the json module to encode and decode messages in JSON format.
import base64  # Import the base64 module to encode and decode binary data.
import os  # Import the os module to interact with the operating system, e.g., file handling.

# Server configuration
HOST = '127.0.0.1'  # Define the IP address of the server.
PORT = 6666  # Define the port number to use for the socket connection.

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the server's address and port
client_socket.connect((HOST, PORT))

# Function to handle incoming messages from the server
def message_handler():
    while True:
        # Receive message from the server
        message = client_socket.recv(1024).decode('utf-8')
        # If message is empty, server has closed the connection
        if not message:
            print("\nConnection closed by the server.")
            break
        # Deserialize the JSON message
        message = json.loads(message)
        # Handle different types of messages
        if message['type'] == 'notification':
            print(f"\n[Server Notification]: {message['payload']['message']}")
        elif message['type'] == 'message':
            print(f"\n[{message['payload']['sender']}]: {message['payload']['text']}")
        elif message['type'] == 'file':
            save_file(message['payload']['file_name'], message['payload']['file_data'])
            print(f"\n[File Received]: {message['payload']['file_name']}")

# Function to save a received file
def save_file(file_name, file_data):
    save_path = "CLIENT_MEDIA"  # Define the path to save received files.
    # Check if save path exists, if not, create it
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # Define the full path to save the file
    file_path = os.path.join(save_path, file_name)
    # Decode the file data and save it
    decoded_file_data = base64.b64decode(file_data.encode('utf-8'))
    with open(file_path, "wb") as file:
        file.write(decoded_file_data)
    print(f"File saved at: {file_path}")

# Start the message handler thread
client_thread = threading.Thread(target=message_handler)
client_thread.daemon = True  # Set the thread as a daemon so it ends when the main program ends
client_thread.start()

# Get user name and room name for the chat
user_name = input("Enter your name: ")
room_name = input("Enter room name: ")

# Send connection message to the server
connect_message = {
    "type": "connect",
    "payload": {
        "name": user_name,
        "room": room_name
    }
}
client_socket.send(json.dumps(connect_message).encode('utf-8'))

# Main loop to handle user input and sending messages
while True:
    user_input = input()
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        break
    # Check if user wants to upload a file
    elif user_input.lower().startswith("upload:"):
        _, file_path = user_input.split(maxsplit=1)
        # Check if file exists
        if os.path.exists(file_path):
            # Read and encode the file data
            with open(file_path, "rb") as file:
                file_data = file.read()
                encoded_file_data = base64.b64encode(file_data).decode('utf-8')
                # Create and send file message
                file_message = {
                    "type": "file_upload",
                    "payload": {
                        "file_name": os.path.basename(file_path),
                        "file_data": encoded_file_data
                    }
                }
                client_socket.send(json.dumps(file_message).encode('utf-8'))
                print("\nUploading file...")
        else:
            print("\nFile does not exist.")
    # Check if user wants to download a file
    elif user_input.lower().startswith("download:"):
        _, file_name = user_input.split(maxsplit=1)
        # Create and send download request message
        download_message = {
            "type": "file_download",
            "payload": {
                "file_name": file_name.strip()
            }
        }
        client_socket.send(json.dumps(download_message).encode('utf-8'))
        print("\nRequesting file download...")
    else:
        # Send text message to the server
        text_message = {
            "type": "message",
            "payload": {
                "text": user_input,
                "sender": user_name,
                "room": room_name
            }
        }
        client_socket.send(json.dumps(text_message).encode('utf-8'))

# Close the client socket when done
client_socket.close()
