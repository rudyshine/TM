from scrapy import cmdline
cmdline.execute("scrapy crawl TmSpider  -o X_spider_data.csv".split())
# cmdline.execute("scrapy crawl TmSpider ".split())