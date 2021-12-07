import sys


n = int(sys.stdin.readline())

# 상근이가 먼저 시작한 후
# 남은 돌의 개수가 짝수면 창영 승, 홀수면 상근 승
if (n - 1) % 2:
    print("CY")
else:
    print("SK")
