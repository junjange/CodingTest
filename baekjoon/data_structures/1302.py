import sys
from collections import Counter

n = int(sys.stdin.readline())
temp = []
for _ in range(n):
    temp.append(str(sys.stdin.readline().strip()))

res = Counter(temp) 
# 람다 정렬을 통해 개수를 내림차순으로 이름을 오름차순으로 정렬
res = sorted(res.items(), key=(lambda x: (-x[1], x[0])))
# 출력
print(res[0][0])
