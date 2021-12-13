import sys


n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
# m.reverse() # 리스트를 거꾸러 변환해 가장 긴 증가하는 부분 수열의 길이를 구하는 방법을 사용
dp = [1] * n

# 반복문을 통해 수열이 증가하는지 확인
for i in range(1, n):
    temp = 0

    # i번의 수와 이전 수들을 비교
    for j in range(i):
        # 두 수를 비교
        if m[i] > m[j]:
            # 증가하는 부분수열의 길이를 구한다.
            if temp < dp[j]:
                temp = dp[j]

    # 증가하는 부분 수열의 길이를 증가시킨다.
    dp[i] = temp + 1

print(max(dp))
