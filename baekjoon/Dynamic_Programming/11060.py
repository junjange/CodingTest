# 10:25 => 10:51

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [sys.maxsize] * (n + 1)
dp[0] = 0

# 반복문을 통해 점프를 확인한다.
for i in range(n):
    # 점프로 갈 수 있는 칸을 확인
    for j in range(a[i]):
        if i + j + 1 < len(dp):
            # 점프한 칸에 점프 횟수에 값을 최솟값으로 초기화
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)

# 마지막 칸에 점프 횟수가 바꼈다면 점프 횟수를 출력
if dp[n - 1] < sys.maxsize:
    print(dp[n - 1])
else:
    print(-1)
