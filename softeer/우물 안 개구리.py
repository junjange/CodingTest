import sys

n, m = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
g = [list(map(int, sys.stdin.readline().split())) for x in range(m)]

# [0] 리스트를 n+1개 만큼 만든다.
# 순서를 맞추기 위해 0번째의 수를 제외한다.
cnt = [1 for _ in range(n+1)]
cnt[0]=0
# 그룹 수 만큼 반복한다.
# A,B가 들 수 있는 무게를 g 리스트에서 가져와 w에 넣어 비교한다.
# 비교할때 더 무거운 무게를 들 수 없다면 0을 부여한다.
for i in range(m):
    if w[g[i][0]-1] > w[g[i][1]-1]:
            cnt[g[i][1]] = 0

    elif w[g[i][0]-1] < w[g[i][1]-1]:
            cnt[g[i][0]] = 0

    else:
        cnt[g[i][0]] = 0
        cnt[g[i][1]] = 0


# cnt 리스트에 1의 개수를 출력한다.
print(cnt.count(1))

