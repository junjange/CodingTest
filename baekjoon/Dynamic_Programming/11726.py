import sys
sys.setrecursionlimit(10 ** 6)

# 점화식 : n = 1 일때 1, n = 2 일때 2, n = 3 일때 3, n = 4 일때 5, n = 5 일때, 8
n = int(sys.stdin.readline())
dp = [0] * (n + 1)

# n이 3보다 작을 때는 직사각형을 채우는 방법의 수가 n개이다.
if n < 3:
    print(n)
# n보다 크거나 같다면 점화식을 통해 문제를 수행
else:
    dp[1] = 1 # n = 1 일때 1
    dp[2] = 2 # n = 2 일때 2
    
    # 반복문을 통해 점화식을 코드로 수행
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # n일때 경우의 수에서 10007로 나눈 값을 출력
    print(dp[n] % 10007)
