# Basic Chat Application with File Transfer

## Overview
This project implements a basic chat application using Python and sockets. The application allows multiple clients to connect to a server, join a chat room, send messages, and share files (.txt and images) with other clients in the same room. The communication between clients and the server is facilitated using a JSON-based protocol.

## Features
- **Multi-Client Communication**: Supports multiple clients to communicate simultaneously.
- **File Transfer**: Allows clients to upload and download files (.txt and images).
- **User Identification**: Clients are identified by user names in the chat.
- **Visual Feedback**: Provides visual feedback for chat interactions and file transfers.
- **JSON Protocol**: Utilizes a JSON-based communication protocol for message exchange.

## How It Works

### 1. Server-Client Architecture
- **Server**: Listens for incoming client connections, handles client messages, manages chat rooms, and facilitates communication between clients.
- **Client**: Connects to the server, sends and receives messages, and handles file uploads and downloads.

### 2. Communication Protocol
- **Connect**: Clients send a "connect" message with their name and desired room name upon connecting.
- **Message**: Clients send messages using a "message" type, and the server broadcasts these messages to all clients in the same room.
- **File Upload/Download**: Clients can upload and download files using specific commands and JSON message types for file transfer.

### 3. File Transfer Mechanism
- **Upload**: Clients read, encode (using Base64), and send file data to the server, which decodes and saves the file.
- **Download**: Clients request a file, and the server sends the encoded file data, which the client then decodes and saves.

### 4. Threading
- **Server**: Uses threading to handle multiple clients simultaneously.
- **Client**: Uses threading to handle incoming messages independently of user input.

## Usage

### Running the Server
```bash
python server.py
```
The server will start listening for incoming connections on the specified IP address and port.

### Running the Client

```bash
python client.py
```

Clients will be prompted to enter their name and desired chat room. They can then send messages and use file transfer commands.

Sending a File
```
upload: <path_to_file>
```
Clients can upload a file by specifying the file path. The file data is sent to the server and made available for download by other clients.

Downloading a File
```
download: <file_name>
```
Clients can download a file by specifying the file name. The server sends the file data to the client, which is then saved.

### Challenges and Solutions
Challenge: Managing multiple clients and ensuring smooth communication.
Solution: Implemented threading to handle multiple clients and manage communication independently.

Challenge: Ensuring safe and accurate file transfers.

Solution: Used Base64 encoding for file data and implemented a JSON-based protocol for structured communication.

### Future Improvements
Implementing user authentication for enhanced security.
Adding support for more file types and larger file transfers.
Implementing additional error handling and user notifications.
Enhancing the user interface for a better user experience.
Conclusion
This basic chat application demonstrates the fundamentals of socket programming, multi-client communication, and file transfer in Python. It provides a foundation for building more robust and feature-rich chat applications in the future.



### Acknowledgements
Inspired by the lab guidelines and this GitHub repository.
sql
Copy code

### Notes:
- Replace `[Your Name]` with your actual name.
- You may add or modify sections as per your project details and requirements.
- Ensure to test all functionalities and validate the code against various scenarios to confirm its robustness and reliability.
- You might want to add a "Dependencies" section if your project requires external libraries or modules.
- If you have any additional features or specific implementation details, consider adding them to the "How It Works" or "Features" section.



