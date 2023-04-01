from bs4 import BeautifulSoup
import requests


class Scraper:
    ''' Scraper Class
    '''

    def url_linker(self, total_pages=0, *args):
        self.urls = list()
        for page in range(1, total_pages+1):
            self.urls.append(self.url_builder(page, *args))
        return self.urls

    def url_builder(self, page=0, *args):
        self.parms = '+'.join(args)
        self.url = f'https://www.flipkart.com/search?q={self.parms}&page={page}'
        return self.url

    def scrapper(self, urls: list, category, pages):

        self.names = list()
        self.data = list()

        for url in urls:
            print(url)

            response = requests.get(url).content
            soup = BeautifulSoup(response, 'html.parser')
            all_blocks = soup.findAll('div', class_='_1YokD2 _3Mn1Gg')
            for product in all_blocks:
                try:
                    if product.find('a', class_='s1Q9rs').get_text():

                        name = product.find('a', class_='s1Q9rs').get('href')
                        flipkart = f'https://www.flipkart.com'
                        link = flipkart+name
                        self.names.append(link)
                        print("Name ", link)

                except Exception as e:
                    continue

        self.data = self.names  # data is a list which has our generated link

        return self.data

    # this function sends the actual link of the product recieved from the scraper function which is generated using the category parameter which is accepted in the box on gui where we can also select the category and also write the product we want
    def individuallink_scraper(self, category, pages=0):
        self.pages = pages
        self.category = category

        # url of page containing mainy blocks is obtained
        urls = self.url_linker(self.pages, self.category)
        # thus this function send actual link of a product in the form of a list
        url = self.scrapper(urls, self.category, self.pages)
        return url[0]
