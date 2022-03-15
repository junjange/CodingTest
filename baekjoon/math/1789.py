import sys

s = int(sys.stdin.readline())
n = 1

# n * (n + 1) / 2 => 1부터 n 까지의 합의 공식
# 반복문을 통해 합이 s보다 클 때의 n을 구한다.
while n * (n + 1) / 2 <= s:
    n += 1

# n - 1를 출력
print(n - 1)
