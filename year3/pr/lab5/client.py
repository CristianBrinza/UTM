import socket  # Import the socket module
import threading  # Import the threading module
import json  # Import the json module for JSON serialization
import os  # Import the os module for file handling
import base64  # Import the base64 module for file encoding

# Define server address and port
HOST = '127.0.0.1'
PORT = 6666

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set socket options to allow reusing the address
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Connect the socket to the server's address and port
client_socket.connect((HOST, PORT))

# Function to handle incoming messages from the server
def message_handler():
    while True:
        # Receive message from the server
        message = client_socket.recv(1024).decode('utf-8')
        # If message is empty, break the loop
        if not message:
            break
        # Deserialize the JSON message
        message = json.loads(message)
        # Check the type of message and display appropriate feedback
        if message['type'] == 'notification':
            print(f"\n[NOTIFICATION] {message['payload']['message']}\nYour message: ", end="")
        elif message['type'] == 'message':
            print(f"\n{message['payload']['sender']}: {message['payload']['text']}\nYour message: ", end="")
        elif message['type'] == 'file':
            # Save the received file
            save_file(message['payload']['file_name'], message['payload']['file_data'])
            print(f"\nFile {message['payload']['file_name']} has been downloaded.\nYour message: ", end="")

# Function to save a file received from the server
def save_file(file_name, file_data):
    # Define the path where files will be saved
    save_path = "CLIENT_MEDIA"
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

# Function to send a file to the server
def send_file(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Open and read the file
        with open(file_path, "rb") as file:
            file_data = file.read()
            # Encode the file data in base64
            encoded_file_data = base64.b64encode(file_data).decode('utf-8')
            # Extract the file name from the path
            file_name = os.path.basename(file_path)
            # Create a JSON message to send the file
            message = {
                "type": "file_upload",
                "payload": {
                    "file_name": file_name,
                    "file_data": encoded_file_data
                }
            }
            # Send the JSON message to the server
            client_socket.send(json.dumps(message).encode('utf-8'))
            print("\nFile has been sent!\nYour message: ", end="")
    else:
        print(f"\nFile {file_path} doesn't exist.\nYour message: ", end="")

# Start the message handler thread
client_thread = threading.Thread(target=message_handler)
# Set the thread as a daemon so it will end when the main program ends
client_thread.daemon = True
client_thread.start()

# Main loop to send messages and files
print("Welcome to the Chat Room!")
print("Type your messages below. To send a file, type 'upload:<path>'. To download a file, type 'download:<filename>'. To exit, type 'exit'.")
while True:
    # Take user input
    user_input = input("Your message: ")
    # Check if the input is an upload command
    if user_input.lower().startswith("upload:"):
        _, file_path = user_input.split(":", 1)
        send_file(file_path.strip())
    # Check if the input is a download command
    elif user_input.lower().startswith("download:"):
        _, file_name = user_input.split(":", 1)
        # Create a JSON message to request a file download
        message = {
            "type": "file_download",
            "payload": {
                "file_name": file_name.strip()
            }
        }
        # Send the JSON message to the server
        client_socket.send(json.dumps(message).encode('utf-8'))
    # Check if the input is an exit command
    elif user_input.lower() == 'exit':
        break
    else:
        # Create a JSON message to send a text message
        message = {
            "type": "message",
            "payload": {
                "text": user_input,
                "sender": "ClientName"  # Replace with actual client name
            }
        }
        # Send the JSON message to the server
        client_socket.send(json.dumps(message).encode('utf-8'))

# Close the socket when done
client_socket.close()
