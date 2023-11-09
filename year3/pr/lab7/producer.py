# Import the pika library to interact with RabbitMQ
import pika
# Import the requests library to make HTTP requests
import requests
# Import BeautifulSoup from bs4 to parse HTML content
from bs4 import BeautifulSoup
# Import the time library for sleep functionality
import time

# Function to establish a connection with RabbitMQ server
def establish_connection(retries=5, delay=5, host='rabbitmq', port=5672):
    # Initialize a variable to keep track of the last exception
    last_exception = None
    # Attempt to connect multiple times based on the retries parameter
    for attempt in range(retries):
        try:
            # Attempt to create a blocking connection with the given host and port
            return pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        except pika.exceptions.AMQPConnectionError as error:
            # Print the error if connection attempt fails
            print(f"Connection attempt {attempt + 1} failed: {error}")
            # Store the last exception to raise later if needed
            last_exception = error
            # Wait for a specified delay before retrying
            time.sleep(delay)
    # If all retries fail, raise the last exception
    raise last_exception

# Define the RabbitMQ server host and queue name
rabbitmq_server = 'rabbitmq'
queue_identifier = 'url_queue'
# Establish connection to RabbitMQ using the function above
rabbitmq_connection = establish_connection()
# Create a channel on the connection
communication_channel = rabbitmq_connection.channel()
# Declare a queue on the channel, which will be durable (survives broker restart)
communication_channel.queue_declare(queue=queue_identifier, durable=True)

# Recursive function to crawl URLs and send them to the RabbitMQ queue
def crawl_urls(max_depth, current_depth, urls_to_visit, collected_urls, channel, queue):
    # Base case: stop if the current depth exceeds the max depth or the list of URLs
    if current_depth >= len(urls_to_visit) or current_depth >= max_depth:
        print(f"Total URLs collected: {len(collected_urls)}")
        return

    # Get the current URL to process
    current_url = urls_to_visit[current_depth]
    try:
        # Fetch the content of the URL using HTTP GET request
        response = requests.get(current_url)
        # Parse the HTML content of the page
        html_parser = BeautifulSoup(response.content, "html.parser")

        # Loop through all anchor tags with a specific class to find product URLs
        for anchor in html_parser.find_all('a', href=True, class_='js-item-ad'):
            # Construct the full URL by appending the href attribute to the base URL
            complete_url = f"https://999.md{anchor.get('href')}"
            # Add the URL to the set if it's not already present to avoid duplicates
            if complete_url not in collected_urls:
                collected_urls.add(complete_url)
                # Publish the URL to the specified RabbitMQ queue
                channel.basic_publish(exchange='', routing_key=queue, body=complete_url)
                print(f"Dispatched URL to queue: {complete_url}")

        # Look for additional pages to crawl by finding pagination links
        for pagination_link in html_parser.select('nav.paginator > ul > li > a'):
            # Construct the full URL for the new page
            next_page_url = f"https://999.md{pagination_link.get('href')}"
            # Add the new page URL to the list if it's not already there
            if next_page_url not in urls_to_visit:
                urls_to_visit.append(next_page_url)

        # Recursively call the function to process the next URL
        crawl_urls(max_depth, current_depth + 1, urls_to_visit, collected_urls, channel, queue)

    except requests.RequestException as e:
        # Print an error message if the URL fetch fails
        print(f"Error fetching URL {current_url}: {str(e)}")

# Set of URLs that have been collected
discovered_urls = set()
# The initial URL from which the crawling will start
initial_url = "https://999.md/                                        "
# Start the recursive crawling process with an arbitrarily large max depth
crawl_urls(100000000, 0, [initial_url], discovered_urls, communication_channel, queue_identifier)

# Close the RabbitMQ connection after the crawling process is complete
rabbitmq_connection.close()
