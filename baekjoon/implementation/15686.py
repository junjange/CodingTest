import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
house = [] # 집의 좌표
chick = [] # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chick.append([i, j])

answer = sys.maxsize
for chi in combinations(chick, m): # combinations을 통해 m개의 치킨집 선택
    temp = 0 # 도시의 치킨 거리
    for h in house:
        chi_len = sys.maxsize # 각 집마다 치킨 거리
        for k in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[k][0]) + abs(h[1] - chi[k][1]))
        temp += chi_len
    answer = min(answer, temp)

print(answer)
