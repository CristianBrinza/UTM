# Importing necessary libraries
import pika  # Used for RabbitMQ messaging
import psycopg2  # PostgreSQL database adapter for Python
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML and XML documents
import json  # For JSON operations
import threading  # For running tasks on separate threads

# Function to extract information from a given URL
def extract_information(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the content of the page using BeautifulSoup
    page_soup = BeautifulSoup(response.content, "html.parser")
    # Initialize an empty dictionary to store the results
    result_data = {}

    # Extract the title of the product and add it to the dictionary
    product_title = page_soup.find('h1', itemprop='name')
    if product_title:
        result_data['Title'] = product_title.text.strip()

    # Extract the description of the product
    product_description = page_soup.find('div', itemprop='description')
    if product_description:
        result_data['Description'] = product_description.text.strip()

    # Extract the price and currency of the product
    product_price = page_soup.find('span', class_='price-value')
    product_currency = page_soup.find('span', itemprop='priceCurrency')
    if product_price:
        if 'negotiable' in product_price.text:
            result_data['Price'] = product_price.text.strip()
        else:
            result_data['Price'] = f"{product_price.text.strip()} {product_currency.get('content')}"

    # Extract the location information
    product_country = page_soup.find('meta', itemprop='addressCountry')
    product_locality = page_soup.find('meta', itemprop='addressLocality')
    if product_country and product_locality:
        result_data['Location'] = f"{product_locality.get('content')}, {product_country.get('content')}"

    # Extract additional advertisement information
    advertisement_info = {}
    ad_views = page_soup.find('div', class_='view-count')
    if ad_views:
        advertisement_info['Views'] = ad_views.text.strip()
    ad_date = page_soup.find('div', class_='update-date')
    if ad_date:
        advertisement_info['Update Date'] = ad_date.text.strip()
    ad_type = page_soup.find('div', class_='ad-type')
    if ad_type:
        advertisement_info['Ad Type'] = ad_type.text.strip()
    ad_owner = page_soup.find('a', class_='owner-name')
    if ad_owner:
        advertisement_info['Owner Username'] = ad_owner.text.strip()
    result_data['Ad Information'] = advertisement_info

    # Extract general information about the product
    general_info_section = page_soup.find('div', class_='general-info-section')
    general_info = {}
    list_items = general_info_section.find_all('li')
    for item in list_items:
        key_element = item.find('span', class_='info-key')
        value_element = item.find('span', class_='info-value')
        if key_element and value_element:
            info_key = key_element.text.strip()
            info_value = value_element.text.strip()
            general_info[info_key] = info_value
    result_data['General Information'] = general_info

    # Extract features of the product
    features_section = page_soup.find('div', class_='features-section')
    features_info = {}
    feature_items = features_section.find_all('li')
    for item in feature_items:
        feature_key_element = item.find('span', class_='feature-key')
        feature_value_element = item.find('span', class_='feature-value')
        if feature_key_element and feature_value_element:
            feature_key = feature_key_element.text.strip()
            feature_value = feature_value_element.text.strip()
            features_info[feature_key] = feature_value
    result_data['Features'] = features_info

    # Print the extracted information in JSON format for readability
    print(json.dumps(result_data, indent=4, ensure_ascii=False))

    # Return the dictionary containing all the extracted information
    return result_data

# Callback function to handle messages received from RabbitMQ
def message_handler(channel, method_frame, header_frame, body):
    # Decode the message body to get the URL
    received_url = body.decode()
    print(f"Processing URL: {received_url}")
    # Extract product information from the URL
    product_data = extract_information(received_url)
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(
            dbname="products_db",
            user="db_user",
            password="db_password",
            host="database_host"
        ) as connection:
            with connection.cursor() as cursor:
                # SQL query to insert product data into the database
                sql_insert_query = """
                INSERT INTO product_table (title, description, price, location, ad_information, general_information, features)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                # Execute the query with the product data
                cursor.execute(sql_insert_query, (
                    product_data.get('Title'),
                    product_data.get('Description'),
                    product_data.get('Price'),
                    product_data.get('Location'),
                    json.dumps(product_data.get('Ad Information')),
                    json.dumps(product_data.get('General Information')),
                    json.dumps(product_data.get('Features'))
                ))
            # Commit the transaction
            connection.commit()
        print(f"Data for {received_url} has been stored in the database.")
    except Exception as error:
        print(f"Database operation failed: {error}")
    finally:
        # Acknowledge the message so RabbitMQ can remove it from the queue
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

# Function to start a message consumer
def initiate_consumer():
    # Define the RabbitMQ server host
    rabbitmq_server = 'rabbitmq_server'
    # Define the queue name
    queue_name = 'product_urls'
    # Establish a connection to RabbitMQ
    rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_server))
    # Create a channel
    rabbitmq_channel = rabbitmq_connection.channel()
    # Declare a durable queue
    rabbitmq_channel.queue_declare(queue=queue_name, durable=True)
    # Specify the prefetch count for the consumer
    rabbitmq_channel.basic_qos(prefetch_count=1)
    # Start consuming messages from the queue using the callback function
    rabbitmq_channel.basic_consume(queue=queue_name, on_message_callback=message_handler)
    print('Consumer is active. Press CTRL+C to stop.')
    # Start the consuming process
    rabbitmq_channel.start_consuming()

# Define the number of consumer threads
number_of_consumers = 5  # Adjust this number based on the desired concurrency

# Create and start consumer threads
for index in range(number_of_consumers):
    thread = threading.Thread(target=initiate_consumer)
    thread.start()
    print(f"Consumer thread {index + 1} has started.")

print(f"{number_of_consumers} consumer threads are now active.")
