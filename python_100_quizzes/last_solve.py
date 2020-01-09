# 1. 직원은 2000명이며, 3초 이내 수행을 해야합니다.
# 2. 입력값의 형식은 csv파일이며 이과장 '3,000,000', 'S은행', '100-0000-0000-000' 형식으로 주어집니다.
# 3. 출력값의 형식은 csv 파일이며 이과장 '1,500,000', '1,500,000', 'S은행', '100-0000-0000-000' 입니다. 또는 '1,000,000', '2,000,000', 'S은행', '100-0000-0000-000' 도 괜찮습니다.
# 4. 라이브러리 사용할 수 있습니다.

# import os
# dirname = os.path.dirname(__file__)
# print(dirname)
# filename = os.path.join(dirname, 'csv092.csv')
# filename = dirname + '\\ex.csv'

# f = open(filename, encoding='utf-8')
# r = csv.reader(f)
# print(r)  # <_csv.reader object at 0x000001933B2B95F8>

import csv
import os

with open(os.path.dirname(__file__)+'\\092.csv', 'r', encoding='utf-8') as f:
    t = csv.reader(f)
    for line in t:
        s1, s2 = '', ''
        for i in line[1].replace(',', ''):
            if i == '3':
                s1 += '1'
                s2 += '2'
            elif i == '4':
                s1 += '2'
                s2 += '2'
            elif i == '6':
                s1 += '1'
                s2 += '5'
            else:
                s1 += i
                s2 += '0'
        line[1] = (s1, s2)
        print(line)