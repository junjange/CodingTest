import sys
from collections import deque


# bfs 탐색
def bfs():
    # a 번부터 탐색
    queue = deque([a])
    visited[a] = 1
    
    # 큐에 원소가 없을 때까지 반복
    while queue:

        target = queue.popleft()
        
        # b번 문자를 탐색했다면 b번 문자까지 걸린 탐색 횟수를 리턴
        # 첫 번째에 카운트한 1을 빼준다.
        if visited[b] != 0:
            return visited[b] - 1

        # 치환 가능한 번호를 모두 탐색한다.
        for i in graph[target]:
            if visited[i] == 0:
                visited[i] = visited[target] + 1
                queue.append(i)
                
    # 큐를 모두 확인하고도 b로 치환 못하면 -1 리턴
    return -1


a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1) # 치환까지 걸린 횟수를 체크

# 2차원 그래프를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


print(bfs())
