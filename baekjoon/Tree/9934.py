import sys
sys.setrecursionlimit(10 ** 9)


# 분할 정복
def divide(start, end, lev):
    # 시작 점과 끝 점이 크로스되면 리턴
    if start > end:
        return
    center = (start + end) // 2 # 루트 노드
    level[lev].append(n[center]) # 루트 노드를 레벨의 따라 리스트에 추가
    divide(start, center - 1, lev + 1) # 왼쪽 서브 트리의 루트 노드를 재귀적으로 탐색
    divide(center + 1, end, lev + 1) # 오른쪽 서브 트리의 루트 노드를 재귀적으로 탐색


k = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
level = [[] for _ in range(k)] 

# 분활 탐색
divide(0, len(n) - 1, 0)

# 각 레벨의 따라 노드를 출력
for i in level:
    print(*i)
