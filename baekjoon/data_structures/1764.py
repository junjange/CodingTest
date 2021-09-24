import sys
from collections import Counter # collections 모듈에 Counter 클래스 사용

n, m = map(int, sys.stdin.readline().split())
res = []
name = []
for i in range(n + m):
    name.append(str(sys.stdin.readline().strip("\n")))

temp = Counter(name) # 이름의 수를 확인

# 반복을 통해 중복되는 이름이 있는지 확인
for i in name:
    # 카운트가 2번 이상인 사람이고
    # 그 사람의 이름이 리스트의 없다면 리스트에 추가한다.
    if temp[i] >= 2 and i not in res:
        res.append(i)

# 오름차순으로 정렬한다.
res.sort()

print(len(res))
for i in res:
    print(i)
