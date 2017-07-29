import re
import csv
from bs4 import BeautifulSoup
import requests


URL = 'http://www.acecqa.gov.au/NQAITS/SearchServices.aspx?vm=1&state=vic&pn={}&ps=100'


with open('childcare_centres.csv', 'w') as f:
    writer = csv.writer(f)
    for n in range(1, 42):
        page = requests.get(URL.format(n))
        soup = BeautifulSoup(page.text, 'html.parser')
        for item in soup.find_all(class_='search-item'):
            name = item.find('h3').text.strip()
            span = item.find(class_='span8')
            address = span.find('p').text.strip()
            try:
                suburb = re.search(',[A-Z\ ]{1,},', address).group(0).replace(',', '').strip()
            except:
                suburb = None
            pcode = re.search('[0-9]{4}', address).group(0).strip()
            try:
                places = span.find(
                    'strong', text="Approved Places").parent.parent.find_all('div')[1].text.strip()
                place = re.search('[\d+]*', places).group(0)
            except:
                place = None
            try:
                service_type = span.find(
                    'strong', text="Service Type").parent.parent.find_all('div')[1].text.strip()
            except:
                service_type = None
            writer.writerow([name, address, suburb, pcode, service_type, place])
