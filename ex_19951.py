def set_order_list():
    for _ in range(M):
        a, b, k = map(int, input().split())
        order_list[a - 1] += k
        order_list[b] -= k

def get_sum():
    end = 0
    for i in range(N):
        end += order_list[i]
        h_list[i] += end
    return h_list

N, M = map(int, input().split())
h_list = list(map(int, input().split()))
order_list = [0 for _ in range(N + 1)]

set_order_list()
result = get_sum()
print(*result)