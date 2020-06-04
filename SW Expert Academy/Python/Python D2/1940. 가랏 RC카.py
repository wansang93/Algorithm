T = int(input())
for t in range(1, T+1):
    N = int(input())
    speed = 0
    distance = 0
    for n in range(N):
        command = input()
        if command == '0':
            command = '0 0'
        
        command, acceleration = map(int, command.split())

        if command == 1:
            speed += acceleration
        elif command == 2:
            speed -= acceleration
            if speed < 0:
                speed = 0
        distance += speed

    print(f'#{t} {distance}')
