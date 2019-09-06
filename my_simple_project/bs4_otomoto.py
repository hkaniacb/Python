import requests
import bs4
import io


def clean_text(s):
    return s.strip().replace("\n", "").replace("\r", "").replace(" ", "")


search_url = 'https://www.otomoto.pl/osobowe/audi/a4/od-2004/?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_no_accident%5D=1&\
       search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D='

result = requests.get(search_url)

cars_file = io.open('cars-search-data.txt', 'w', encoding="utf-8")
cars_file.write("cena;nazwa;rocznik;przebieg;silnik;paliwo;\n")

cars_html_data = bs4.BeautifulSoup(result.text, features="lxml")
pages_count = int(cars_html_data.select('.page')[-1].text)

print("total search pages = {}".format(pages_count))
for index in range(1, pages_count):
    result = requests.get("{}&page={}".format(search_url, index))
    current_page = bs4.BeautifulSoup(result.text, features='lxml')
    cars_search_page = current_page.select('article.offer-item')
    for car_item in cars_search_page:

        price = clean_text(car_item.find('span', class_='offer-price__number').text.strip())
        cars_file.write("{};".format(price))

        title = car_item.find('a', class_='offer-title__link').text.strip()
        cars_file.write("{};".format(title))

        params = car_item.find_all("li", class_='offer-item__params-item')
        for param in params:
            cars_file.write("{};".format(clean_text(param.text)))
        cars_file.write('\n')

cars_file.close()
