# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


# http://stackoverflow.com/questions/19910055/scrapy-storing-crawled-pages-as-static-files

from scrapy.item import Item, Field


class AnarchySpiderItem(scrapy.Item):
    url = Field()
    html = Field()
