import sys


n = int(sys.stdin.readline())
num = [input() for _ in range(n)]
i = 1

# 반복문을 통해 학생 번호를 확인
while True:

    # set 자료형을 통해 중복을 확인
    if len(set(map(lambda x: x[-i:], num))) == n:
        print(i)
        break

    i += 1
