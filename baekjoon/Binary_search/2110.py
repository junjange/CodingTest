import sys

n, c = map(int, sys.stdin.readline().split())
x = sorted(int(sys.stdin.readline()) for _ in range(n))

_max = x[-1] # 마지막 집
_min = 1 # 첫 번째 집

# 이분 탐색
while _max >= _min:

    mid = (_max + _min) // 2 # 공유기를 설치할 간격
    insert = x[0] # 공유기를 설치한 집
    cnt = 1 # 공유기의 설치 개수

    # 반복문을 통해 공유기를 설치
    for i in x:
        # 현재 집의 위치가 공유기를 설치한 집과의 간격이 같거나 크다면 공유기를 설치한다.
        if i >= insert + mid:
            insert = i # 공유기를 설치한 집 초기화
            cnt += 1 # 카운트

        # 공유기의 개수가 설치한 개수보다 크다면
        # 더 이상 공유기를 설치할 필요 없으므로 반복을 멈춰준다.
        if cnt > c:
            break

    # 공유기의 개수가 설치한 개수보다 작거나 같다면 설치하는 간격을 늘려준다.
    if cnt >= c:
        _min = mid + 1

    # 공유기의 개수가 설치한 개수보다 크다면 설치하는 간격을 줄여준다.
    else:
        _max = mid - 1

# 가장 인접한 두 공유기 사이의 최대 거리 출력
print(_max)
