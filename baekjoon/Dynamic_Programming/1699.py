# pypy3 (통과)
# python3 (시간초과)
import sys

n = int(sys.stdin.readline())
dp = [x for x in range(100001)] # 각 자연수를 만드는 제곱수에 최대 항의 개수

# 반복문을 통해 각 자연수를 확인
for i in range(1, n + 1):
    # 반복문을 통해 각 자연수를 만드는 제곱수에 항의 개수를 구한다.
    for j in range(1, i):

        # 각 자연수가 제곱수보다 작다면 제곱수로 항의 개수를 만들지 못하므로 반복을 멈춘다. 
        if i < j * j:
            break
        
        # 각 자연수를 만드는 제곱수에 최소 항의 개수를 구한다.
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[n])
