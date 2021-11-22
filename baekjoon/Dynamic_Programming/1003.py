import sys

t = int(sys.stdin.readline())
dp = [1] * 42

dp[0] = 0 # 피보나치 수 0일때, 0
dp[1] = 1 # 피보나치 수 1일때, 1

# 점화식을 통해 0과 1의 호출 횟수를 구한다.
for i in range(2, 41):
    dp[i] = dp[i - 2] + dp[i - 1]

# 테스트 케이스만큼 반복하여 답을 구한다.
for _ in range(t):
    n = int(sys.stdin.readline())

    print(dp[n - 1], dp[n])
