import scrapy
# from scrapy.items import BrandItem, ProductItem
from scrapy_selenium import SeleniumRequest


class NutritionixGrocerySpider(scrapy.Spider):
    name = 'nutritionix_grocery_spider'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.nutritionix.com/brands/grocery',
            wait_time=10,
            # screenshot=True,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):
        driver = response.request.meta['driver']
        brand_elements = driver.find_elements(by='xpath', value='//p[@class="ng-binding"]')
        print([_ for _ in brand_elements])
        # print(brand_elements)
        # BrandItem.add_value('name', '//p[@class="ng-binding"]')

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
