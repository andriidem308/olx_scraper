from scrapy.utils.project import get_project_settings
from sys import argv
from scrapy.crawler import CrawlerProcess
import os
import importlib
import inspect
import logging

log = logging.getLogger('starter')
scraper_id = str(argv[-1])
spiders = [spider.split('.py')[0] for spider in os.listdir('spiders')]
spider_default_classes = ['Product', 'Selenium']

if spiders.count(scraper_id) > 1:
    log.error(f'ID: {scraper_id} is duplicated!')
else:
    for spider in spiders:
        if scraper_id == spider:
            spider_path = importlib.import_module(f'spiders.{spider}')
            spider_classes = (inspect.getmembers(spider_path, inspect.isclass))
            found_classes = []
            for spider_class in spider_classes:
                if not spider_class[0] in spider_default_classes:
                    found_classes.append(spider_class[0])
            if found_classes:
                process = CrawlerProcess(get_project_settings())
                process.crawl(getattr(spider_path, found_classes[-1]), scraper_id)
                process.start()
