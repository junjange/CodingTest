import sys
from collections import Counter


t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    n = int(sys.stdin.readline())
    temp = []

    # 의상의 이름과 종류를 입력받는다.
    for i in range(n):
        a, b = map(str, sys.stdin.readline().split())
        temp.append(b) # 의상의 종류를 리스트에 추가

    # 의상의 종류가 들어있는 리스트를 카운터 함수를 통해 개수를 확인한다.
    res = Counter(temp)

    # (의상의 개수 + 1) 을 모든 의상의 종류를 곱한 후 - 1 해준다.
    num = 1
    for j in res:
        num *= (res[j] + 1)
        
    print(num - 1)
