# pypy3 해결.. 
# python3 (94%) 시간초과

import sys
sys.setrecursionlimit(10 ** 5)


# dfs 탐색
def dfs(x, l):
    visited[x] = True
    level[x] = l

    # 현재 노드와 연결되오 있는 노드 확인
    for i in tree[x]:

        # 탐색하지 않은 노드라면 재귀적으로 탐색
        if not visited[i]:
            parent[i] = x # 부모 노드로 초기화
            dfs(i, l + 1)


# lca 알고리즘
def lca(a, b):

    # 레벨을 맞춘다.
    while level[a] != level[b]:
        # a의 레벨을 높인다.
        if level[a] > level[b]:
            a = parent[a]

        # b의 레벨을 높인다.
        else:
            b = parent[b]

    # a와 b의 공통 조상을 찾는다.
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


n = int(sys.stdin.readline())

# 각 노드가 연결된 정보를 트리로 표현
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1) # 각 노드의 부모 노드 정보
level = [0] * (n + 1) # 각 노드의 레벨
visited = [0] * (n + 1) # 방문 여부

# 루트 노드부터 연결된 노드를 탐색
dfs(1, 0)

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))
