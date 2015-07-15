import scrapy
import urllib2
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request

import os.path


class AnarchySpider(scrapy.Spider):
    name = "anarchy"
    # 
    #allowed_domains = ["anarchy-online.com"]
    start_urls = ['http://www.anarchy-online.com']
    path = "/home/nuwen/Funcom/anarchy_spider/files/"

    def parse(self, response):

        # scrape assets
        self.scrape_assets(response)

        # write response body to flat file
        item = {}
        item['url'] = response.url
        item['html'] = response.body
        fullPath =  self.path + response.url.split("/")[-1] + ".html"
        file = open(fullPath, "w+")
        file.write(item["html"])
        file.close()

        # follow urls
        urls = Selector(response=response).xpath("//a/@href").extract()
        for link in urls:
            # ignore image hrefs
            if link.split(".")[-1].lower() in ["jpg", "jpeg", "gif", "png", "bmp", "tiff"]:
                pass
            elif link.startswith("/"):
                yield Request(self.start_urls[0]+link, callback=self.parse)

    def scrape_assets(self, response):
        # //img/@src, //link/@href, //script/@src
        imgs = Selector(response=response).xpath("//img/@src").extract()
        links = Selector(response=response).xpath("//link/@href").extract()
        scripts = Selector(response=response).xpath("//script/@src").extract()
        assets = [imgs, links, scripts]
        for obj in assets:
            for url in obj:
                self.write_asset(url)

    def write_asset(self, url):
        # ignore external urls
        if not url.startswith("/"):
            return
        else:
            response = urllib2.urlopen(self.start_urls[0]+url)

        asset = response.read()
        # strip leading "/" to append to our path
        if url.startswith("/"): url = url[1:]
        if not os.path.exists(os.path.dirname(self.path+url)):
            os.makedirs(os.path.dirname(self.path+url))
        file = open(self.path+url, "w+")
        file.write(asset)
        file.close()