# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebItem(scrapy.Item):

    title = scrapy.Field()
    time = scrapy.Field()
    temp = scrapy.Field()
    Weather = scrapy.Field()
    Feels_Like = scrapy.Field()
    Wind = scrapy.Field()
    Humidity = scrapy.Field()
    Chance = scrapy.Field()
    Amount = scrapy.Field()


