import sys

n = int(sys.stdin.readline())
names = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
names.sort(key=lambda x : (int(x[3]) , int(x[2]), int(x[1]))) # 년/월/일 기준으로 졍렬

# 갸장 나이가 적은 사람의 이름, 가장 나이가 많은 사람 이름을 출력
print(names[-1][0])
print(names[0][0])
