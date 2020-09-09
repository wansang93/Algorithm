from collections import Counter

def get_2grams(str):
    list_set = []
    for i in range(len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            list_set.append(str[i]+str[i+1])

    return list_set

def solution(str1, str2):    
    str1_set = Counter(get_2grams(str1.lower()))
    str2_set = Counter(get_2grams(str2.lower()))

    intersection_set = str1_set & str2_set
    union_set = str1_set | str2_set

    len_intersection_set = sum(intersection_set.values())
    len_union_set = sum(union_set.values())

    if len_union_set == 0:
        return 65536
    else:
        return int(len_intersection_set / len_union_set * 65536)

print(solution("aa1+aa2", "AAAA12"))


# 다른 사람 풀이
import re
import math

def solution2(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)