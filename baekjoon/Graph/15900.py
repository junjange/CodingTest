import sys
from collections import deque
# pypy3으로 해결


# bfs 탐색
def bfs(x):

    queue = deque([x])
    cnt = 0
    
    # 큐가 없을 때까지 반복
    while queue:
        target = queue.popleft()
        
        # 현재 노드가 리프 노드이고 1번 노드가 아닐 경우
        if len(graph[target]) == 1 and target != 1:
            # 현재 노드까지 가기 위한 이동 횟수를 더한다.
            cnt += visited[target]
            continue
        
        # 현재 노드와 연결된 노드를 탐색
        for i in graph[target]:
            # 탐색하지 않은 노드일 경우
            if visited[i] == 0:
                
                # 연결된 노드까지 가기위한 이동 횟수를 초기화
                visited[i] = visited[target] + 1
                queue.append(i)
    
    # 이동 횟수에 합을 리턴
    return cnt


n = int(sys.stdin.readline())

# 그래프를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모노드까지 가기 위한 이동 횟수
visited = [0] * (n + 1)

# 1번 노드부터 리프 노드를 확인
res = bfs(1)

# 짝수이면 Yes, 홀수이면 No
if res % 2:
    print("Yes")
else:
    print("No")

    
    
