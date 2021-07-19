import sys
from collections import deque


# bfs 탐색
def bfs():

    queue = deque([n])

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:

        # 팝하여 탐색
        a = queue.popleft()

        # 현재 위치가 동생에 위치와 같다면 멈춘다.
        if a == k:
            print(graph[a])
            break

        # 3가지 이동 방법을 수행한다.
        for i in (a - 1, a + 1, a * 2):
            # 이때 정해진 위치로 이동했고 이동하지 않은 위치라면
            # 현재 이동시간 + 1 을 하여 현재 위치까지 가기 위한 시간을 초기화한다.
            # 그리고 다시 리스트에 추가하여 그 위치에서 다시 이동한다.
            if 0 <= i <= 100000 and not graph[i]:
                graph[i] = graph[a] + 1
                queue.append(i)


n, k = map(int,sys.stdin.readline().split())
graph = [0] * 100001
bfs()
