import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

# 반복문을 통해 수열이 증가하는지 확인
# n번의 수까지 증가하는 길이를 구한다.
for i in range(1, n):
    result_max = 0 # i번의 수를 비교할 변수

    # i번의 수와 그전에 수들을 비교
    for j in range(i):
        # 두 수의 크기 비교
        if a[i] > a[j]:
            # 증가하는 부분 수열의 길이를 구한다.
            if result_max < dp[j]:
                result_max = dp[j]

    # 증가하는 부분 수열의 길이를 증가시킨다.
    dp[i] = result_max + 1

print(max(dp))
