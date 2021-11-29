import sys

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복한다.
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [1] * (n + 1)

    # 반복문을 통해 점화식을 코드로 수행
    # n = 1일때 1, n = 2일때 1, n = 3일때 1, n = 4일때 2, n = 5일때 2, n = 6일때 3 ..
    # f(n) = f(n - 2) + f(n - 3)
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    print(dp[n - 1])
