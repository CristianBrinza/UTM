import http.server
import socketserver
import json
import re



# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab3


print('')
print('▒█▀▄▒█▀▄  lab. PR | FAF | FCIM | UTM | Fall 2023')
print('░█▀▒░█▀▄  FAF-212 Cristian Brinza lab3 ')
print('')


# improving performance: This is done outside the request handler to ensure that the file is read only once


'''
The 'b' before the string creates a bytes object in Python. HTTP responses are typically sent as bytes, so this ensures the content is in the right format.

ex:     self._send_page(content=b"Home Page")

this is telling the server to send an HTTP response with the content "<<the text : ex:"Home Page" >>" to the client who made the request.
'''

# Read product data from a JSON file
with open('products.json', 'r') as f:
    products = json.load(f)


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Log the incoming request
        print(f"Received request for path: {self.path}")

        # Route for the home page
        if self.path == '/':
            self._send_page(content=b"Home Page")
            return

        # Route for the about page
        if self.path == '/about':
            self._send_page(content=b"About Us Page")
            return

        # Route for the contacts page
        if self.path == '/contacts':
            self._send_page(content=b"Contacts Page")
            return

        # Route to list all products with links to their detailed pages
        if self.path == '/products':
            product_links = [f"<li><a href='/product/{i}'>{product['name']}</a></li>" for i, product in enumerate(products)]
            content = f"<ul>{''.join(product_links)}</ul>".encode()
            self._send_page(content=content)
            return

        # Route for individual product details using regex for dynamic URL parsing
        match = re.match(r'/product/(\d+)', self.path)
        if match:
            product_id = int(match.group(1))
            if 0 <= product_id < len(products):
                product = products[product_id]
                content = f"<h1>{product['name']}</h1><p>{product['description']}</p><p>Price: ${product['price']}</p>".encode()
                self._send_page(content=content)
                return
            else:
                self._send_page(status_code=404, content=b"Product not found")
                return

        # If no routes match, return a 404 page
        self._send_page(status_code=404, content=b"404 Not Found")
        return

    def _send_page(self, status_code=200, content_type="text/html", content=b""):
        """
        Helper method to send a response with the given status code, content type, and content.
        """
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(content)
        # Log the response status
        print(f"Responded with status: {status_code}")
        print("--------------------------------------")
        # this i used to consolelog the actions performed for this lab



'''
    comments for future users
'''
# Create and start an HTTP server
# Using `localhost` ensures the server is only accessible from this machine.
# Port 8081 is used, but can be changed if needed.
# I have used this port because my 8080 was used for work
with socketserver.TCPServer(("localhost", 8081), MyHttpRequestHandler) as httpd:
    print("======================================")
    print("Welcome to Lab 3 : the Simple HTTP Server!")
    print("Serving at: http://localhost:8081")
    print("You can access the following routes:")
    print("- / (Home Page)")
    print("- /about (About Us Page)")
    print("- /contacts (Contacts Page)")
    print("- /products (List of Products)")
    print("- /product/<id> (Details of a specific product by its ID)")
    print("======================================")
    print("Waiting for incoming requests...")
    httpd.serve_forever()


