import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

url="https://list.suning.com/0-20368-0-0-0-0-0-0-0-0-10018a45472a10017a10069a10132a56664.html"
r=requests.get(url)
time.sleep(10)
soup = BeautifulSoup(r.text, 'lxml')
print(soup)