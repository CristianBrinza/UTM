# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab7


print('')
print('▒█▀▄▒█▀▄  lab. PR | FAF | FCIM | UTM | Fall 2023')
print('░█▀▒░█▀▄  FAF-212 Cristian Brinza lab7  ')
print('')


# Import necessary libraries
import requests  # Used for making HTTP requests to web pages
from bs4 import BeautifulSoup  # Used for parsing HTML content
import pika  # RabbitMQ library for Python
from termcolor import colored  # Library to add color to console output


# Function to display a simple start-up banner
def display_banner():
    """Displays a simple banner at the start of the script."""
    # Print a colored message to the console
    print(colored("Starting URL Scraper and Queue Sender", "green"))


# Function to set up a RabbitMQ connection and declare a queue
def setup_rabbitmq():
    """Set up RabbitMQ connection and channel."""
    # Connect to RabbitMQ server running on localhost
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # Create a channel on this connection
    channel = connection.channel()
    # Declare a queue named 'url_queue' on this channel
    channel.queue_declare(queue='url_queue')
    # Print a status message
    print(colored("RabbitMQ Setup Complete", "blue"))
    # Return the created connection and channel
    return connection, channel


# Function to send a URL to the RabbitMQ queue
def send_url_to_queue(channel, url):
    """Send a URL to the RabbitMQ queue."""
    # Publish a message (URL) to the 'url_queue'
    channel.basic_publish(exchange='', routing_key='url_queue', body=url)
    # Print a status message for each URL sent
    print(colored(f"URL Sent to Queue: {url}", "yellow"))


# Function to parse a URL and enqueue new links found
def parse_and_enqueue_links(url, channel):
    """Parse given URL and enqueue new links found."""
    # Make an HTTP GET request to the URL
    response = requests.get(url)
    # Parse the content of the request using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Loop through all 'a' tags with 'href' attribute and 'js-item-ad' class
    for link in soup.find_all('a', href=True, class_='js-item-ad'):
        href = link.get('href')
        # Check if href is valid and doesn't start with 'b'
        if href and href[1] != 'b':
            # Construct the full URL
            full_url = f"https://999.md{href}"
            # Send the URL to the RabbitMQ queue
            send_url_to_queue(channel, full_url)

    # Return a list of new URLs from the page's pagination section
    return [f"https://999.md{a.get('href')}" for a in soup.select('nav.paginator > ul > li > a') if a.get('href')]


# Recursive function for crawling URLs
def recursive_crawl(max_iterations, current_iteration, urls, channel):
    """Recursively crawl URLs up to a maximum number of iterations."""
    # Check if the maximum iterations or URL list length is reached
    if current_iteration >= max_iterations or current_iteration >= len(urls):
        return

    # Print the current URL being processed
    print(colored(f"Processing URL {current_iteration + 1}/{len(urls)}: {urls[current_iteration]}", "cyan"))
    # Parse and enqueue links from the current URL
    new_urls = parse_and_enqueue_links(urls[current_iteration], channel)
    # Loop through the new URLs and add them to the list if not already present
    for new_url in new_urls:
        if new_url not in urls:
            urls.append(new_url)

    # Recursively call the function with the next URL
    recursive_crawl(max_iterations, current_iteration + 1, urls, channel)


# Main execution block
if __name__ == "__main__":
    # Display the start-up banner
    display_banner()
    # Initial list of URLs to crawl
    initial_urls = ["https://999.md/ro/list/real-estate/house-and-garden?o_38_249=1644&applied=1&eo=12900&eo=12912&eo=12885&eo=13859&ef=40&ef=41&o_41_1=776"]
    # Set up RabbitMQ connection and channel
    connection, channel = setup_rabbitmq()

    try:
        # Start the recursive crawling process
        recursive_crawl(1000000, 0, initial_urls, channel)
    finally:
        # Close the RabbitMQ connection when done
        connection.close()
        # Print a message indicating the closure of the connection
        print(colored("RabbitMQ Connection Closed", "red"))
