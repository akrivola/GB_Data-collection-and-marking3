# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    categories = scrapy.Field()
    url = scrapy.Field()
    photo = scrapy.Field()
    #file_path = scrapy.Field()