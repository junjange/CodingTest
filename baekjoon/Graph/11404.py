import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

# 자기 자신으로 오는 경우는 x
for _ in range(n + 1): graph[_][_] = 0

# 반복문을 통해 그래프를 표시
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    if graph[s][e] > c:
        graph[s][e] = c

# 반복문을 통해 경로 확인
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):

            # 자기 자신으로 오는 경우는 x
            if j == k:
                graph[j][k] = 0

            # j -> k 로 가는 경우와 j -> i -> k 로 가는 경우중 비용이 적게드는 것을 확인
            else:
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 반복문을 통해 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
