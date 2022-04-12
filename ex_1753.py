import heapq

def dijkstra():
    mid_list = [[end_w_list[K], K]]

    while mid_list:
        mid_w, mid_v = heapq.heappop(mid_list)

        for end_w, end_v in graph[mid_v]:
            if mid_w + end_w < end_w_list[end_v]:
                end_w_list[end_v] = mid_w + end_w
                heapq.heappush(mid_list, [end_w_list[end_v], end_v])

# input
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for i in range(E):
    start, end, w = map(int, input().split())
    graph[start].append([w, end])

# util
INF = 123456789

# solve
end_w_list = [INF] * (V + 1)
end_w_list[K] = 0
dijkstra()

for i in end_w_list[1:]:
    print("INF" if i >= INF else i for i in end_w_list[1:]) 
