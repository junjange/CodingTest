import sys
from collections import deque


def bfs():
    visited = [1e9] * 1000001
    queue = deque([s])
    visited[s] = 0
    while queue:
        target = queue.popleft()
        if target == g:
            return visited[target]
        for i in (u, -d):
            if 1 <= i + target <= f and visited[i + target] == 1e9:
                visited[i + target] = min(visited[target] + 1, visited[i + target])
                queue.append(i + target)

    return "use the stairs"


# f: 건물 층수
# s: 현재 위치
# g: 스타트 링크 위치
# u: 위로 가는 버튼
# d: 아래로 가는 버튼
f, s, g, u, d = map(int, sys.stdin.readline().split())

print(bfs())
