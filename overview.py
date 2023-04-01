from bs4 import BeautifulSoup
import requests
from individuallink import Scraper


class Scraper1:
    def scrapper(self, category, pages):

      # creating a list to store the scrapped description
        self.descriptions = list()

        # urlrecieved is  not in the form of list but is a part of list which is send directly by the function
        urlrecieved = Scraper().individuallink_scraper(category, pages)

        print(urlrecieved)

        response = requests.get(urlrecieved).content
        soup = BeautifulSoup(response, 'html.parser')
        # description_block  is the main block of description
        description_block = soup.findAll('div', class_='_1AtVbE col-12-12')
        for description in description_block:
            try:

                if description.find('div', class_='_1mXcCf').get_text():
                    description = description.find(
                        'div', class_='_1mXcCf').get_text()
                    print(description)
                    self.descriptions.append(description)

            except Exception as e:
                continue

        return self.descriptions

    def flipkart_scraper(self, category, pages=0):
        self.pages = pages
        self.category = category

        data = Scraper1().scrapper(self.category, self.pages)  # data is  a list
        print(data)

        return data
