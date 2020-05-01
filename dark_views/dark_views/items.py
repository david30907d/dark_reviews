# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DarkViewsItem(scrapy.Item):
    # define the fields for your item here like:
    line_id = scrapy.Field()
    wechat_id = scrapy.Field()
    whatsapp_id = scrapy.Field()
    phone_number = scrapy.Field()

    website = scrapy.Field()
    url = scrapy.Field()

    img = scrapy.Field()
    price = scrapy.Field()

    country = scrapy.Field()
    city = scrapy.Field()
