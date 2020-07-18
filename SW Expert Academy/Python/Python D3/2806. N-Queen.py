T = int(input())
for t in range(1, T+1):

    result = 0
    def adjacent(level):
        for i in range(level):
            if row[level] == row[i] or abs(row[level] - row[i]) == level - i:
                return False
        return True
            
    def dfs(level):
        global result
        
        if level == N:
            result += 1

        else:
            for i in range(N):
                row[level] = i
                if adjacent(level):
                    dfs(level + 1)

    N = int(input())
    row = [0] * N
    dfs(level=0)
    print(f'#{t} {result}')