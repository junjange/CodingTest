import sys
from collections import deque

n = int(sys.stdin.readline())

# 2차원 그래프로 표현
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색 유무
visited = [False] * (n + 1)
parent = [0] * n

# 큐에 1번 노드를 추가하여 모든 노드를 탐색
queue = deque([1])
while queue:
    temp = queue.popleft()

    # 1번 노드와 연결된 노드중에 탐색하지 않은 노드를 추가
    for i in graph[temp]:
        if not visited[i]:
            queue.append(i)

            # 부모 노드를 추가
            parent[i - 1] = temp

            # 탐색 체크
            visited[i] = True

# 1번 노드를 제외한 나머지 노드를 순서대로 출력
for i in parent[1:]:
    print(i)
