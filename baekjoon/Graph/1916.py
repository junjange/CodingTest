import sys
import heapq


# bfs 탐색
def bfs():
    heap = []
    heapq.heappush(heap, [start, 0])
    visited[start] = 0

    while heap:
        x, y = heapq.heappop(heap)
        # 현재 도시까지 가는데 드는 비용이 더 적으면 넘어간다.
        if visited[x] < y:
            continue

        # 도시와 연결되어 있는 도시들을 확인
        for i, j in graph[x]:

            # 다음 도시까지 가는데 드는 비용을 확인
            target = j + y
            # 다음 도시까지 가는데 드는 비용과 이전에 그 도시까지 걸린 비용을 비교
            if target < visited[i]:
                # 다음 도시까지 가는데 드는 비용을 초기화
                visited[i] = target

                heapq.heappush(heap, [i, target])


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 2차원 그래프로 표현
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
start, end = map(int, sys.stdin.readline().split()) # 출발 도시와 도착 도시
# 비용을 최대로 정의
INF = sys.maxsize
visited = [INF] * (n + 1)
bfs() # bfs 탐색

# 도착 도시까지 가는데 드는 최소 비용 출력
print(visited[end])
