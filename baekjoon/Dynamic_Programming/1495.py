import sys

n, s, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)] # 2차원 배열(각 곡마다 볼륨을 저장)
dp[0][s] = 1

# 반복문을 통해 각 곡을 통해 만들 수 있는 볼륨을 dp에 담는다.
for i in range(n):
    for j in range(m + 1):
        # 현재 i곡의 볼륨이 담겨있다면
        if dp[i][j] == 1:

            # 볼륨을 줄였을 때 0보다 크다면 다음 곡에 현재 볼륨을 담는다.
            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = 1

            # 볼륨을 키웠을 때 m보다 작다면 다음 곡에 현재 볼륨을 담는다.
            if j + v[i] <= m:
                dp[i + 1][j + v[i]] = 1

# 반복문을 통해 마지막 곡에 최대 볼륨을 찾는다.
for k in range(m, -1, -1):
    if dp[n][k] == 1:
        print(k)
        exit()

# 마지막 곡에 볼륨이 없다면 -1 출력
print(-1)
