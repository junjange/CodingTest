import sys

n = int(sys.stdin.readline())
m = [0] * 10001
for k in range(1, n + 1):
    m[k] = int(sys.stdin.readline())

dp = [0] * 10001 # 각 잔까지 먹을 수 있는 포도주 양
dp[0] = m[0]
dp[1] = m[1]
dp[2] = m[1] + m[2]

# 반복문을 통해 각 잔의 최대 포도주 양을 구한다.
for i in range(3, n + 1):
    # 현재 포도주를 안먹는 경우, 연속적으로 포도주를 먹는 경우, 이전 포도주를 안먹고 현재 포도주를 먹는경우
    dp[i] = max(dp[i - 1], dp[i - 3] + m[i - 1] + m[i], dp[i - 2] + m[i])

print(dp[n])
