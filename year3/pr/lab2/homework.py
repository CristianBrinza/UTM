import json
import requests
from bs4 import BeautifulSoup

def fetch_web_content(product_url):
    """Fetches the content of the given URL."""
    response = requests.get(product_url)
    return BeautifulSoup(response.content, 'html.parser')


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


def main():
    """Main function to interact with the user and perform operations."""
    while True:
        print("\n--- Menu ---")
        print("1. Scrape product details")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            target_url = input("Enter the product URL: ")
            parsed_content = fetch_web_content(target_url)
            owner_details = extract_owner_details(parsed_content)
            product_info = extract_product_info(parsed_content)

            final_data = {
                'Owner Details': owner_details,
                'Product Info': product_info
            }

            print("\n--- Output Options ---")
            print("1. Display on console")
            print("2. Write to file")
            output_choice = input("Enter your choice: ")

            if output_choice == "1":
                print("\nScraped Data:")
                print(final_data)
            elif output_choice == "2":
                filename = input("Enter filename (default: storage.txt): ")
                if not filename:
                    filename = "storage.txt"
                with open(filename, "w") as outfile:
                    outfile.write(json.dumps(final_data, indent=2, ensure_ascii=False))
                print(f"Data saved to {filename}")
            else:
                print("Invalid choice!")

        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()
