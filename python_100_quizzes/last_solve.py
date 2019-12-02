name = input().split()
score = map(int, input().split())
dic = dict(zip(name, score))
print(dic)