from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    # 그래프로 표현
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])
    visited[1] = 1
    
    # bfs 탐색
    while queue:
        x = queue.popleft()

        for i in graph[x]:

            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1

    answer = visited.count(max(visited))
    return answer



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
