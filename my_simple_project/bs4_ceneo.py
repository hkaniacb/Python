import requests
import bs4
import io
from pip._vendor.distro import cached_property


def clean_text(s):
    return s.strip().replace("\n", "").replace("\r", "").replace(" ", "")

search_url = 'https://www.ceneo.pl/51555235'

result = requests.get(search_url)

cars_html_data = bs4.BeautifulSoup(result.text, features="lxml") # pobranie całego html
current_page = cars_html_data

cars_search_page = current_page.select("tr.product-offer")

print(cars_search_page)
for car_item in cars_search_page:
    price = clean_text(car_item.find('span', class_='price').text.strip())
    name_product = car_item.find('span', class_='short-name__txt').text.strip()
    nazwa = car_item.find('img')['alt']
    print(price, name_product,nazwa)

    # splitowanie stringa i wrzucenie go listy 
nr_produktu = "https://www.ceneo.pl/20718474".split('/')
nr_last_item = len(nr_produktu)-1 # odwołanie się na ostaniegi elementu listy 
print(nr_produktu[nr_last_item]) # wyświetlenie ostani element listy 
