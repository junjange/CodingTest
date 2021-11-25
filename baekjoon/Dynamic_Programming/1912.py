import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
dp = [m[0]] # 0번째 인덱스의 수를 미리 리스트 안에 넣는다.

# 반복문을 통해 각 인덱스의 최댓값을 구한다.
for i in range(n - 1):
    # 이전 수들의 합이랑 현재 수를 더한 값과 현재 수 중 큰 값을 리스트에 추가
    dp.append(max(dp[i] + m[i + 1], m[i + 1]))

print(max(dp))
