import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scrapy.crawler import CrawlerProcess
from Crawler.spiders import crawlingspider

def show_options():
    print("Please select an option:")
    print("1. Run the Spider")
    print("2. TBD")
    print("3. TBD")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("Running Scrapy spider...")
        process = CrawlerProcess()
        process.crawl(crawlingspider)
        process.start()  
    elif choice == "2":
        print("You selected Option 2.")
    elif choice == "3":
        print("You selected Option 3.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        
show_options()
