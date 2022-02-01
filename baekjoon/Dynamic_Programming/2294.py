import sys


n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
dp = [100001] * (k + 1)
dp[0] = 0 # 0원을 만들기 위한 코인의 개수는 0

# 반복문을 통해 코인으로 1부터 k가치를 확인
for i in coin:
    for j in range(1, k + 1):
        # 코인으로 현재 가치를 만들 수 있다면
        # 현재 가치를 만든 코인의 개수와 j - i를 만든 코인의 개수에서 +1해준 값을 비교
        if j - i >= 0:
            dp[j] = min(dp[j], dp[j - i] + 1)


# k를 구하기 위한 경우의 수가 100001 불가능한 경우
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
