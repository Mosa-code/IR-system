import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(scrapy.Spider):
    name = "MyCrawler"
    start_urls = ['http://example.com/']
    custom_settings = {
        'DEPTH_LIMIT': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'AUTOTHROTTLE_ENABLED': True,
    }
        
    rules = (
        Rule(LinkExtractor(), callback="parse_item")
        )     

    def parse_item(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


    
