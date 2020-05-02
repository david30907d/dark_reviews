import scrapy
from bs4 import BeautifulSoup
from dark_views.items import DarkViewsItem
import re
import unicodedata


class JkforumSpider(scrapy.Spider):
    name = "jkforum"
    allowed_domains = ["www.jkforum.net"]
    base_url = f"https://{allowed_domains[0]}"
    start_urls = [
        "https://www.jkforum.net/forum-1128-1.html",
    ]

    def parse(self, response):
        ''' This function parses jkforum. Some contracts are mingled
        with this docstring.

        @url https://www.jkforum.net/forum-1128-1.html
        @scrapes line_id wechat_id whatsapp_id phone_number website price img country city url
        '''
        outside_page_handlers_config = {
            "img": self._get_img,
            "country": self._get_country,
            "city": self._get_city,
            "url": lambda item: item.select("a.s.xst")[0],
        }

        soup = BeautifulSoup(response.text, features="lxml")
        for item in soup.select("tbody")[:20]:
            dv_item = DarkViewsItem()
            if item.get("id"):
                for field, handler in outside_page_handlers_config.items():
                    dv_item[field] = handler(item)
                if dv_item["url"] and dv_item["url"].get("href"):
                    dv_item["url"] = f"{self.base_url}/{dv_item['url']['href']}"
                    yield scrapy.Request(
                        dv_item["url"],
                        callback=self.parse_inner_page,
                        cb_kwargs=dv_item,
                    )

    def parse_inner_page(self, response, **dv_item):
        ''' This function parses jkforum. Some contracts are mingled
        with this docstring.

        @url https://www.jkforum.net/thread-11356677-1-1.html
        @returns items 1 1
        @scrapes line_id wechat_id whatsapp_id phone_number website price
        '''

        inner_page_handlers_config = {
            "line_id": self._get_line_id,
            "wechat_id": self._get_wechat_id,
            "whatsapp_id": self._get_whatsapp_id,
            "phone_number": self._get_phone_number,
            "website": self._get_website,
            "price": self._get_price,
        }
        inner_page = BeautifulSoup(response.text, features="lxml").select("div.pcb")[0]
        inner_page = unicodedata.normalize('NFKC', inner_page.text)
        inner_page_text = inner_page.replace("：", ":").replace(" ", "").lower()
        for field, handler in inner_page_handlers_config.items():
            dv_item[field] = handler(inner_page_text)
        return dv_item

    @staticmethod
    def _get_img(item) -> str:
        if item.img:
            return item.img.get("src")

    @staticmethod
    def _get_country(item) -> str:
        return "台灣"

    @staticmethod
    def _get_city(item) -> str:
        return "台北"

    @classmethod
    def _get_line_id(cls, inner_page_text: str) -> str:
        line_regexs = (
            r"(id.*|line.*|賴.*):([a-zA-Z0-9]+)",
            r"(lineid|line|賴|賴id)([a-zA-Z0-9]+)",
        )
        return cls._get_social_media_id(inner_page_text, line_regexs)

    @classmethod
    def _get_wechat_id(cls, inner_page_text: str) -> str:
        line_regexs = (
            r"(wechat.*):([a-zA-Z0-9]+)",
            r"(wechat)([a-zA-Z0-9]+)",
        )
        return cls._get_social_media_id(inner_page_text, line_regexs)

    @classmethod
    def _get_whatsapp_id(cls, inner_page_text: str) -> str:
        line_regexs = (
            r"(whatsapp.*):([a-zA-Z0-9]+)",
            r"(whatsapp)([a-zA-Z0-9]+)",
        )
        return cls._get_social_media_id(inner_page_text, line_regexs)

    @classmethod
    def _get_phone_number(cls, inner_page_text):
        line_regexs = (
            r"(聯絡.*|電話.*|手機.*|cellphone.*|來電.*):(09[0-9 –-]{8,10})",
            r"(聯絡|電話|手機|phone|來電)(09[0-9 –-]{8,10})",
            r"(.+?)(09[0-9 –-]{8,10})",
        )
        return cls._get_social_media_id(inner_page_text, line_regexs)

    @staticmethod
    def _get_website(inner_page_text):
        return ""

    @classmethod
    def _get_price(cls, inner_page_text):
        line_regexs = (
            r"(費用.*|價錢.*|分鐘.*|小時.*|分.*):([1-9]{1}[0-9]{3}|[1-9]k)",
            r"(費用.*|價錢.*|分鐘.*|小時.*|分.*)/([1-9]{1}[0-9]{3}|[1-9]k)",
            r"(費用|價錢|分鐘|小時|分)([1-9]{1}[0-9]{3}|[1-9]k)",
        )
        return cls._get_social_media_id(inner_page_text, line_regexs, 0)

    @staticmethod
    def _get_social_media_id(inner_page_text, social_media_regexs, default=''):
        for line_regex in social_media_regexs:
            regex_result = re.search(line_regex, inner_page_text)
            if regex_result:
                return regex_result.group(2).strip()
        return ""
