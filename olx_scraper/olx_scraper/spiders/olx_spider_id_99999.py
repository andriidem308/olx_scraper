import scrapy


class OLXSpider(scrapy.Spider):
    name = 'olx_spider'

    start_urls = [
        'https://www.olx.ua/uk/elektronika/q-iphone-8/?search%5Bfilter_float_price%3Afrom%5D=1000'
    ]

    custom_headers = {
        'Host': 'www.olx.ua',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
        # 'Cookie': 'PHPSESSID=mj0d33fvg90hf554mk1a6qjf38;'
    }

    def parse(self, response, **kwargs):
        links = response.xpath('//td[@class="title-cell "]//a/@href').extract()
        print(links)
