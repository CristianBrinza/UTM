import socket
import re

def establish_tcp_connection(path):
    #Establish a TCP connection and retrieve content from the specified path.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 8081))
        headers = {
            "Host": "localhost",
            "User-Agent": "TCP_Parser/1.0"
        }
        headers_str = "\r\n".join(f"{k}: {v}" for k, v in headers.items())
        request = f"GET {path} HTTP/1.1\r\n{headers_str}\r\n\r\n"
        s.sendall(request.encode())
        response = s.recv(4096).decode()
        return response.split("\r\n\r\n", 1)[-1]  # Return only the content, excluding headers

def extract_product_links(content):
    return re.findall(r"href='/product/(\d+)'", content)

def parse_product_details(content):
    details = {}
    patterns = {
        "name": r"<h1>(.*?)</h1>",
        "description": r"<p>(.*?)</p>",
        "price": r"Price: \$(\d+\.\d+)"
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            if key == "price":
                details[key] = float(match.group(1))
            else:
                details[key] = match.group(1)
    return details if details else None

def main():
    # Get product listing page
    product_listing_content = establish_tcp_connection('/products')
    product_links = extract_product_links(product_listing_content)

    # Parse each product page
    for product_id in product_links:
        product_content = establish_tcp_connection(f'/product/{product_id}')
        product_details = parse_product_details(product_content)
        if product_details:
            print(product_details)
        else:
            print(f"Failed to parse details for product ID: {product_id}")

if __name__ == "__main__":
    main()
