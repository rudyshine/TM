# import codecs
# import re
# from urllib import request
# import requests
# from bs4 import BeautifulSoup
#
# # url='https://gree.tmall.com/category-1290118897.htm?spm=a1z10.1-b-s.w10971653-16352291479.13.ZyOt7k&search=y&scene=taobao_shop'
# url='https://rate.tmall.com/list_detail_rate.htm?itemId=543803699362&sellerId=1652490016&currentPage=1'
# r = requests.get(url=url)
# html0 = r.content.decode('gb2312', 'ignore')
# html0 = str(html0)
# file = codecs.open( "tmallpage.txt", "w")
# file.write(html0)
# file.close()
# Content=re.findall(r'rateContent(.*?)","',html0)
# print("lenuserClient:",len(Content))
# print("referenceName:",Content)
#
# Content=re.findall(r'rateContent(.*?)","',html0)
# print("lenuserClient:",len(Content))
# print("referenceName:",Content)

import requests as rq
import re
import pandas as pd
url='http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016¤tPage=1'
myweb = rq.get(url)
print(myweb.text)
myjson = re.findall('\"rateList\":(.*?)"searchinfo"',myweb.text)
mytable = pd.read_json(myjson)
mytable.to_csv('mytable.txt')
mytable.to_excel('mytable.xls')