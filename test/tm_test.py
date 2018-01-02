import requests
from bs4 import BeautifulSoup
import re
import time

# url = "https://list.tmall.com/search_product.htm?sort=s&style=g&theme=699&active=1&cat=50924011&brand=30652%2C30862%2C30645%2C21210%2C4536553"
url="https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.2a70033eVI6hpk&cat=50924011&brand=30652,30862,30645,21210,4536553&s=300&sort=s&style=g&active=1&industryCatId=50924011&theme=699&spm=a220m.1000858.0.0.2a70033eVI6hpk&type=pc#J_Filter"
r=requests.get(url)
time.sleep(10)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
ips = soup.find_all('div', class_="view  view-noCom")
productPrice=re.findall(r'<em title="(.*?)">', str(ips))
print(productPrice)
print(len(productPrice))
productStatus=re.findall(r'<em>(.*?)</em>', str(ips))
print(productStatus)
print(len(productStatus))
productType=re.findall(r'<a .*? title="电风扇类别:(.*?)">', str(ips))
print(len(productType))
print(productType)
productName=re.findall(r'<a data-p=".*?" href=".*?" target="_blank" title=".*?">(.*?)</a>', str(ips))
print(productName)
print(len(productName))


links=soup.find_all('a',class_="ui-page-next")
for i in links:
    if links==[]:
        break
    else:
        links = re.findall(r'<a .*? href="\?(.*?)">', str(links))[0]
        link = re.sub(r"amp;", "", links)
        nextlink = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.2a70033eVI6hpk&' + link
        print(nextlink)






