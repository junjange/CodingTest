import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]

_min = 1 # 랜선의 최소 길이
_max = 2e31 # 랜선의 최대 길이

# 이분 탐색
# 랜선의 최소 길이가 최대 길이보다 커질 때까지 반복
while _max >= _min:
    mid = (_max + _min) // 2 # 현재 랜선을 자를 길이
    res = 0

    # 반복문을 통해 랜선을 자른다.
    for i in lan:
        cnt = i // mid
        res += cnt

        # 랜선을 자른 후 남은 랜선이 필요한 랜선보다 많다면
        # 더 이상 랜선을 자를 필요 없기 때문에 반복을 멈춘다.
        if res > n:
            break

    # 필요한 랜선보다 현재 자른 랜선이 크거나 같다면 랜선을 자를 길이를 늘려주기 위해 
    # 랜선의 최소 길이를 현재 랜선을 자른 길이에 + 1 해준 값으로 초기화한다.
    if res >= n:
        _min = mid + 1

    # 필요한 랜선보다 현재 자른 랜선이 작다면 랜선을 자를 길이를 쥴여주기 위해 
    # 랜선의 최대 길이를 현재 랜선을 자른 길이에 - 1 해준 값으로 초기화한다.
    else:
        _max = mid - 1

# 랜선을 자를 수 있는 최대 길이를 출력
print(int(_max))
