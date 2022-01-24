import sys


n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
cnt = 0
flag = True

# 반복문을 통해 행렬 a와 행렬 b를 비교
# 3*3 기준으로 확인하기 위해 n-2, m-2로 반복
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            cnt += 1 # 뒤집기 카운트

            # 반복문을 통해 3*3 크기에 행렬을 뒤집어준다.
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    a[x][y] = 1 - a[x][y]

# 반복문을 통해 a와 b 행렬이 같은지 확인
for k in range(n):
    if a[k] != b[k]:
        flag = False
        break

# a와 b 행렬이 같으면 cnt를 출력 다르다면 -1 출력
if flag:
    print(cnt)
else:
    print(-1)
