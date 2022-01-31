import sys


word = list(map(int, sys.stdin.readline().strip()))

# 암호를 해석할 수 없는 경우는 첫 번째 숫자가 0인 경우
if word[0] == 0:
    print(0)

# 암호를 해석 할 수 있다면
else:

    word = [0] + word
    dp = [0] * len(word)
    dp[0] = 1 # 첫 번째 암호와 두 번째 암호를 더했을 때 해석 가능한 경우의 수
    dp[1] = 1 # 첫 번째 암호를 해석 가능한 경우의 수

    # 반복문을 통해 암호가 해석 되는지 확인
    for i in range(2, len(word)):

        # 현재 암호가 해석이 되는지
        if word[i] > 0:
            dp[i] += dp[i - 1]

        # 이전 암호 숫자와 현재 암호 숫자를 더해 암호를 해석 할 수 있는지 확인
        temp = word[i - 1] * 10 + word[i]

        if 9 < temp < 27:
            dp[i] += dp[i - 2]

        # 현재 암호까지 해석 할 수 있는 경우의 수
        dp[i] %= 1000000

    # 마지막 수까지 해석 할 수 있는 경우의 수 출력
    print(dp[-1] % 1000000)
