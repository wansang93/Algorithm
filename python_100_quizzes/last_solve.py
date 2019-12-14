nationWidth = {
    'Korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England' : 242900,
}

print(nationWidth.keys())  # ['Korea', 'Rusia', 'China', 'France', 'Japan', 'England']
print(nationWidth.values())  # [220877, 17098242, 9596961, 543965, 377915, 242900]
print(nationWidth.items())
# [('Korea', 220877), ('Rusia', 17098242), ('China', 9596961), ('France', 543965), ('Japan', 377915), ('England', 242900)]
print(dir(nationWidth))
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

new = nationWidth.copy()
new.pop('Korea')
print(new)

def min_gap(dic):
    gap = max(dic.values())
    item = max(dic.keys())
    print(item, gap)
    for i in dic:
        if gap > dic[i]:
            gap = dic[i]
            item = i
    return item

print(min_gap(new))





























# w = nationWidth['Korea']
# nationWidth.pop('Korea')
# l = list(nationWidth.items())
# gap = max(nationWidth.values())
# item = 0

# for i in l:
#     if gap > abs(i[1] - w):
#         gap = abs(i[1] - w)
#         item = i
# print(item[0], item[1]-w)