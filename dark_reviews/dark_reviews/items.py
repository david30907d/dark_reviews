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
    title = scrapy.Field()

    img = scrapy.Field()
    price = scrapy.Field()

    country = scrapy.Field()
    city = scrapy.Field()


class WixItem(scrapy.Item):
    handleId = scrapy.Field()
    fieldType = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    productImageUrl = scrapy.Field()
    collection = scrapy.Field()
    sku = scrapy.Field()
    ribbon = scrapy.Field()
    price = scrapy.Field()
    surcharge = scrapy.Field()
    visible = scrapy.Field()
    discountMode = scrapy.Field()
    discountValue = scrapy.Field()
    inventory = scrapy.Field()
    weight = scrapy.Field()
    productOptionName1 = scrapy.Field()
    productOptionType1 = scrapy.Field()
    productOptionDescription1 = scrapy.Field()
    productOptionName2 = scrapy.Field()
    productOptionType2 = scrapy.Field()
    productOptionDescription2 = scrapy.Field()
    productOptionName3 = scrapy.Field()
    productOptionType3 = scrapy.Field()
    productOptionDescription3 = scrapy.Field()
    productOptionName4 = scrapy.Field()
    productOptionType4 = scrapy.Field()
    productOptionDescription4 = scrapy.Field()
    productOptionName5 = scrapy.Field()
    productOptionType5 = scrapy.Field()
    productOptionDescription5 = scrapy.Field()
    productOptionName6 = scrapy.Field()
    productOptionType6 = scrapy.Field()
    productOptionDescription6 = scrapy.Field()
    additionalInfoTitle1 = scrapy.Field()
    additionalInfoDescription1 = scrapy.Field()
    additionalInfoTitle2 = scrapy.Field()
    additionalInfoDescription2 = scrapy.Field()
    additionalInfoTitle3 = scrapy.Field()
    additionalInfoDescription3 = scrapy.Field()
    additionalInfoTitle4 = scrapy.Field()
    additionalInfoDescription4 = scrapy.Field()
    additionalInfoTitle5 = scrapy.Field()
    additionalInfoDescription5 = scrapy.Field()
    additionalInfoTitle6 = scrapy.Field()
    additionalInfoDescription6 = scrapy.Field()
    customTextField1 = scrapy.Field()
    customTextCharLimit1 = scrapy.Field()
    customTextMandatory1 = scrapy.Field()


class WixBlog(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    images = scrapy.Field()
