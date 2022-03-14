import sys

n, m = map(int, sys.stdin.readline().split())
drawing = [[0 for _ in range(100)] for _ in range(100)] # 그림
cnt = 0 # 모자이크 중에 보이지 않는 그림의 개수

# 반복문을 통해 불투명한 종이를 확인
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # 반복문을 통해 불투명한 종이의
    # 왼쪽 아래 모서리 좌표와 오른쪽 위 모서리 좌표에
    # 포함되는 그림을 카운트
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            drawing[i - 1][j - 1] += 1

# 반복문을 통해 m개 이상 불투명한 종이가 올라가 있는 그림을 카운트
for i in range(100):
    for j in range(100):
        if drawing[i][j] > m:
            cnt += 1
                  
print(cnt)
