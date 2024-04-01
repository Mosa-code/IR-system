from typing import Any
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyCrawler(scrapy.Spider):
    name = "MyCrawler"
    start_urls = ['https://en.wikipedia.org/wiki/Nintendo']
    custom_settings = {
        'CONCURRENT_REQUESTS': 2,
        'DEPTH_LIMIT': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'AUTO_THROTTLE_ENABLED': True,
    }
        
    def __init__(self):
        self.link_extractor = LinkExtractor(allow='https://en.wikipedia.org/wiki/Nintendo', unique=True)

    def parse(self,response):
        for link in self.link_extractor.extract_links(response):
            with open('links.txt', 'a+') as f:
                f.write(f"\n{str(link)}")
            yield response.follow(url=link, callback=self.parse)

