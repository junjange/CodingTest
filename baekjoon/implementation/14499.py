import sys


# 주사위 굴리기
def solution(v):
    # 동
    if v == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]

    # 서
    elif v == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]

    # 북
    elif v == 3: 
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    
    # 남
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
order = list(map(int, sys.stdin.readline().split()))
dice = [0, 0, 0, 0, 0, 0, 0]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
 

for i in order:
    # 지도 범위 내에 주사위를 굴릴 수 있는지 확인
    if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
        x += dx[i] # 지도 x좌표
        y += dy[i] # 지도 y좌표
        solution(i) # 주사위 굴리기

        # 좌표가 지도의 0인 곳이라면
        # 주사위에 맨 밑에 수를 지도에 복사한다.
        if graph[x][y] == 0:
            graph[x][y] = dice[1]
        
        # 0이 아니라면 주사위에 맨 밑에 수에 지도의 수를 복사한다.
        # 지도의 수는 0으로 초기화한다.
        else:
            dice[1] = graph[x][y]
            graph[x][y] = 0
        
        # 주사위에 맨 위에 수를 출력
        print(dice[6])
