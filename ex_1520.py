import sys
input = sys.stdin.readline

def dfs(x, y):
    if dp_graph[x][y] >= 0:
        return dp_graph[x][y]

    dp_graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if is_promise(nx, ny, graph[x][y]):
            dp_graph[x][y] += dfs(nx, ny)
    
    return dp_graph[x][y]

# input
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

# util
dx = (1, 0, 0, -1)
dy = (0, 1, -1, 0)
is_promise = lambda x, y, value : 0 <= x < M and 0 <= y < N and value > graph[x][y]

# solve
dp_graph = [[-1] * N for _ in range(M)] # [x][y]에서 출발해 [-1][-1]에 도달할 수 있는 경우의 수
dp_graph[M - 1][N - 1] = 1
print(dfs(0, 0))