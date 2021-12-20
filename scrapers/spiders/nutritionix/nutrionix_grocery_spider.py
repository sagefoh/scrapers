import scrapy
# from scrapers.items import BrandItem, ProductItem
from scrapy_selenium import SeleniumRequest


class NutritionixGrocerySpider(scrapy.Spider):
    name = 'nutritionix_grocery_spider'
    allowed_domains = ["www.nutritionix.com"]
    start_urls = ["https://www.nutritionix.com/brands/grocery/"]

    def start_requests(self):
        # pkl.dump(browser.get_cookies(), open(cookies_path, "wb"))
        # cookies = pkl.load(open(cookies_path, "rb"))
        # for cookie in cookies:
        #     browser.add_cookie(cookie)
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                wait_time=3,
                # screenshot=True,
                callback=self.parse,
                dont_filter=True,
            )

    def parse(self, response):
        driver = response.request.meta['driver']

        brand_list = []
        page_count = 1

        link_path = '//div[@class="brand-grid ng-scope"]/a[@class="block"]'
        brand_path = '//p[@class="ng-binding"]'
        page_path = '//pre[@class="text-center ng-binding"]'

        page_text = driver.find_elements(by='xpath', value=page_path)
        print('\n\n\n\n\n\n\n')

        print(len(page_text))

        print('\n\n\n\n\n\n\n')

        max_item = int(page_text.split(' ')[-1])

        print('NutriSpider has started crawling...')

        print('\n\n\n\n\n\n\n\n')

        while True:
            link_elements = driver.find_elements(by='xpath', value=link_path)
            links = [link_element.get_attribute('href') for link_element in link_elements]

            brand_elements = driver.find_elements(by='xpath', value=brand_path)
            names = [brand_element.get_attribute('innerHTML').strip() for brand_element in brand_elements]

            brand_list.extend(tuple(zip(names, links)))

            page_text = driver.find_elements(by='xpath', value=page_path)[0].get_attribute('innerHTML')

            item_count = int(page_text.split(' - ')[-1].split(' ')[0])

            print(brand_list)

            if item_count >= max_item:
                print('Crawling done. The spider has retired to its abode.')
                break
            else:
                page_count += 1
                driver.get(url=url + '?page={}'.format(page_count))


        print('\n\n\n\n\n\n\n\n')

    def parse_brands(self, response):
        pass

    def parse_products(self, response):
        pass


# url = 'https://www.nutritionix.com/brands/grocery'
# browser = init_chrome_browser(
#     download_path="/tmp/downloads",
#     chrome_driver_path="/tmp/chromedriver/chromedriver",
#     cookies_path="/dbfs" + utils_folder + "cookies.pkl",
#     url=url
#
# )
#
# links = []
# brands = []
# page_count = 1
#
# link_path = '//div[@class="brand-grid ng-scope"]/a[@class="block"]'
# brand_path = '//p[@class="ng-binding"]'
# page_path = '//pre[@class="text-center ng-binding"]'
#
# page_text = browser.find_elements(by='xpath', value=page_path)[0].get_attribute('innerHTML')
# item_count = int(page_text.split(' - ')[-1].split(' ')[0])
# max_item = int(page_text.split(' ')[-1])
#
# bar = pb.ProgressBar(max_value=max_item, )
#
# print('NutriSpider has started crawling...')
#
# while (True):
#     link_elements = browser.find_elements(by='xpath', value=link_path)
#     links.extend([link_element.get_attribute('href') for link_element in link_elements])
#
#     brand_elements = browser.find_elements(by='xpath', value=brand_path)
#     brands.extend([brand_element.get_attribute('innerHTML').strip() for brand_element in brand_elements])
#
#     page_text = browser.find_elements(by='xpath', value=page_path)[0].get_attribute('innerHTML')
#
#     item_count = int(page_text.split(' - ')[-1].split(' ')[0])
#
#     pbar(item_count, max_item, status='Crawling')
#
#     if item_count >= max_item:
#         print('Crawling done. The spider has retired to its abode.')
#         break
#     else:
#         page_count += 1
#         browser.get(url=url + '?page={}'.format(page_count))
