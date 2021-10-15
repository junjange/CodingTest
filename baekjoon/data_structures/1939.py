import sys
from collections import deque


# bfs 탐색
def bfs():
    queue = deque([start])
    visited[start] = True

    # 큐가 없을 때까지 반복
    while queue:

        # 현재 섬
        target = queue.popleft()

        # 현재 탐색하는 섬이 도착해야하는 섬이라면 True 리턴
        if target == end:
            return True

        # 현재 탐색하고 있는 섬과 연결되어 있는 섬 확인
        for i, j in graph[target]:
            # 탐색하지 않은 섬이고 현재 중량으로 갈 수 있는 섬이면
            if not visited[i] and mid <= j:
                visited[i] = True
                queue.append(i)

    # 도착해야하는 섬을 도착하지 못했다면 False 리턴
    return False


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
start, end = map(int, sys.stdin.readline().split())

_min = 1 # 최솟값
_max = 1000000000 # 최댓값
# 이분 탐색
while _min <= _max:
    visited = [False] * (n + 1) # 탐색 여부
    mid = (_min + _max) // 2 # 현재 중량

    # bfs 탐색
    if bfs():
        # True 일 경우 이동이 가능, 중량 증가
        # 최솟값을 중간보다 + 1 해준다.
        _min = mid + 1

    else:
        # False 일 경우 이동이 불가, 중량 감소
        # 최댓값을 중간 보다 -1 해준다.
        _max = mid - 1

# 최대 중량
print(_max)
