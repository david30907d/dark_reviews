# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DarkViewsPipeline:
    def process_item(self, item, spider):
        have_at_least_one_social_media_id = False
        for social_media_id in ("line_id", "wechat_id", "whatsapp_id"):
            if item.get(social_media_id):
                have_at_least_one_social_media_id = True
            item.setdefault(social_media_id, "")
        if not have_at_least_one_social_media_id:
            raise Exception("Should have at least one social media id!")
        item.setdefault("phone_number", "")
        item.setdefault("website", "")
        item.setdefault("price", "")
        return item
