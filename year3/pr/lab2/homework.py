import json
import csv
import requests
from bs4 import BeautifulSoup


# ▒█▀▄▒█▀▄ lab. PR | FAF | FCIM | UTM | Fall 2023
# ░█▀▒░█▀▄ FAF-212 Cristian Brinza lab2 homework


print('')
print('▒█▀▄▒█▀▄  lab. PR | FAF | FCIM | UTM | Fall 2023')
print('░█▀▒░█▀▄  FAF-212 Cristian Brinza lab2 homework ')
print('')



# User-Agent Rotation: List of user agents to mimic different browsers.
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.3',
    # Add more user agents if needed
]

def fetch_web_content(product_url):
    """Fetches the content of the given URL."""
    # User-Agent Rotation: Select a user agent based on the hash of the URL.
    headers = {
        'User-Agent': USER_AGENTS[hash(product_url) % len(USER_AGENTS)]
    }
    try:
        # Error Handling: Catch network errors or invalid URLs.
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching URL {product_url}. Error: {e}")
        return None


def extract_owner_details(parsed_content):
    """Extracts the owner details from the parsed content."""
    owner_details = {}
    owner_section = parsed_content.find('dl', {'class': 'adPage__aside__stats__owner'})
    owner_details['Name'] = owner_section.find('a', {'class': 'adPage__aside__stats__owner__login buyer_experiment'}).text
    owner_details['On website since'] = owner_section.find('span').text
    last_update_section = owner_section.find_next('div')
    owner_details['Last Update'] = last_update_section.text
    ad_type_section = last_update_section.find_next('div')
    owner_details['Ad type'] = ad_type_section.text
    views_section = ad_type_section.find_next('div')
    owner_details['Views'] = views_section.text
    return owner_details


def extract_product_info(parsed_content):
    """Extracts product information from the parsed content."""
    product_info = {}
    description_section = parsed_content.find('div', {'class': 'adPage__content__description grid_18'})
    product_info['Description'] = description_section.text
    features_section = parsed_content.find('div', {'class': 'adPage__content__features'}).find_all('h2')
    for feature in features_section:
        feature_details = {}
        ul_section = feature.find_next('ul')
        if ul_section:
            list_items = ul_section.find_all('li')
            for item in list_items:
                spans = item.find_all('span')
                if len(spans) == 2:
                    feature_details[spans[0].text] = spans[1].text
                else:
                    feature_details[spans[0].text] = 'None'
        product_info[feature.text] = feature_details
    return product_info


def export_to_csv(filename, data_list):
    """Exports the scraped data to a CSV file."""
    # Export to CSV: Write the scraped data into a CSV format.
    keys = data_list[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)


def read_urls_from_file(filename):
    """Reads URLs from a given file."""
    with open(filename, 'r') as file:
        return [url.strip() for url in file.readlines()]


def main():
    """Main function to interact with the user and perform operations."""
    all_data = []

    while True:
        print("\n--- Menu ---")
        print("1. Scrape product details")
        print("2. Scrape product details from a .txt file")
        print("3. Export all scraped data")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Scrape Multiple URLs: Allow user to input multiple URLs separated by commas.
            target_urls = input("Enter the product URLs (comma-separated): ").split(',')
            for url in target_urls:
                parsed_content = fetch_web_content(url.strip())
                if parsed_content:
                    owner_details = extract_owner_details(parsed_content)
                    product_info = extract_product_info(parsed_content)

                    final_data = {
                        'URL': url,
                        'Owner Details': owner_details,
                        'Product Info': product_info
                    }
                    all_data.append(final_data)
                    print(f"Scraped data for {url}")

        elif choice == "2":
            # Scrape URLs from a .txt file
            file_path = input("Enter the path to the .txt file containing the product URLs (without extension): ")+".txt"
            try:
                target_urls = read_urls_from_file(file_path)
                for url in target_urls:
                    parsed_content = fetch_web_content(url)
                    if parsed_content:
                        owner_details = extract_owner_details(parsed_content)
                        product_info = extract_product_info(parsed_content)

                        final_data = {
                            'URL': url,
                            'Owner Details': owner_details,
                            'Product Info': product_info
                        }
                        all_data.append(final_data)
                        print(f"Scraped data for {url}")
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found!")

        elif choice == "3":
            print("\n--- Export Options ---")
            print("1. JSON")
            print("2. TXT")
            print("3. CSV")
            print('4. Console')
            export_choice = input("Enter your choice: ")



            if export_choice == "1":
                filename = input("Enter filename (without extension): ")
                with open(f"{filename}.json", "w") as outfile:
                    outfile.write(json.dumps(all_data, indent=2, ensure_ascii=False))
                print(f"Data saved to {filename}.json")
            elif export_choice == "2":
                filename = input("Enter filename (without extension): ")
                with open(f"{filename}.txt", "w") as outfile:
                    outfile.write(json.dumps(all_data, indent=2, ensure_ascii=False))
                print(f"Data saved to {filename}.txt")
            elif export_choice == "3":
                filename = input("Enter filename (without extension): ")
                # Export to CSV: Save the scraped data into a CSV file.
                export_to_csv(f"{filename}.csv", all_data)
                print(f"Data saved to {filename}.csv")
            elif export_choice == "4":
                print(json.dumps(final_data, indent=2, ensure_ascii=False))  # Print the scraped data to console

            else:
                print("Invalid choice!")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
