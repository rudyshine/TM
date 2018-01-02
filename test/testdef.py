import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

def get_info(url):
    r=requests.get(url,timeout=1000)
    soup = BeautifulSoup(r.text, 'lxml')
    ips = soup.find_all('div', class_="view  view-noCom")
    productPrice=re.findall(r'<em title="(.*?)">', str(ips))
    print(productPrice)
    print(len(productPrice))
    productStatus=re.findall(r'<em>(.*?)</em>', str(ips))
    print(productStatus)
    print(len(productStatus))
    productType=re.findall(r'<a .*? title="电风扇类别:(.*?)">', str(ips))
    print(productType)
    print(len(productType))
    productName=re.findall(r'<a data-p=".*?" href=".*?" target="_blank" title=".*?">(.*?)</a>', str(ips))
    print(productName)
    print(len(productName))
    links = soup.find_all('a', class_="ui-page-next")
    links = re.findall(r'<a .*? href="\?(.*?)">', str(links))[0]
    link = re.sub(r"amp;", "", links)
    if link != []:
        url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.2a70033eVI6hpk&' + link
        get_info(url)





if __name__ == '__main__':
    url = "https://list.tmall.com/search_product.htm?sort=s&style=g&theme=699&active=1&cat=50924011&brand=30652%2C30862%2C30645%2C21210%2C4536553"
    get_info(url)


