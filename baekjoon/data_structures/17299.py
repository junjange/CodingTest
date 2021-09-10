import sys
from collections import Counter # collections 모듈에 Counter 클래스 사용

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
counter = Counter(a) # Counter 클래스를 통해 a 리스트 안에 담긴 등장 횟수를 확인
stack = [0]

res = [-1] * n

for i in range(1, n):
    # 인덱스를 통해 오등큰수가 있는지 확인
    while stack and counter[a[stack[-1]]] < counter[a[i]]:
        # 오등큰수이면 비교한 값을 팝하고 오등큰수를 입력받는다.
        # 위 과정을 오큰수 리스트가 사라지거나 오등큰수가 아닐 때까지 한다.
        res[stack.pop()] = a[i]

    # 오등큰수를 비교할 인덱스를 추가한다.
    stack.append(i)

print(*res)

