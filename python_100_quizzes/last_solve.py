l = [10, 20, 25, 27, 34, 35, 39] #기존 입력 값
n = int(input('순회 횟수는: '))

def rotate(inL, inN):
    newL = inL.copy()
    sub = []
    for i in range(inN):
        newL.insert(0, newL.pop())
    
    for i, j in zip(inL, newL):
        sub.append(abs(i-j))
    index = sub.index(min(sub))
    print("index: {}".format(index))
    print("value: %d %d"%(inL[index], newL[index]))

rotate(l, n)