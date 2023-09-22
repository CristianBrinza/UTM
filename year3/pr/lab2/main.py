import requests
from bs4 import BeautifulSoup

base_url = "https://999.md/ro/list/transport/cars"
all_links = []
links=[]
bost = "booster"



def get_links_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    car_links = [a['href'] for a in soup.select('a.js-item-ad')]
    return car_links

all_links.append(get_links_from_page(base_url))


while True:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    next_page = soup.select_one('is-last-page')
    if next_page:
        base_url = next_page['href']
        all_links.append(get_links_from_page(base_url))

    else:
        break


for a in all_links:
    for b in a:
        if "booster"not in b:
            links.append("https://999.md/"+b)
all_links = list(set(links))
print(all_links)

