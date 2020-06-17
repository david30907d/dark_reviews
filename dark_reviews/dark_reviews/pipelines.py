# -*- coding: utf-8 -*-


# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
from dark_reviews.items import WixItem


class DarkViewsPipeline:
    def __init__(self):
        self.duplicates = set()

    def process_item(self, item, spider):
        have_at_least_one_social_media_id = False
        for social_media_id in ("line_id", "wechat_id", "whatsapp_id", "phone_number"):
            if item.get(social_media_id) in self.duplicates:
                raise DropItem(f"Duplicate item found: {item}")
            if item.get(social_media_id):
                have_at_least_one_social_media_id = True
                self.duplicates.add(item.get(social_media_id))
        if (
            not have_at_least_one_social_media_id
            or item["price"] == 0
            or not item["img"]
        ):
            raise DropItem(
                "Should have at least one social media id! Also, price and img are necessary!"
            )
        return JkForumAdapter(item).item


class JkForumAdapter(object):
    def __init__(self, jkform_item):
        self.jkform_item = jkform_item
        self.item = WixItem()
        self.item["handleId"] = self.get_item_name()
        self.item["fieldType"] = "Product"
        self.item["name"] = self.get_item_name()
        self.item["description"] = self.warning() + jkform_item["title"]
        self.item["productImageUrl"] = jkform_item["img"]
        self.item["collection"] = jkform_item["city"]
        self.item["sku"] = ""
        self.item["ribbon"] = ""
        self.item["price"] = (
            jkform_item["price"]
            if "k" not in jkform_item["price"]
            else float(jkform_item["price"].replace("k", "")) * 1000
        )
        self.item["surcharge"] = ""
        self.item["visible"] = "TRUE"
        self.item["discountMode"] = ""
        self.item["discountValue"] = ""
        self.item["inventory"] = 1
        self.item["weight"] = ""
        self.item["productOptionName1"] = ""
        self.item["productOptionType1"] = ""
        self.item["productOptionDescription1"] = ""
        self.item["productOptionName2"] = ""
        self.item["productOptionType2"] = ""
        self.item["productOptionDescription2"] = ""
        self.item["productOptionName3"] = ""
        self.item["productOptionType3"] = ""
        self.item["productOptionDescription3"] = ""
        self.item["productOptionName4"] = ""
        self.item["productOptionType4"] = ""
        self.item["productOptionDescription4"] = ""
        self.item["productOptionName5"] = ""
        self.item["productOptionType5"] = ""
        self.item["productOptionDescription5"] = ""
        self.item["productOptionName6"] = ""
        self.item["productOptionType6"] = ""
        self.item["productOptionDescription6"] = ""
        self.item["additionalInfoTitle1"] = "簡介："
        self.item["additionalInfoDescription1"] = jkform_item["title"]
        self.item["additionalInfoTitle2"] = ""
        self.item["additionalInfoDescription2"] = ""
        self.item["additionalInfoTitle3"] = ""
        self.item["additionalInfoDescription3"] = ""
        self.item["additionalInfoTitle4"] = ""
        self.item["additionalInfoDescription4"] = ""
        self.item["additionalInfoTitle5"] = ""
        self.item["additionalInfoDescription5"] = ""
        self.item["additionalInfoTitle6"] = ""
        self.item["additionalInfoDescription6"] = ""
        self.item["customTextField1"] = ""
        self.item["customTextCharLimit1"] = ""
        self.item["customTextMandatory1"] = ""

    def get_item_name(self):
        prefix = self.jkform_item["city"]
        if self.jkform_item["line_id"]:
            return f"{prefix}-Line: {self.jkform_item['line_id']}"
        elif self.jkform_item["phone_number"]:
            return f"{prefix}-手機: {self.jkform_item['phone_number']}"
        elif self.jkform_item["wechat_id"]:
            return f"{prefix}-WeChat: {self.jkform_item['wechat_id']}"
        elif self.jkform_item["whatsapp_id"]:
            return f"{prefix}-WhatsApp: {self.jkform_item['whatsapp_id']}"

    def warning(self):
        return "請勿於本平台付費預約按摩師，請自行聯繫，任何交易皆與本平台無關。"
