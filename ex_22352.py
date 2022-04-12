import sys
input = sys.stdin.readline


# input
def get_input():
    N, M = map(int, input().split())
    before = [list(map(int, input().split())) for _ in range(N)]
    after = [list(map(int, input().split())) for _ in range(N)]

    return N, M, before, after

class Ex_22352:
    def __init__(self, N, M, before, after) -> None:
        self.N, self.M, self.before, self.after = N, M, before, after
        
        self.dx = (1, 0, 0, -1)
        self.dy = (0, 1, -1, 0)
        self.visited = [[False] * M for _ in range(N)]

        # util
        self.find_diff_node = lambda : next(([col, row] for row in range(M) for col in range(N) if self.before[col][row] != self.after[col][row]), None)
        self.is_promise = lambda x, y, origin: 0 <= x < N and 0 <= y < M and not self.visited[x][y] and self.before[x][y] == origin

    def dfs(self, node, target):
        stack = [node]
        origin_num = self.before[node[0]][node[1]]

        while stack:
            x, y = stack.pop()
            self.visited[x][y] = True
            self.before[x][y] = target
            
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                
                if self.is_promise(nx, ny, origin_num):
                    stack.append([nx, ny])
    
    def print_result(self):
        # find diff node after modify
        print("NO" if self.find_diff_node() else "YES")
        
    def solve(self):
        # dfs diff node
        node = self.find_diff_node()
        if node:
            after_num = self.after[node[0]][node[1]]
            self.dfs(node, after_num) 

if __name__ == "__main__":
    N, M, before, after = get_input()
    problem = Ex_22352(N, M, before, after) 
    problem.solve()
    problem.print_result()