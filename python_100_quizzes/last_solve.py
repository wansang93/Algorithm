import time

# 1번째 시간
start_time = time.time()
mystr = ""
for i in range(1001):
    mystr += str(i)
print(mystr.count('1'))

end_time = time.time()
result = end_time-start_time + 1

# 2번째 시간 
def count(n):
	countN = str(list(range(n+1))).count('1')
	return countN

start_time2 = time.time()
print(count(1000))
end_time2 = time.time()
result2 = end_time2-start_time2 + 1

# 3번째 시간
start_time3 = time.time()
mystr2 = ''.join(list(map(str, [i for i in range(1001)]))).count('1')
print(mystr2)
end_time3 = time.time()
result3 = end_time3 - start_time3 + 1

print(result)
print(result2)
print(result3)

# 1번째: 1.0059840679168701(가장 느림)
# 2번째: 1.0009987354278564
# 3번째: 1.0009963512420654

