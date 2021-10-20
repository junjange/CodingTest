import sys
from collections import deque
import heapq


# bfs 탐색
def bfs(x, y):
    global res, eat, size
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 아기 상어가 먹을 수 있는 물고기가 없을 때까지 반복
    while True:
        queue = deque([[x, y, 0]]) # 아기 상어의 x좌표, y좌표, 이동 시간 
        visited = [[False] * n for _ in range(n)] # 탐색 여부
        visited[x][y] = True # 현재 아기 상어의 위치
        heap = [] # 아기 상어가 먹을 수 있는 물고기
        flag = n ** 2 # 아기 상어의 최소 이동 시간

        # 아기 상어가 갈 수 있는 모든 곳을 탐색
        while queue:
            a, b, cnt = queue.popleft()

            # 아기 상어의 최소 이동 시간보다 많은 시간이 필요한 곳부터는 탐색을 멈춘다.
            if cnt > flag:
                break

            # 상/하/좌/우 탐색
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                # 공간 안에 있고 탐색하지 않았고 아기 상어의 크기보다 작거나 같은 물고기 이거나 공간이라면
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] <= size:
                    # 아기 상어보다 작은 물고기 이고 공간이 아니라면
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        heapq.heappush(heap, (nx, ny, cnt + 1)) # 먹을 수 있는 물고기를 힙에 추가
                        flag = cnt # 아기 상어의 최소 이동시간을 초기화

                    queue.append([nx, ny, cnt + 1])
                    visited[nx][ny] = True

        # 아기 상어가 먹을 수 있는 물고기가 있다면
        if len(heap) > 0:
            # 위, 왼쪽에 물고기 부터 우선적으로 먹어야 하기때문에 heapq 를 사용
            x, y, move = heapq.heappop(heap) 
            res += move # 이동 시간을 더해준다.
            eat += 1 # 물고기를 먹는다.
            graph[x][y] = 0 # 먹은 물고기의 자리는 0으로 초기화

            # 먹은 물고기의 수가 아기 상어의 크기와 같다면
            # 아기 상어의 크기를 올려준다.
            if eat == size:
                size += 1
                eat = 0

        # 먹을 물고기가 없으면 탐색을 멈춰준다.
        else:
            break


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
size = 2 # 아기 상어의 크기
res = 0 # 최소 이동 시간
eat = 0 # 먹은 물고기 수

# 아기 상어의 위치를 찾는다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0 # 아기 상어의 위치를 0으로 초기화
            bfs(i, j)
            break
print(res)
