# mydata = ["홍길동","엄석대","연개소문","김첨지"]
# mydata2 = [2, 1, 10, 0]

# newlist = [(i, j) for i, j in zip(mydata, mydata2)]
# newlist = sorted(newlist, key=lambda x: x[1], reverse=True)

# newdic = {}
# for i in range(len(newlist)):
#     newdic[newlist[i][0]] = i+1

# print(newdic)

name = 'A C B D'.split(' ')
point = list(map(int, '70 10 55 40'.split(' ')))

def hojun(x): #이름과 기능을 바꿔서 적용해보세요.
    return x[1]

def sol(name, point):
    d = {}
    z = [[i, j] for i, j in zip(name, point)]
    z = sorted(z, key=hojun, reverse=True)
    
    for i in range(len(z)):
        d[z[i][0]] = i+1
    return d

print(sol(name, point))

#아래 코드를 실행해보세요.
test = 'AA CCCC BBB D'.split(' ')
sorted(test, key=len)