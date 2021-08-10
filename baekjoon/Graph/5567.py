import sys
from collections import deque


# bfs 탐색
def bfs(x):
    queue = deque([x])
    cnt = 0

    # 자기 자신부터 방문
    visited[x] = 1

    while queue:
        friend = queue.popleft()
        cnt += 1

        # 친구의 친구를 확인
        for j in graph[friend]:
            # 방문하지 않았다면 방문
            if not visited[j]:
                
                # 방문 순서를 카운트
                visited[j] = visited[friend] + 1
                queue.append(j)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 노드 방문 여부와 순서 확인
visited = [0 for i in range(n + 1)]

# 각 연결된 노드를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 나부터 탐색
bfs(1)

# 방문 순서가 2번째인 사람과 3번째인 사람의 수를 합하여 출력
print(visited.count(2) + visited.count(3))

