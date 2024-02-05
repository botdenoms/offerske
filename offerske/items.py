# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class OfferskeItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    offer = scrapy.Field()
    price = scrapy.Field()
    off = scrapy.Field()
    left = scrapy.Field()
    thumb = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()

    features = scrapy.Field()
    features_items = scrapy.Field()
    box = scrapy.Field()
    box_items = scrapy.Field()
    specs = scrapy.Field()
    specs_items = scrapy.Field()

    ratings = scrapy.Field()
    stars = scrapy.Field()
