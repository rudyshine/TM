# Mac下不能使用
from scrapy import cmdline
cmdline.execute("scrapy crawl Spider  -o M_spider_data.csv".split())
# cmdline.execute("scrapy crawl Spider".split())