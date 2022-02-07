# pypy3 해결(python3 시간초과)
import sys

n = int(sys.stdin.readline())

balls = [] # 만들 수 있는 사면체
ball = 0

# 반복문을 통해 각 사면체를 만드는데 사용되는 대포알의 개수를 balls에 저장한다.
for i in range(1, 300001):
    ball += (i * (i + 1)) // 2
    balls.append(ball)

    # 사면체를 만드는데 사용되는 대포알의 개수가
    # 현재 다솜이의 해적선에 있는 대포알보다 크다면 그 이후의 대포알은 계산 할 필요없다.
    if balls[-1] >= n:
        break

dp = [float('inf')] * (n + 1)

# 반복문을 통해 대포알의 개수에 따라 만들 수 있는 사면체를 확인
for j in range(1, n + 1):
    for k in balls:
        # 현재 대포알의 개수로 사면체를 만들 수 있으면
        if k == j:
            dp[j] = 1
            break
        # 대포알의 개수로 사면체를 만들 수 없다면
        if k > j:
            break

        # 현재 대포알의 개수로 만들 수 있는 사면체를 확인
        dp[j] = min(dp[j], dp[j - k] + 1)
        
print(dp[n])
