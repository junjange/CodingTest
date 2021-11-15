import sys

n, k = map(int, sys.stdin.readline().split())

bag = [[0, 0]]
for _ in range(n):
    bag.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*(k + 1) for _ in range(n + 1)]

# 물건의 수에 따라 가방에 물건을 얼마나 담을 수 있는지 확인
# 반복문을 통해 각 물건의 무게와 가치를 확인
for i in range(1, n + 1):
    w = bag[i][0]
    v = bag[i][1]

    # 가방의 무게
    for j in range(1, k + 1):

        # 현재 비교하고 있는 가방의 최대 무게가 현재 물건의 무게보다 작다면
        # 이전에 비교했던 가방의 무게에 현재 물건을 담을 수 있는 가치가 최대 가치가 된다.
        if j < w:
            dp[i][j] = dp[i - 1][j]

        # 현재 비교하고 있는 가방의 최대 무게가 비교하고 있는 물건의 무게보다 크거나 같다면
        # 이전에 비교했던 가방의 현재 무게의 가치와 이전에 비교했던 가방의 무게에서 현재 물건의 무게만큼 뺀 무게의 가치 + 현재 물건의 가치 중
        # 제일 큰 가치가 현재 가방에 담을 수 있는 최대 가치가 된다.
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
