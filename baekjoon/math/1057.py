import sys

n, kim, lim = map(int, sys.stdin.readline().split())
cnt = 0

# kim과 lim이 같은면 같은 라운드에서 만난 것
while kim != lim:
    # kim과 lim 앞에 있는 사람들중 진 사람들을 제외하고
    # kim과 lim의 위치를 초기화한다.
    kim -= kim // 2
    lim -= lim // 2
    cnt += 1 # 카운트

print(cnt)
