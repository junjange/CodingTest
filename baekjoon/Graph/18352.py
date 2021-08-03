import sys
from collections import deque


# bfs 탐색
def bfs(v, w):
    queue = deque([v])
    visited = [-1] * (n + 1)
    visited[v] = 0 # 처음 탐색하는 노드는 최단 거리를 0으로 가정했기 때문에

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:
        target = queue.popleft()

        # 탐색하지 않았다면 탐색
        for i in graph[target]:
            if visited[i] == -1:

                # 탐색 결과를 최단 거리로 체크
                visited[i] = visited[target] + 1
                queue.append(i)

                # 최단 거리가 구하는 거리정보와 같다면 res 리스트에 추가
                if visited[i] == w:
                    res.append(i)

    # res 리스트 리턴
    return res


n, m, k, x = map(int, sys.stdin.readline().split())

# 각 노드가 연결된 정보를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# 결과 리스트
res = []

# bfs 탐색
bfs(x, k)
# 리턴 받은 res 리스트에 값이 있으면 오름차순 후 순서대로 출력
if res:
    res.sort()
    for i in res:
        print(i)

# 없다면 -1 출력
else:
    print(-1)
