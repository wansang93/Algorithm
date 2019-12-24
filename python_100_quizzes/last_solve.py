numstr = input()
revnum = numstr[::-1]
n = 0
count = 1
answer = 0
dic = {3: 1, 6: 2, 9: 3}
for c in revnum:
    answer += dic[int(c)] * count
    count *= 3
        
print(answer)