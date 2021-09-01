import sys
from collections import deque
import heapq


# bfs 탐색
def bfs(start):
    # heap 리스트에 시작 정점까지 걸리는 거리와 시작 정점을 푸시한다.
    heap = []
    heapq.heappush(heap, [0, start])
    # 시작점 자신은 0으로 출력
    visited[start] = 0

    while heap:
        x, y = heapq.heappop(heap)

        # 각 정점에서 연결되어있는 다른 정점을 확인
        for aim, d in graph[y]:
            # 현재 정점부터 다른 정점까지 걸린 거리와
            target = d + x # d : 현재 정점부터 다른 정점까지 걸린 거리, x : 이전 정점부터 현재 정점까지 걸린 거리

            # 이전 정점부터 다음 정점까지 걸린 거리와 이전에 정의 된 다음 정점까지 걸린 거리를 비교
            if target < visited[aim]:
                # 정점까지 걸린 거리를 초기화
                visited[aim] = target
                
                heapq.heappush(heap, [target, aim])


v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

# 2차원 그래프를 표현
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

# 모든 경로의 거리를 무한대로 정의
INF = 100000000
visited = [INF] * (v + 1)

# 시작 정점부터 탐색
bfs(k)

for i in visited[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")

        
        
