import sys
from collections import deque


# bfs 탐색
def bfs(v):
    cnt = 0
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while q:
        a = q.popleft()
        cnt += 1

        # 해킹하지 않았으면 해킹을 한다.
        for j in graph[a]:
            if not visited[j]:
                visited[j] = True
                q.append(j)

    # 방문한 정점의 수를 리턴
    return cnt


n, m = map(int, sys.stdin.readline().split())

# 2차원 리스트의 맵 정보를 입력 받는다.
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[y].append(x)

cnt_max = 0
result = []
for i in range(1, n + 1):
    if graph[i]:
        tmp = bfs(i)

        # bfs를 통해 리턴값을 받고 최대값과 비교
        if cnt_max <= tmp:
            # 최대값이 더 작으면 결과값을 초기화한다.
            if cnt_max < tmp:
                result = []
            cnt_max = tmp
            result.append(i)

print(*result)
