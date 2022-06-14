import sys

# #/
# 정리!
# 1. 반복문을 통해서 코인을 확인
# 2. 1원부터 m원까지 돈(j) - 코인(i) => 0보다 크다면 코인으로 만들 수 있는 돈
# 3. dp[j] += dp[j - i]
# 4. 위 식의 j - i의 경우 이전에 dp의 저장된 j-i번 째의 수를 가져와 사용하는 것을 의미
# 5. 즉, j - i를 사용했을 때의 경우의 수에 i를 더한 것
# i == 1일 때
# 1원 : 1
# 2원 : 11
# 3원 : 111
# 4원 : 1111
# 5원 : 11111
# ....
# j == 2일 때
# 1원 : 1
# 2원 : 11 2 => j - i = 0이기 때문에 dp[0]인 경우를 더한다.
# 3원 : 111 12 => j - i = 1이기 때문에 dp[1]인 경우를 더한다.
# 4원 : 1111 112 22 => j - i = 2이기 때문에 dp[2]인 경우를 더한다.
# 5원 : 11111 1112 122  => j - i = 3기 때문에 dp[3]인 경우를 더한다.
# #/

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coin = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    dp = [0] * 10001
    dp[0] = 1

    # 반복문을 통해 코인을 확인
    for i in coin:
        # 반복문을 통해 코인으로 1원부터 m원까지 만들 수 있는 경우의 수를 확인
        for j in range(1, m + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]

    print(dp[m])
