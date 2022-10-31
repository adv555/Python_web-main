# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsAggregatorItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    image = scrapy.Field()
    # authors = scrapy.Field()

class NewsAuthorItem(scrapy.Item):
    authors = scrapy.Field()
