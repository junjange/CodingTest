import sys


t = int(sys.stdin.readline())

# 테스트 케이스를 반복
for _ in range(t):
    r, m = map(str, sys.stdin.readline().split())

    # 반복해야하는 문자를 반복 횟수만큼 출력
    for i in m:
        for j in range(int(r)):
            print(i, end="")
            
    print() # 한줄 들여쓰기
