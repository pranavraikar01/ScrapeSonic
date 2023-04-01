from bs4 import BeautifulSoup
import pandas as pd
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
        self.sp = list()
        self.rating = list()
        self.categories = list()
        self.data = dict()
        self.pages = pages

        for url in urls:
            print(url)

            response = requests.get(url).content
            soup = BeautifulSoup(response, 'html.parser')
            all_blocks = soup.findAll('div', class_='_4ddWXP')
            for product in all_blocks:
                try:
                    if product.find('a', class_='s1Q9rs').get_text() and product.find('div', class_='_30jeq3').get_text() and product.find('div', class_='_3LWZlK').get_text() and category:

                        name = product.find('a', class_='s1Q9rs').get_text()
                        self.names.append(name)
                        print("Name ", name)

                        selling_price = product.find(
                            'div', class_='_30jeq3').get_text()
                        selling_price = str(selling_price).replace(
                            ",", "").split("₹")[1]
                        self.sp.append(selling_price)
                        print("Sell price", selling_price)

                        rat = product.find('div', class_='_3LWZlK').get_text()
                        if rat:
                            self.rating.append(rat)
                        else:
                            self.rating.append("None")
                        print("Rating ", rat)

                        if category:
                            self.categories.append(category)
                        else:
                            self.categories.append("None")
                        print("Category ", category)
                except Exception as e:
                    continue

        self.data['names'] = self.names
        self.data['selling_price'] = self.sp
        self.data['rating'] = self.rating
        self.data['categories'] = self.categories

        return self.data

    def flipkart_scraper(self, category, pages=0):
        self.pages = pages
        self.category = category

        urls = self.url_linker(self.pages, self.category)
        # returns a dictionary
        return self.scrapper(urls, self.category, self.pages)

    def types(self, n):
        self.n = n
        return self.n

    def dataframe_and_scrape(self, cat, pa=0):
        '''Scraped Data and DataFrame
        '''
        df = pd.DataFrame(
            columns=[
                'names',
                'selling_price',
                'rating',
                'categories',

            ],
        )
        df = df.rename_axis('S. No.')
        self.all_data = list()
        self.catego = cat

        self.pag = pa

        data = Scraper().flipkart_scraper(
            self.catego, self.pag)  # data is a dictionary here
        self.all_data.append(data)
        for d in self.all_data:
            df1 = pd.DataFrame(d)
            df = pd.concat([df, df1], ignore_index=True)
        return df
