# -*-utf8-*-
import requests
import time
import random
import re
# import numpy as np
import pandas as pd
import pymongo
import codecs
from bs4 import BeautifulSoup
from urllib import request
import matplotlib.pyplot as plt

#设置请求中头文件的信息
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'https://www.jd.com/'}

cookie={
'_jda':'122270672.2082744608.1490836927.1491443901.1491447607.20',
'__jdb':'122270672.6.2082744608|20.1491447607',
'__jdc':'122270672',
'__jdu':'2082744608',
'__jdv':'122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d0494d40ca3242e2b57611255d334b6d|1491447607413',
'ipLoc-djd':'1-72-2799-0',
'ipLocation':'%u5317%u4EAC',
'unpl':'V2_ZzNtbRdWRh1wXUNVKUleBmIARl4RU0USdQhFUH9MXgdiUBUIclRCFXMUR1FnGFwUZwMZXUpcRxNFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2V3oQXwNiBhVcS2dzEkU4dlB%2fEVoMZDMTbUNnAUEpAEdUcxFbSGQCG15EUkYSdAF2VUsa',
'user-key':'c4a237ca-dae8-403e-9cec-ad4d0c1470da'}

def get_ip_list(url_ip, headers_ip):
    web_data = requests.get(url_ip, headers=headers_ip)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[0].text + ':' + tds[1].text)
    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def get_maxpage(url0):
    r=requests.get(url=url0,headers=headers,cookies=cookie)
    html0=r.content.decode('gb2312','ignore')
    html0=str(html0)
    file = codecs.open(productId+"page.txt", "w")
    file.write(html0)
    file.close()
    html0 = codecs.open(productId+'page.txt', 'r').read()
    maxpage=re.findall(r',"jwotestProduct".*?,"maxPage":(.*?),',html0)
    if maxpage==['0']:
        print("这个产品没有用户进行评论")
        return 0
    else:
        sumpage = maxpage.pop()
        return sumpage

def crawlpage(ran_num,url1,proxies):
    r = requests.get(url=url1, headers=headers, cookies=cookie,timeout=10,proxies = proxies)
    html = r.content.decode('gb2312', 'ignore')
    for i in ran_num:
        i = str(i)
        url = url1 + i

        r = requests.get(url=url, headers=headers, cookies=cookie,timeout=10,proxies = proxies)
        html2 = r.content.decode('gb2312', 'ignore')
        html = html + html2
        # time.sleep(5)
        print("当前抓取页面:", url, "状态:", r)
    # html = str(html)
    # 写入文件
    html = str(html)
    file = codecs.open(productId+"page.txt", "w")
    file.write(html)
    file.close()

    html = codecs.open(productId+"page.txt", 'r').read()
    # 产品名称
    referenceName = re.findall(r',"guid".*?,"referenceName":(.*?),', html)
    print("lenuserClient:", len(referenceName))
    print("referenceName:", referenceName)

    # 下单时间referenceTime
    referenceTime1 = re.findall(r',"referenceName".*?,"referenceTime":(.*?),', html)
    referenceTime = []
    for d in referenceTime1:
        date = d[1:20]
        referenceTime.append(date)
    print("lenuserClient:", len(referenceTime))
    print("referenceTime:", referenceTime)

    ##提取userClient（用户客户端信息）字段信息
    userClient = re.findall(r',"referenceName".*?,"userClientShow":(.*?),', html)
    # ##提取userLevel（用户等级）字段信息
    userLevel = re.findall(r'"productSize".*?,"userLevelName":(.*?),', html)
    # #提取nickname字段信息
    nickname = re.findall(r'"userImageUrl".*?,"nickname":(.*?),', html)
    # #提取userProvince(省份)字段信息
    userProvince = re.findall(r'"userImageUrl".*?,"userProvince":(.*?),', html)
    # 提取days字段信息
    days = re.findall(r'"referenceName".*?,"days":(.*?),', html)
    ##提取score字段信息
    score = re.findall(r'"referenceName".*?,"score":(.*?),', html)
    ##提取isMobile字段信息
    isMobile = re.findall(r'"productSize".*?,"isMobile":(.*?),', html)
    # ##提取productSize字段信息
    productSize = re.findall(r'"creationTime".*?,"productSize":(.*?),', html)
    ##提取时间字段信息
    creationTime1 = re.findall(r'"creationTime":(.*?),"referenceName', html)
    creationTime = []
    for d in creationTime1:
        date = d[1:20]#取时间
        creationTime.append(date)
    ##提取评论信息
    content = re.findall(r'"guid".*?,"content":(.*?)","creationTime"', html)
    print("content:", len(content))
    # 对提取的评论信息进行去重
    content_1 = []
    for i in content:
        if not "img" in i:
            content_1.append(i)
    # 将前面提取的各字段信息汇总为table数据表，以便后面分析
    table = pd.DataFrame({'creationTime': creationTime,"referenceTime":referenceTime,
                       'referenceName':referenceName,'nickname': nickname,
                       'productSize': productSize,'isMobile': isMobile,
                       'userClient': userClient,'userLevel': userLevel,
                       'userProvince': userProvince,'content_1': content_1,
                       'days': days, 'score': score})
    table['creationTime'] = pd.to_datetime(table['creationTime'])
    table = table.set_index('creationTime')
    table.head()
    print("存入csv....")
    # table.to_csv('jd_table_textmaxpage.csv')
    table.to_csv(productId+'jd_table.csv', mode='a', header=False)
    print("存完....")

    # 数据存入momgodb
    print("开始连接数据库：")
    client = pymongo.MongoClient('localhost', 27017)
    rent_info = client['jd_table']  # 给数据库命名
    sheet_table = rent_info[productId+'jd_table']  # 创建表单
    sheet_table.insert({'creationTime': creationTime,"referenceTime":referenceTime,
                        'referenceName':referenceName,'nickname': nickname,
                        'productSize': productSize,'isMobile': isMobile,
                        'userClient': userClient,'userLevel': userLevel,
                        'userProvince': userProvince,'content_1': content_1,
                        'days': days, 'score': score})
    print("done......")
    donetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("endtime is:", donetime)

    # #数据可视化展示
    # mobile_t=table.loc[table["mobile"] == "true"]
    # #在table中筛选没有使用移动设备的条目并创建新表
    # mobile_f=table.loc[table["mobile"] == "false"]
    # #按月汇总使用移动设备的数据
    # mobile_t_m=mobile_t.resample('M',how=len)
    # #按月汇总不使用移动设备的数据
    # mobile_f_m=mobile_f.resample('M',how=len)
    # #提取使用移动设备的按月汇总nickname
    # mobile_y=mobile_t_m['nickname']
    # #提取没有使用移动设备的按月汇总nickname
    # mobile_n=mobile_f_m['nickname']
    #
    # plt.subplot(2, 1, 1)
    # plt.plot(mobile_y,'go',mobile_y,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
    # plt.ylabel('移动设备评论数量')
    # plt.title('PC&mobile')
    # plt.subplot(2, 1, 2)
    # plt.plot(mobile_n,'go',mobile_n,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
    # plt.xlabel('month')
    # plt.ylabel('PC')
    # plt.show()

def getnum(sumpage,url1):

    n=100
    if int(sumpage)>=n:
        m=int(sumpage)//n
        ran_num = range(int(sumpage))
        for i in range(m):
            s = set(ran_num)
            ran1 = random.sample(ran_num, n)
            s1 = set(ran1)
            ip_list = get_ip_list(url_ip, headers_ip=headers_ip)
            proxies = get_random_ip(ip_list)
            print("proxies:", proxies)
            crawlpage(ran1,url1,proxies)
            s2 = s - s1
            ran_num = list(s2)
        ran_num = random.sample(ran_num,len(ran_num))
        crawlpage(ran_num,url1,proxies)
    else:
        ip_list = get_ip_list(url_ip, headers_ip=headers_ip)
        proxies = get_random_ip(ip_list)
        print("proxies:", proxies)
        ran_num0 =random.sample(range(0,int(sumpage)), int(sumpage))
        crawlpage(ran_num0,url1,proxies)



if __name__=='__main__':
    startime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("startime is:", startime)
    ##ip代理网址
    url_ip='http://www.kuaidaili.com'
    headers_ip = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }
    ##产品列表网址
    url = "https://sale.jd.com/act/GrZjoT7UQWCn.html"
    ##产品爬取页面
    url2 = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&productId="
    url3 = "&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0"
    url4 = "&score=0&sortType=5&pageSize=10&isShadowSku=0&page="
    ##产品列表页面获取skuid值
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    for skuid in soup.find_all('li'):
        Id = skuid.get('skuid')
        if Id != None:
            Id = str.split(Id)
            productId = ''.join(Id)
            for i in range(0, len(Id)):
                productId = ''.join(Id)
                ##productId拼入抓取页面
                url0 = url2 + productId + url3
                print("url0:", url0)
                url1 = url2 + productId + url4
                print("url1:", url1)
                # time.sleep(60)
                sumpage=get_maxpage(url0)
                if sumpage!=0:
                    getnum(sumpage,url1)
                endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                print("endtime is:",endtime)
                # time.sleep(1800)

                #
                # 用以上手机号编辑短信yxzh到号码1069
                # 8163
                # 0163
                # 331
                # 完成验证
                # 注：可能有部分帐号不支持通过邮箱联系人找回密码