T = int(input())
for t in range(1, T+1):
    text = input()
    answer = 'Not exist'

    for i in range(len(text)//2+1):
        if text[i] != '?' and text[-i-1] != '?':
            if text[i] != text[-i-1]:
                break
    else:
        answer = 'Exist'

    print(f'#{t} {answer}')