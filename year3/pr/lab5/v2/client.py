import socket
import threading
import json
import base64
import os

# Server configuration
HOST = '127.0.0.1'
PORT = 6666

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((HOST, PORT))

# Function to handle incoming messages from the server
def message_handler():
    while True:
        # Receive message from the server
        message = client_socket.recv(1024).decode('utf-8')
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
    save_path = "CLIENT_MEDIA"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.join(save_path, file_name)
    decoded_file_data = base64.b64decode(file_data.encode('utf-8'))
    with open(file_path, "wb") as file:
        file.write(decoded_file_data)
    print(f"File saved at: {file_path}")

# Start the message handler thread
client_thread = threading.Thread(target=message_handler)
client_thread.daemon = True
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
    if user_input.lower() == 'exit':
        break
    elif user_input.lower().startswith("upload:"):
        _, file_path = user_input.split(maxsplit=1)
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                file_data = file.read()
                encoded_file_data = base64.b64encode(file_data).decode('utf-8')
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
    elif user_input.lower().startswith("download:"):
        _, file_name = user_input.split(maxsplit=1)
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
