import pytest
import requests

from dark_reviews.spiders.jkforum import JkforumSpider

JK_SPIDER = JkforumSpider()
SESS = requests.session()


def test_parse_inner_page1() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-10161939-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "hihoi456",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "",
            "website": "",
            "price": "",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page2() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-11363988-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "a51688a",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "",
            "website": "",
            "price": "",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page3() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-7343037-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "sd688",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "0900506327",
            "website": "",
            "price": "1400",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page4() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-10671336-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "cwu290",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "0916-415-110",
            "website": "",
            "price": "2400",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page5() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-11739367-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "cce225",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "",
            "website": "",
            "price": "",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page6() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-10261503-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "sexybaby16888",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "0967–314–285",
            "website": "",
            "price": "2300",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page7() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-10312490-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "0939690904",
            "website": "",
            "price": "1800",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page8() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-10819145-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "w33211",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "",
            "website": "",
            "price": "",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page9() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-11707629-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "w33211",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "",
            "website": "",
            "price": "",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")


def test_parse_inner_page10() -> None:
    if __debug__:
        item = JK_SPIDER.parse_inner_page(
            SESS.get("https://www.jkforum.net/thread-9233575-1-1.html"), **{"img": ""}
        )
        if item != {
            "line_id": "",
            "wechat_id": "",
            "whatsapp_id": "",
            "phone_number": "0974-125-599",
            "website": "",
            "price": "2000",
            "img": "",
        }:
            raise AssertionError("parse_inner_page!")
