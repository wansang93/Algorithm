# 점수입력 : 97 86 75 66 55 97 85 97 97 95
# 출력 : 6

l = list(map(int, list(input().strip().split())))

count = 3
#3개는 무조건 구매, 배열 정렬 후 1~3위 중 중복되는 숫자까지 포함

data_sorted = sorted(list(l))
print(l)
print(data_sorted)
for i in range(len(l)-1, 0, -1):
	if data_sorted[-3] == l[i]:
		count += 1
print(count)