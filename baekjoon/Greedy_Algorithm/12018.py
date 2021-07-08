import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
res = []
cnt = 0

# 과목 수 만큼 반복하여 각 과목의 수강인원을 확인하고 결과 리스트에 담는다.
for i in range(n):
    p, l = map(int, sys.stdin.readline().split())
    mileage = list(map(int, sys.stdin.readline().split()))
    mileage.sort()
    # 각 과목을 신청한 사람 수가 과목의 수강인원보다 크거나 같으면
    # 과목에 커트라인을 리스트에 담는다.
    if p >= l:
        for _ in range(p-l):
            heapq.heappop(mileage)

        res.append(heapq.heappop(mileage))

    # 그게 아니라면 마일리지 1을 넣어도 수강할 수 있게 된다.
    # 따라서 마일리지 1을 리스트에 담는다.
    else:
        res.append(1)

# 과목의 커트라인을 담은 리스트를 내림차순으로 정렬하여
# 마일리지를 제일 적게 사용해서 과목을 최대한 많이 듣게 한다.
res.sort(reverse=True)
for i in range(n):
    m -= res.pop()
    # 마일리지가 0보다 작으면 멈춘다.
    if m < 0:
        break
    cnt += 1

print(cnt)



