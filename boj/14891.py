LEFT, RIGHT = 6, 2
record = [0] * 5
gears = [""] + [input() for _ in range(4)]

for info in [list(map(int, input().split())) for _ in range(int(input()))]:
    x, direction = info
    visited = [False] * 5

    stack = [[x, -direction]]
    while stack:
        x, direction = stack.pop()

        if not visited[x]:
            visited[x] = True

            if x - 1 > 0 and gears[x - 1][(RIGHT + record[x - 1]) % 8] != gears[x][(LEFT + record[x]) % 8]:
                stack.append([x - 1, -direction])

            if x + 1 <= 4 and gears[x + 1][(LEFT + record[x + 1]) % 8] != gears[x][(RIGHT + record[x]) % 8]:
                stack.append([x + 1, -direction])

            record[x] += direction

print(sum([int(gears[i + 1][record[i + 1] % 8]) * pow(2, i) for i in range(4)]))
