WALL, R, B, SPACE, HOLE = '#', 'R', 'B', '.', 'O'
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
COUNT = 0


def canMove(x, y):
    return 0 <= x < N and 0 <= y < M and board[x][y] == SPACE or board[x][y] == HOLE


def move(dir, pos, count):
    global COUNT
    dx, dy = dir
    x, y = pos

    while canMove(x + dx, y + dy):
        x, y = x + dx, y + dy

        if board[x][y] == HOLE:
            COUNT = count
            return x, y
    return x, y


def getBoard():
    init_board = [[] for _ in range(N)]
    init_stack = [[[], [], 0]]
    for x in range(N):
        init_board[x] = list(input())

        if B in init_board[x]:
            y = init_board[x].index(B)
            B_visited[x][y] = True
            init_stack[0][0] = x, y

        if R in init_board[x]:
            y = init_board[x].index(R)
            R_visited[x][y] = True
            init_stack[0][1] = x, y

    return init_board, init_stack


def getOrder(B_pos, R_pos, dir):
    if dir[0] == 0 and B_pos[0] == R_pos[0]:
        if B_pos[1] * dir[1] > R_pos[1] * dir[1]:
            return [B_pos, R_pos]
        else:
            return [R_pos, B_pos]

    elif dir[1] == 0 and B_pos[1] == R_pos[1]:
        if B_pos[0] * dir[0] > R_pos[0] * dir[0]:
            return [B_pos, R_pos]
        else:
            return [R_pos, B_pos]

    else:
        return [B_pos, R_pos]


N, M = map(int, input().split())
B_visited = [[False] * M for _ in range(N)]
R_visited = [[False] * M for _ in range(N)]
board, stack = getBoard()

while stack:
    B_pos, R_pos, count = stack.pop()

    for dir in DIRECTIONS:
        positions = getOrder(B_pos, R_pos, dir)

        for i in range(2):
            nx, ny = positions[i]
            if canMove(nx, ny):
                x, y = move(dir, positions[i], count)
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                positions[i] = (x, y)

        stack.append([B_pos, R_pos, count + 1])

print(COUNT)