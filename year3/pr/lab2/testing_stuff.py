import requests
from bs4 import BeautifulSoup



url = 'https://999.md/ro/list/phone-and-communication/fitness-trackers'


def fetch_html(url):
    response = requests.get(url)
    return response.text

def extract_links_from_pagination(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('nav.paginator > ul > li > a')
    '''
    soup = BeautifulSoup(response.content, 'html.parser')
    
        car_links = [a['href'] for a in soup.select('a.js-item-ad')]
        return car_links
    '''
    car_links = []
    for link in links:
        car_links.append('https://999.md' + link['href'])

    return car_links

'''
  all_links.append(get_links_from_page(base_url))
'''
def get_item_links(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    item_links = soup.select('a.js-item-ad')

    filtered_links = []
    for item_link in item_links:
        if 'booster' not in item_link['href']:
            new_link = 'https://999.md' + item_link['href']
            if new_link not in filtered_links:
                filtered_links.append(new_link)

    return filtered_links

def get_all_item_links(start_url):
    pagination_links = extract_links_from_pagination(start_url)

    all_item_links = []
    for pagination_link in pagination_links:
        item_links = get_item_links(pagination_link)
        all_item_links.extend(item_links)

    return all_item_links


print(len(get_all_item_links(url)))


'''

for a in all_links:
    for b in a:
        if "booster"not in b:
            links.append("https://999.md/"+b)
all_links = list(set(links))
print(all_links)


'''


