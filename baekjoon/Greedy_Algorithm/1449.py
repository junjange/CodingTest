import sys

n, l = map(int, sys.stdin.readline().split())
position = list(map(int, sys.stdin.readline().split()))
# 가까운 위치부터 수리하기위해 오름차순으로 정렬 한다.
position.sort()

# 수리를 한 위치
repair = 0
# 테이프 사용 횟수
cnt = 0

# 반복문을 통해 물이 새는 곳의 위치를 확인한다.
for i in position:
    # 수리를 한 위치와 물이 새는 곳의 위치 비교
    if repair < i:
        # 테이프 하나로 수리
        cnt += 1
        # 물이 새는 곳의 위치와 테이프 길이를 더해 수리를 한 위치를 바꿈
        # 물이 새는 곳부터 수리를 하기 때문에 -1을 해준다.
        repair = i + l - 1

print(cnt)