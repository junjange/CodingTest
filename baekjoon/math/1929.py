import sys

m, n = map(int, sys.stdin.readline().split())
dp = [False, False] + [True] * 1000001
primes = []

# 에라토스테네스의 체를 통해 소수를 구한다.
for i in range(2, n+1):
    if dp[i]:
        primes.append(i)
        for j in range(i*2, n+1, i):
            dp[j] = False


# 구한 소수가 범위 내에 있다면 출력
for i in primes:
    if i > n:
        break

    if i >= m:
        print(i)

