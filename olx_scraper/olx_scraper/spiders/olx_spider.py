import scrapy
from modules.items import Product
from modules.utils import get_page


class OLXSpider(scrapy.Spider):
    name = 'olx_spider'

    start_urls = [
        'https://www.olx.ua/uk/elektronika/telefony-i-aksesuary/q-iphone-8/?search%5Bfilter_float_price%3Afrom%5D=1000&search%5Border%5D=created_at%3Adesc'
    ]

    page_size = 39

    def parse(self, response, **kwargs):
        links = response.xpath('//table[@id="offers_table"]//tr[@class="wrap"]//td[@class="title-cell "]//a/@href').extract()

        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_product)

        if len(links) == self.page_size:
            next_page = get_page(response.url) if 'page=' in response.url else response.url + '&page=2'
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_product(self, response):
        item = Product()
        item['Name'] = response.xpath('//h1/text()').extract_first()
        if item['Name']:
            item['URL'] = response.url
            item['Name'] = response.xpath('//h1/text()').extract_first()
            item['Price'] = response.xpath('//h3[contains(@class, "css-okktvh-Text")]/text()').extract_first()
            item['Description'] = response.xpath('//div[@class="css-g5mtbi-Text"]/text()').extract_first()
            yield item
