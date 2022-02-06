import sys

d, k = map(int, sys.stdin.readline().split())

# 반복문을 통해 조건에 맞는 모든 경우를 탐색한다.(1≤A≤B)
for i in range(1, 100000):
    for j in range(1, 100000):
        dp = [0] * (d + 1)
        dp[1] = i
        dp[2] = j

        # d일까지 할머니가 떡을 주는 경우를 탐색
        for l in range(3, d + 1):
            dp[l] = dp[l - 1] + dp[l - 2]

        # 마지막 날에 할머니가 떡을 준 개수가 k개라면
        # 첫 번째날과 두 번째 날에 떡을 준 개수를 출력하고 종료한다.
        if dp[-1] == k:

            print(dp[1])
            print(dp[2])
            exit()
