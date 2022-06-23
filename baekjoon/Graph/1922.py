import sys


# 부모 노드 찾기
def find(p):
    if p == parent[p]:
        return p

    parent[p] = find(parent[p])
    return parent[p]


# 트리 합치기
def union(x, y):
    x = find(x)
    y = find(y)

    if y < x:
        parent[x] = y
    else:
        parent[y] = x


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph.sort(key=lambda x : x[2])
parent = [i for i in range(n+1)]
answer = 0

for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        answer += c


print(answer)
