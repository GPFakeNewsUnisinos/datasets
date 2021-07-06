# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    
