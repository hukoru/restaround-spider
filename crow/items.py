# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RestaurantItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    restaurant_id = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()

    pass


class RestaurantDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    ranking = scrapy.Field()
    keywords = scrapy.Field()
    price_range = scrapy.Field()
    cover_image_url = scrapy.Field()
    cover_image_width = scrapy.Field()
    cover_image_height = scrapy.Field()
    content = scrapy.Field()
    content2 = scrapy.Field()
    hour_range_sunday = scrapy.Field()
    hour_range_monday = scrapy.Field()
    hour_range_tuesday = scrapy.Field()
    hour_range_wednesday = scrapy.Field()
    hour_range_thursday = scrapy.Field()
    hour_range_friday = scrapy.Field()
    hour_range_saturday = scrapy.Field()
    address = scrapy.Field()
    location = scrapy.Field()
    phone_number = scrapy.Field()

    pass