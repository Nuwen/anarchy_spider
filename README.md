
# anarchy-online.com Spider
##### Created with [Scrapy](http://scrapy.org/)

Scrapes flat HTML files and assets from anarchy-online.com, recursively. 

### Installation
Requirements: Python 2.7+ & pip

``` 
git clone github.com/Nuwen/anarchy_spider.git new_dir
cd new_dir
pip install -r requirements.txt
OR
pip install scrapy
```

### Use
```
cd new_dir
scrapy runspider anarchy_spider/spiders/main_spider.py
```

Spider will scrape to ```files/``` and preserve all directory structure :)