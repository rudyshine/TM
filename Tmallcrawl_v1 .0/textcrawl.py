import numpy as np
import pandas as pd
import time
import re
import codecs
import requests
import matplotlib.pyplot as plt
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
'Accept':'*/*',
'accept-encoding':'gzip, deflate, sdch, br',
'accept-language': "zh-CN,zh;q=0.8",
'Referer':'https://www.tmall.com/'}

cookie={
'_tb_token':'cIWuKnQ9Lruc',
'cna':'LVFjEWkW22MCAd0E0xPQMlfe',
'cookie2':'1c44760819e5c09a2b394cc883130e42',
'isg':'As3NGEzYqVJhKQ1cB-gs5t6F3OA7UwF8SGl9Ow9S3mTBBuy41vvPTNnUBiyb',
'l':'AgoK6Mo0UQIPvnFe3Ng-M4If2vusLI5H',
't':'0927edf52d4b5d1cb826664c94a48b58',
'tk_trace':'1'}
productId='1111'

url0 = "https://rate.tmall.com/list_detail_rate.htm?itemId=543801975609&spuId=569641085" \
       "&sellerId=3079263591&order=3&currentPage=1&append=0&content=1&tagId=&posi=&" \
       "picture=&ua=059UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2FQXxJdE5xRX9Bfyk" \
       "%3D%7CU2xMHDJ7G2AHYg8hAS8XLQMjDUsqTDBBbzlv%7CVGhXd1llXGhWa15jWWZSaFZoX2JAeER%2BQ3" \
       "xDfkR%2FRXxHeUF0TmA2%7CVWldfS0QMAg9AyMfKgokWzJJZQZ1GytRIkcmdhMsCCNqRBJE%7CVmhIGCcS" \
       "Mg8vEy4TJwc5DTcKKhYrFC0NNww5GSUYJx4%2BBDkCVAI%3D%7CV25OHjAePgQ4DS0TLxMzCzUPO207%7CWGF" \
       "BET9UM1UoRSNecFBoXWNDfEZ9XWdZZlwKXA%3D%3D%7CWWBAED4QMAsyByceIB8%2FCjEPNWM1%7CWmFBET" \
       "9aIgwsEC8RMQwsGCEfI3Uj%7CW2JCEjwSMgo%2FCysVIB8%2FAz8HPABWAA%3D%3D%7CXGVFFTsVNQw5DS0" \
       "RLRUoCDQKMQUxZzE%3D%7CXWVFFTsVNWVcZlNzT3NKfykJNBQ6FDQINgI3CV8J%7CXmdaZ0d6WmVFeUB8XG" \
       "JaYEB5WWVYeExsWXlGfFxnR39fY10L&isg=As3NGEzYqVJhKQ1cB-gs5t6F3OA7UwF8SGl9Ow9S3mTBBuy41v" \
       "vPTNnUBiyb&needFold=0&_ksTS=1493080744558_2197&callback=jsonp2198"
url1 = "https://rate.tmall.com/list_detail_rate.htm?itemId=543801975609&spuId=569641085" \
       "&sellerId=3079263591&order=3&currentPage=1&append=0&content=1&tagId=&posi=&" \
       "picture=&ua=059UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt%2FQXxJdE5xRX9Bfyk" \
       "%3D%7CU2xMHDJ7G2AHYg8hAS8XLQMjDUsqTDBBbzlv%7CVGhXd1llXGhWa15jWWZSaFZoX2JAeER%2BQ3" \
       "xDfkR%2FRXxHeUF0TmA2%7CVWldfS0QMAg9AyMfKgokWzJJZQZ1GytRIkcmdhMsCCNqRBJE%7CVmhIGCcS" \
       "Mg8vEy4TJwc5DTcKKhYrFC0NNww5GSUYJx4%2BBDkCVAI%3D%7CV25OHjAePgQ4DS0TLxMzCzUPO207%7CWGF" \
       "BET9UM1UoRSNecFBoXWNDfEZ9XWdZZlwKXA%3D%3D%7CWWBAED4QMAsyByceIB8%2FCjEPNWM1%7CWmFBET" \
       "9aIgwsEC8RMQwsGCEfI3Uj%7CW2JCEjwSMgo%2FCysVIB8%2FAz8HPABWAA%3D%3D%7CXGVFFTsVNQw5DS0" \
       "RLRUoCDQKMQUxZzE%3D%7CXWVFFTsVNWVcZlNzT3NKfykJNBQ6FDQINgI3CV8J%7CXmdaZ0d6WmVFeUB8XG" \
       "JaYEB5WWVYeExsWXlGfFxnR39fY10L&isg=As3NGEzYqVJhKQ1cB-gs5t6F3OA7UwF8SGl9Ow9S3mTBBuy41v" \
       "vPTNnUBiyb&needFold=0&_ksTS=1493080744558_2197&callback=jsonp2198"
r=requests.get(url=url0,headers=headers,cookies=cookie)
html0=r.content.decode('gb2312','ignore')
html0=str(html0)
file = codecs.open("page0.txt", "w")
file.write(html0)
file.close()
html0 = codecs.open('page0.txt', 'r').read()
print(html0)
# 获取总页数
lastPage=str.find('lastPage')
# page=lastPage.pop()
print(len(lastPage))
print(lastPage)

# ##提取评论信息
content=re.findall(r',"position".*?,"rateContent":(.*?)","',html0)
print("content:",len(content))
print("content:",content)
# print("开始执行抓取......")
# url1="https://club.jd.com/comment/productPageComments.action?callback=" \
#      "fetchJSON_comment98vv79456&productId=1993089&score=0&sortType=5&" \
#      "pageSize=10&isShadowSku=0&page="
# ran_num=range(0,int(page))
# r=requests.get(url=url1,headers=headers,cookies=cookie)
# html=r.content.decode('gb2312','ignore')
# for i in ran_num:
#       i=str(i)
#       url=url1+i
#       r=requests.get(url=url,headers=headers,cookies=cookie)
#       html2=r.content.decode('gb2312','ignore')
#       html = html + html2
#       time.sleep(1)
#       print("当前抓取页面:",url,"状态:",r)
#
# #写入文件
# html=str(html)#, encoding = "GBK")
# file = codecs.open("page.txt", "w")
# file.write(html)
# file.close()

# startime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# html = codecs.open('3889758page.txt', 'r').read()
#
# #产品名称
# referenceName=re.findall(r',"guid".*?,"referenceName":(.*?),',html)
# print("lenuserClient:",len(referenceName))
# print("referenceName:",referenceName)
#
# #下单时间referenceTime
# referenceTime1=re.findall(r',"referenceName".*?,"referenceTime":(.*?),',html)
# referenceTime=[]
# for d in referenceTime1:
#   date=d[1:20]
#   referenceTime.append(date)
# print("lenuserClient:",len(referenceTime))
# print("referenceTime:",referenceTime)
#
# ##提取userClient（用户客户端信息）字段信息
# userClient=re.findall(r',"referenceName".*?,"userClientShow":(.*?),',html)
# print("lenuserClient:",len(userClient))
# print("userClient:",userClient)
#
# # ##提取userLevel（用户等级）字段信息
# userLevel=re.findall(r'"productSize".*?,"userLevelName":(.*?),',html)
# print("lenuserLevel:",len(userLevel))
# print("userLevel",userLevel)
# # #提取productColor字段信息
# # productColor=re.findall(r'"referenceName".*?,"productColor":(.*?),',html)
# # print("productColor",productColor)
# # print("lenuserLevel:",len(productColor))
# # # #提取recommend(推荐)字段信息
# # recommend=re.findall(r'"creationTime".*?,"recommend":(.*?),',html)
# # print("lenuserLevel:",len(recommend))
# # print("recommend",recommend)
# # #提取nickname字段信息
# nickname=re.findall(r'"userImageUrl".*?,"nickname":(.*?),',html)
# print("lenuserLevel:",len(nickname))
# print("nickname",nickname)
#
# # #提取userProvince(省份)字段信息
# userProvince=re.findall(r'"userImageUrl".*?,"userProvince":(.*?),',html)
# print("lenuserLevel:",len(userProvince))
# print("userProvince",userProvince)
#
# # # #提取usefulVoteCount（被标记的有用评论数）字段信息
# # usefulVoteCount=re.findall(r'"referenceImage".*?,"usefulVoteCount":(.*?),',html)
# # print("lenuserLevel:",len(usefulVoteCount))
# # print("usefulVoteCount:",usefulVoteCount)
#
# #提取days字段信息
# days=re.findall(r'"referenceName".*?,"days":(.*?),',html)
# print("lendays:",len(days))
# print("days:",days)
#
# # #追加评论
# # afterDays=re.findall(r'"referenceName".*?,"afterDays":(.*?)}',html)
# # print("lenafterDays:",len(afterDays))
# # print("afterDays:",afterDays)
#
# ##提取score字段信息
# score=re.findall(r'"referenceName".*?,"score":(.*?),',html)
# print("lenscore:",len(score))
# print("score:",score)
# ##提取isMobile字段信息
# isMobile=re.findall(r'"productSize".*?,"isMobile":(.*?),',html)
# print("lenscore:",len(isMobile))
# print("isMobile:",isMobile,"\n")
# # mobile=[]
# # for m in isMobile:
# #     n=m.replace('}','') #替换掉最后的}
# #     mobile.append(n)
# # print("lenscore:",len(mobile))
# # print("mobile:",mobile)
# # ##提取productSize字段信息
# productSize=re.findall(r'"creationTime".*?,"productSize":(.*?),',html)
# print("lenscore:",len(productSize))
# print("productSize:",productSize)
#
# ##提取时间字段信息
# creationTime1=re.findall(r'"creationTime":(.*?),"referenceName',html)
# creationTime=[]
# for d in creationTime1:
#   date=d[1:20]
#   creationTime.append(date)
# print("lenscore:",len(creationTime))
# print("creationTime:",creationTime)
# # hour=[]
# # for h in creationTime:
# #   date=h[10:13]
# #   hour.append(date)
# # print("lenscore:",len(hour))
# # print("hour:",hour)

# table = pd.DataFrame({'creationTime': creationTime,"referenceTime":referenceTime,
#                       "referenceName":referenceName,'nickname': nickname,
#                        'productSize': productSize,
#                        'isMobile': isMobile, 'userClient': userClient,
#                       'userLevel': userLevel, 'userProvince': userProvince,
#                        'content_1': content_1,
#                       'days': days, 'score': score})
# # table = pd.DataFrame({'userClient': userClient, 'days': days,'score': score})
# table['creationTime'] = pd.to_datetime(table['creationTime'])
# table['referenceTime'] = pd.to_datetime(table['referenceTime'])
# table = table.set_index('creationTime')
# table.head()
# print("存入csv....")
# # table.to_csv('jd_table_textmaxpage.csv')
# table.to_csv( 'jd_table2222====.csv', mode='a')
# print("存完....")
# endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print("endtime is:",endtime)

# # print(df)
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