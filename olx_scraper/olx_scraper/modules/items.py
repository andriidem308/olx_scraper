import scrapy


class Product(scrapy.Item):
    URL = scrapy.Field()
    Price = scrapy.Field()
    Stock = scrapy.Field()
    Name = scrapy.Field()
    Brand = scrapy.Field()
    EAN = scrapy.Field()
    MPN = scrapy.Field()
    Description = scrapy.Field()
    Category = scrapy.Field()
    Shop_ID = scrapy.Field()
    Image = scrapy.Field()


product_fields = list(Product().fields.keys())


class Parser(scrapy.Item):
    vendorName = scrapy.Field()
    mpn = scrapy.Field()
    deeplink = scrapy.Field()
    name = scrapy.Field()
    categoryName = scrapy.Field()
    ean = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    proprietaryId = scrapy.Field()
    condition = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    promoText = scrapy.Field()
    reviewCount = scrapy.Field()
    reviewScore = scrapy.Field()
    hatch_stock = scrapy.Field()
    hatch_price = scrapy.Field()


product_parser_fields = list(Parser().fields.keys())


class WalmartJsonParser(scrapy.Item):
    itemId = scrapy.Field()
    name = scrapy.Field()
    salePrice = scrapy.Field()
    upc = scrapy.Field()
    brandName = scrapy.Field()
    productUrl = scrapy.Field()
    modelNumber = scrapy.Field()
    stock = scrapy.Field()
    customerRating = scrapy.Field()
    numReviews = scrapy.Field()
    categoryPath = scrapy.Field()
