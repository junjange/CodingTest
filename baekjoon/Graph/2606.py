import sys


# dfs 함수
def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = 1

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

# 각 노드가 연결된 정보를 표현
graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# 각 노드의 방문유무
visited = [0] * (n + 1)

dfs(1)
print(visited.count(1) - 1)


