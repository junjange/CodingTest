import sys


# 점화식 : (n > 3), f(n) = f(n - 1) + f(n - 2) + f(n - 3)
def dp(v):
    # 1을 만들 수 있는 경우의 수 : 1
    if v == 1:
        return 1

    # 2을 만들 수 있는 경우의 수 : 2
    elif v == 2:
        return 2

    # 3을 만들 수 있는 경우의 수 : 4
    elif v == 3:
        return 4

    # 그 외 수를 만들 수 있는 경우의 수는 재귀 호출을 통해 구한다.
    else:
        return dp(v - 1) + dp(v - 2) + dp(v - 3)


t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복하여 함수를 수행
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp(n))

