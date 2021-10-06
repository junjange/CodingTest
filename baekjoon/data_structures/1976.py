import sys
sys.setrecursionlimit(10 ** 6)


# a가 속한 집합과 b가 속한 집합 합치기
def union(x, y):
    x = find(x)
    y = find(y)

    # a와 b의 부모 노드가 같으면 동일한 집합이므로 리턴
    if x == y:
        return
    # 부모 노드가 다르다면 두 집합을 합친다.
    else:
        parent[y] = x


# 부모 노드 찾기
def find(target):
    # 자기 자신이 부모 노드이면 자기 자신을 리턴
    if target == parent[target]:
        return target

    # 부모 노드를 재귀함수를 통해 찾는다.
    parent[target] = find(parent[target])

    # 자신의 부모 노드를 리턴
    return parent[target]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [0] * (n + 1)

for k in range(1, n + 1):
    parent[k] = k

for i in range(1, n + 1):
    # 그래프로 표현
    graph = list(map(int, sys.stdin.readline().split()))

    # 현재 도시와 연결되어 있는 도시를 확인
    for j in range(1, len(graph) + 1):
        if graph[j - 1] == 1:
            union(i, j) # 두개의 도시를 합칩합으로 표현

# 여행 계획
tour = list(map(int, sys.stdin.readline().split()))

# set() 함수를 통해 합칩합을 찾는다. 즉, 모든 도시가 연결되어 있는지 확인한다.
res = set([find(i) for i in tour])

# res 의 길이가 1일 경우 모든 도시가 연결되어 있다는 것이다.
if len(res) == 1: 
    print('YES')
else:
    print('NO')
