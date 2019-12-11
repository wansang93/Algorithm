# 1부터 100까지의(100을 포함) 모든 숫자를 일렬로 놓고 모든 자릿수의 총 합을 구하세요. 

# 예를 들어 10부터 15까지의 모든 숫자를 일렬로 놓으면 101112131415이고 각 자리의 숫자를 더하면 25입니다.

mylist = []
mystr = ""
for i in range(1, 101):
    mylist.append(i)
    mystr += str(i)

print(mylist)
print(mystr)

sum = 0
for i in mystr:
    sum += int(i)

print(sum)