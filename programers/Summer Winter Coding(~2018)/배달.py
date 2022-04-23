# 23:15
import sys
from collections import deque
    
        
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    visited = [sys.maxsize] * (N + 1)
    visited[1] = 0
    
    for a, b, c in road:
        
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    queue = deque([[1, 0]])

    # bfs
    while queue:

        target, num = queue.popleft()
        
        for j in graph[target]:
            if num + j[1] <= K and num + j[1] < visited[j[0]]:
                visited[j[0]] = num + j[1]
                queue.append([j[0], num + j[1]])

    
    for k in visited:
        if k != sys.maxsize:
            answer += 1

    return answer
