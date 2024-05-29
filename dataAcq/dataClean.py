# 数据清洗
import pandas as pd
import re
import time

# 先读取数据文件
data = pd.read_csv('book.csv')
result = pd.DataFrame(data)

a = result.dropna(axis=0, how='any')
pd.set_option('display.max_rows', None)  # 输出全部行，不省略

b = u'数据'
number = 1

b1 = '1981-8'
li1 = a['出版社']
for i in range(0, len(li1)):
    try:
        if b1 in li1[i]:
            # print(number,li1[i])
            number += 1
            a = a.drop(i, axis=0)
    except:
        pass

b2 = '中国基督'
a['出版时间'] = a['出版时间'].str[0: 5]
li2 = a['出版时间']
for i in range(0, len(li2)):
    try:
        if b2 in li2[i]:
            # print(number,li2[i])
            number += 1
            a = a.drop(i, axis=0)
    except:
        pass

b3 = 'CNY'
li3 = a['价格']
for i in range(0, len(li3)):
    try:
        if b3 in li3[i]:
            a['价格'] = li3.str.replace('CNY', '')
    except:
        pass

b41 = '清'
b42 = '明'
li4 = a['国家']
a['国家'] = li4.str.replace("国", "")
for i in range(0, len(li4)):
    try:
        if b41 in li4[i]:
            a['国家'] = li4.str.replace('清', '中')
        if b42 in li4[i]:
            a['国家'] = li4.str.replace('明', '中')
    except:
        pass

time.sleep(3)

a.to_csv('newbook.csv', index=False, encoding='gbk')
print('数据清洗完成！')