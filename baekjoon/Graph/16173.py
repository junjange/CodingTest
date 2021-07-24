import sys
from collections import deque


# bfs 탐색
def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:

        a, b = queue.popleft()
        check = graph[a][b]

        # 현재 위치가 승리 지점이면 멈춰 성공 메시지 출력
        if check == -1:
            print("HaruHaru")
            return

        # 우, 하를 이동하여 비교
        for dx, dy in (1, 0), (0, 1):
            x = a + dx * check
            y = b + dy * check

            # 정사각형 구역 내부이고 한번도 방문하지 않았으면 노드를 큐에 넣고 방문 처리한다.
            if 0 <= x < n and 0 <= y < n and visited[x][y] == False:
                queue.append((x, y))
                visited[x][y] = True

    # 모든 상황에서 승리 지점을 가지 못하면 실패 메시지 출력
    print("Hing")


n = int(sys.stdin.readline())
# 2차원 그래프로 표현
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 탐색 여부
visited = [[False] * n for _ in range(n)]
# 탐색
bfs()
