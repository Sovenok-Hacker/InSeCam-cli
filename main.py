import requests
from bs4 import BeautifulSoup as BS
country = input('Country code :> ')
data = requests.get(f'http://www.insecam.org/en/bycountry/{country}/', headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'}).content.decode()
soup = BS(data, 'lxml')
log = open(f'cameras_{country}.txt', 'w')
pages_count = int(str(soup.find('ul', class_='pagination')).splitlines()[2].split(',')[1].split(',')[0][1:])
for i in range(0, pages_count):
    print(f'[INFO] Page: {i}')
    data = requests.get(f'http://www.insecam.org/en/bycountry/{country.upper()}/?page={i}', headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'}).content.decode()
    soup = BS(data, 'lxml')
    for camera in soup.find_all(class_='thumbnail-item__img img-responsive'):
        log.write(camera.get('src') + '\n')
        print(camera.get('src'))
log.close()
