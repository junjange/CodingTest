import sys

n, k = map(int, sys.stdin.readline().split())
Length = list(map(int, sys.stdin.readline().split()))
res = []

# 원생 각각의 키 차이를 구한다.
for i in range(0, n - 1):
    res.append(Length[i+1] - Length[i])

# 키 차이를 오름차순으로 정렬한다.
res.sort()
result = 0

# 학생의 수에서 조를 뺀 수만큼 원생의 키 차이 수를 반복하여 최소 비용을 구한다.
for i in range(n - k):
    result += res[i]

print(result)

