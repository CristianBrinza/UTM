# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab7


print('')
print('▒█▀▄▒█▀▄  lab. PR | FAF | FCIM | UTM | Fall 2023')
print('░█▀▒░█▀▄  FAF-212 Cristian Brinza lab7  ')
print('')

# Import necessary libraries
import requests  # Used for making HTTP requests
from bs4 import BeautifulSoup  # Used for parsing HTML content
import pika  # Used for interacting with RabbitMQ for message queuing
from tinydb import TinyDB  # TinyDB is a lightweight database to store data

# Initialize a TinyDB database to store extracted information
db = TinyDB("database.json")

def get_html_content(url):
    """
    Fetch HTML content from a URL.

    Args:
    url (str): The URL from which to fetch the content.

    Returns:
    BeautifulSoup object: Parsed HTML content of the page.
    """
    response = requests.get(url)  # Send a GET request to the URL
    return BeautifulSoup(response.content, "html.parser")  # Parse the content of the page

def parse_html_content(soup, url):
    """
    Parse specific elements from HTML and return them in a dictionary.

    Args:
    soup (BeautifulSoup): Parsed HTML content of a page.
    url (str): The URL of the page being processed.

    Returns:
    dict: A dictionary containing extracted elements like title, price, etc.
    """
    result = {"URL": url}  # Initialize a dictionary with the URL

    # Define a dictionary where keys are attributes we want to extract (like Title, Price),
    # and values are tuples containing the tag name and attribute for BeautifulSoup to find.
    for attr, selector in {
        "Title": ("h1", {"itemprop": "name"}),
        "Price": ("span", {"class": "adPage__content__price-feature__prices__price__value"}),
        "Location": ("strong", {"class": "adPage__content__region"}),
        "Description": ("div", {"itemprop": "description"})
    }.items():
        element = soup.find(*selector)  # Use BeautifulSoup to find the element
        if element:  # If the element is found
            result[attr] = element.get_text(strip=True)  # Extract and store its text content

    # Extract currency separately and append it to price if available
    currency = soup.find("span", itemprop="priceCurrency")
    if currency and "Price" in result:
        result["Price"] += f" {currency.get('content', '').strip()}"

    return result

def process_message(channel, method, properties, body):
    """
    Callback function to process each message received from the queue.

    Args:
    channel: The channel object.
    method: Provides delivery information.
    properties: Message properties.
    body: The message body (content).
    """
    url = body.decode()  # Decode the message body to get the URL
    print(f"[INFO] Processing URL: {url}")  # Log information

    try:
        soup = get_html_content(url)  # Get the HTML content of the page
        data = parse_html_content(soup, url)  # Parse the HTML content to get required data
        db.insert(data)  # Insert the data into the database
        print(f"[SUCCESS] Data inserted for URL: {url}")
    except Exception as e:
        print(f"[ERROR] Failed to process URL {url}: {e}")  # Log any errors
    finally:
        channel.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message processing

def start_message_queue_consumer():
    """
    Initialize and start the message queue consumer to process incoming messages.
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))  # Connect to the RabbitMQ server
    channel = connection.channel()  # Create a channel
    channel.queue_declare(queue="url_queue")  # Declare a queue named 'url_queue'

    # Tell RabbitMQ that this function `process_message` is the callback function for the queue
    channel.basic_consume(queue="url_queue", on_message_callback=process_message, auto_ack=False)
    print("[*] Queue Consumer is running. Press CTRL+C to exit.")
    channel.start_consuming()  # Start consuming (receiving) messages from the queue

# The following line checks if this script is the main program and is not being imported as a module in another script.
if __name__ == "__main__":
    start_message_queue_consumer()  # If it is the main program, start the message queue consumer
