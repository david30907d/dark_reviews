# -*- coding: utf-8 -*-
import json

import scrapy
from bs4 import BeautifulSoup
from opencc import OpenCC

from dark_reviews.items import WixBlog

OPENCC_CONVERTER = OpenCC("s2t")
ORIGIN_AUTHOR = "斯基"
NEW_AUTHOR = "SexTube"


class A1024sijiSpider(scrapy.Spider):
    name = "1024siji"
    allowed_domains = ["1024siji.com"]
    start_urls = [
        "http://www.1024siji.com/category/%e4%b8%9c%e4%ba%9a/%e6%97%a5%e6%9c%ac"
    ]

    custom_settings = {
        "ITEM_PIPELINES": {"dark_reviews.pipelines.A1024sijiPipeline": 300,}
    }

    def parse(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        for article in soup.select("h2 a"):
            blog_item = WixBlog()
            blog_item["title"] = OPENCC_CONVERTER.convert(article["title"])
            blog_item["url"] = article["href"]
            yield scrapy.Request(
                blog_item["url"], callback=self.parse_inner_page, cb_kwargs=blog_item,
            )

    def parse_inner_page(self, response, **blog_item):
        inner_page_soup = BeautifulSoup(response.text, features="lxml")
        blog_item["content"] = OPENCC_CONVERTER.convert(
            inner_page_soup.select("div.post-content")[0].text
        )
        blog_item["images"] = [
            img["src"] for img in inner_page_soup.select("div.post-content img")
        ]
        return blog_item
