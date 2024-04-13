import scrapy, os
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

class MyCrawler(scrapy.Spider):
    name = "MyCrawler"
    start_urls = ['https://en.wikipedia.org/wiki/League_of_Legends']
    custom_settings = {
        'CONCURRENT_REQUESTS': 2,
        'DEPTH_LIMIT': 6,
        'CLOSESPIDER_PAGECOUNT': 6,
        'AUTO_THROTTLE_ENABLED': True,
    }

        
    def __init__(self):
        self.link_extractor = LinkExtractor(allow='https://en.wikipedia.org/wiki/League_of_Legends', unique=True)

    def parse(self, response):
        page_name = response.url.split("/")[-1]
        filename = f'{page_name}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        yield {
            'title': response.css('title::text').get(),
            'url': response.url,
        }

        for link in self.link_extractor.extract_links(response):
            yield response.follow(url=link, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
    "SCRAPYD_HOST": "localhost",  
    "SCRAPYD_PORT": 6800,  
})

process.crawl(MyCrawler)
process.start()
