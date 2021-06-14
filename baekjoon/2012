import sys

n = int(sys.stdin.readline())
ex = [int(sys.stdin.readline()) for x in range(n)]
# 각 사람이 예상한 등수를 오름차순으로 정렬한다.
ex.sort()
# 랭크를 사람의 수만큼 만든다.
rank = [i for i in range(1, n+1)]
# 불만도 최소합
result = 0

# 랭크에서 각 사람이 예상한 등수를 빼면 불만도에 최소를 구할수있다.
for i in range(n):
    result += abs(rank[i] - ex[i])

print(result)

