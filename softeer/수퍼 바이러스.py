import sys


# 지수를 재귀적으로 나눈다.
def f(x, y):
    if y == 1:
        return x

    elif y % 2 == 0:
        a = f(x, y / 2)
        return a * a % 1000000007

    else:
        b = f(x, (y - 1) / 2)
        return b * b * x % 1000000007


k, p, n = list(map(int, sys.stdin.readline().split()))
# 0.1초당 p배씩 증가이기 때문에 계산을 편리하게 하기위해 n을 10배 해준다.
n = 10 * n
result = f(p, n)
result *= k
print(result % 1000000007)
