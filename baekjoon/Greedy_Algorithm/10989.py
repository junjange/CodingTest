import sys

n = int(sys.stdin.readline())
dp = [0] * 10001

# 반복문을 통해 dp[idx] 위치에 수를 카운트한다.
for _ in range(n):
    dp[int(sys.stdin.readline())] += 1

# 10001번 반복해서 받은 수에 개수를 출력한다.
for i in range(1, 10001):
    for _ in range(dp[i]):
        print(i)
