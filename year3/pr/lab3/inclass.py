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

with open('products.json', 'r') as f:
    products = json.load(f)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received request for path: {self.path}")

        if self.path == '/':
            self._send_page(content=b"Home Page")
            return

        if self.path == '/about':
            self._send_page(content=b"About Us Page")
            return

        if self.path == '/contacts':
            self._send_page(content=b"Contacts Page")
            return

        if self.path == '/products':
            product_links = [f"<li><a href='/product/{i}'>{product['name']}</a></li>" for i, product in enumerate(products)]
            content = f"<ul>{''.join(product_links)}</ul>".encode()
            self._send_page(content=content)
            return

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

        self._send_page(status_code=404, content=b"404 Not Found")
        return

    def _send_page(self, status_code=200, content_type="text/html", content=b""):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(content)
        print(f"Responded with status: {status_code}")
        print("--------------------------------------")


with socketserver.TCPServer(("localhost", 8081), MyHttpRequestHandler) as httpd:
    httpd.serve_forever()


