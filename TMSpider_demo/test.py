# a=[1,3,4]
# b=[2,5]
# # print(len(a))
# a[len(a):]=b
# print(a)
import re
import jieba
from string import punctuation

text='"车厢，设坐票制。昨日，《南都ＭＥＴＲＯ》创刊仪式暨２０１２年深港地铁圈架的车厢和买双副秘书长、轨道交人的需求，提有微高一“我们要稍高一些' \
     '的服务”。比如，尝试有地铁赵鹏林说，比如有些地铁是“观光线”，不仅沿途的风光非常好，还能凭一张票无数次上下，如同旅' \
     '游时提供的“通票服务”。再比门可放大件行李的座位，避免像现在放行李不太方便的现象。“未来地铁建设。”“觉"'
# text=re.sub(r'，',"",text)
# text=re.sub(r'。',"",text)
# text=re.sub(r'"',"",text)
# text=re.sub(r'“',"",text)
# text=re.sub(r'”',"",text)
# text=re.sub(r'《',"",text)
# text=re.sub(r'》',"",text)
# # print(text)
# f_stop = open('stoplist.txt')
# sw = [line.strip() for line in f_stop]
# texts = ' '.join((jieba.cut(text)))
# print(texts)

import re
import jieba
text='"车厢，设坐票制。昨日，《南都ＭＥＴＲＯ》创刊仪式暨２０１２年深港地铁圈架的车厢和买双副秘书长、轨道交人的需求，提有微高一“我们要稍高一些' \
     '的服务”。比如，尝试有地铁赵鹏林说，比如有些地铁是“观光线”，不仅沿途的风光非常好，还能凭一张票无数次上下，如同旅' \
     '游时提供的“通票服务”。再比门可放大件行李的座位，避免像现在放行李不太方便的现象。“未来地铁建设。”“觉"'
text=re.sub(r'[,，。、《》“”]','',text)
f_stop = open('stoplist.txt')
sw = [line.strip() for line in f_stop]
texts = ' '.join((jieba.cut(text)))
print(texts)