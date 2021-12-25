import sys


x, y = map(str, sys.stdin.readline().split())

# 입력받은 두 수를 역순으로 더한다.
z = str(int(x[::-1]) + int(y[::-1]))

# 더한 두 수를 역순으로 변환해 출력
print(int(z[::-1]))
