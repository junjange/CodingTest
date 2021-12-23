import sys


n = list(map(int, sys.stdin.readline().strip()))
n.sort(reverse= True) # 입력받은 수를 내림차순으로 정렬

# 반복문을 통해 수를 출력
for i in n:
    print(i, end="")
