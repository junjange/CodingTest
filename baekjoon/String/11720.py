import sys


n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().strip())) # 정수형을 리스트로 받는다.

print(sum(m))
