import socket
'''
    A TCP client is a software component or application that initiates a TCP (Transmission Control Protocol) 
    connection to a server to exchange data. TCP is one of the main protocols in the Internet protocol suite 
    and provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications 
    running on hosts communicating over an IP network.

'''
def tcp_client_request(path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 8081))
        request = f"GET {path} HTTP/1.1\r\nHost: localhost\r\n\r\n"
        s.sendall(request.encode())
        response = s.recv(4096)
        print(response.decode())

# Test the client
tcp_client_request('/')
tcp_client_request('/about')
tcp_client_request('/contacts')
tcp_client_request('/product/0')
