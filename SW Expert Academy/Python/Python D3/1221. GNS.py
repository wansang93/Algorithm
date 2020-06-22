T = int(input())
for t in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    words = list(input().split())

    word_dic = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9
    }
    words.sort(key=word_dic.__getitem__)

    print(f'#{t}')
    print(f'{" ".join(words)}')
